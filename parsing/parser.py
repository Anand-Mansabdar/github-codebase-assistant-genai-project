from pathlib import Path
from tree_sitter import Parser
from parsing.language import get_language
from repository.metadata import FileMetadata
from parsing.ast_models import CodeStructure
from parsing.ast_models import FunctionInfo, ClassInfo


def create_parser(language: str) -> Parser:
  ts_language = get_language(language=language)
  parser = Parser(ts_language)
  return parser


def parse_source(source_code: str, language: str):
  parser = create_parser(language=language)
  source_bytes = source_code.encode("utf-8")
  tree = parser.parse(source_bytes)
  
  return tree


def walk_tree(node):
  yield node
  
  for child in node.children:
    yield from walk_tree(child)
    

def extract_functions(tree):
  functions = []
  
  for node in walk_tree(tree.root_node):
    if node.type != "function_definition":
      continue
    
    name_node = node.child_by_field_name("name")
    
    if name_node is None:
      continue
    
    function_name = name_node.text.decode("utf-8")
    
    functions.append(FunctionInfo(
      name=function_name,
      start_line=node.start_point[0]+1,
      end_line=node.end_point[0] + 1
    ))
    
  return functions


def extract_classes(tree) -> list[ClassInfo]:
  classes = []
  
  for node in walk_tree(tree.root_node):
    if node.type != "class_definition":
      continue
    
    name_node = node.child_by_field_name("name")
        
    if name_node is None:
      continue
    
    class_name = name_node.text.decode("utf-8")
    
    methods = []
    body = node.child_by_field_name("body")
    
    if body is not None:
      for child in body.named_children:
        if child.type != "function_definition":
          continue
        
        method_name_node = child.child_by_field_name("name")
        
        if method_name_node is None:
          continue
        
        methods.append(
          FunctionInfo(
            name=method_name_node.text.decode("utf-8"),
            start_line=child.start_point[0]+1,
            end_line=child.end_point[0] + 1
          )
        )
    
    classes.append(
      ClassInfo(
        name=class_name,
        start_line=node.start_point[0] + 1,
        end_line=node.end_point[0] + 1,
        methods=methods
      )
    )
    
  return classes

def extract_imports(tree) -> list[str]:
  imports = []
  
  for node in walk_tree(tree.root_node):
    if node.type not in {"import statement", "import_from_statement"}:
      continue
    
    if node.text is None:
      continue
    
    import_text = node.text.decode("utf-8").strip()
    imports.append(import_text)
  return imports


def extract_top_level_functions(tree) -> list[FunctionInfo]:
  functions = []
  
  for node in tree.root_node.named_children:
    if node.type != "function_definition":
      continue
    
    name_node = node.child_by_field_name("name")
    
    if name_node is None:
      continue
    
    functions.append(
      FunctionInfo(
        name=name_node.text.decode("utf-8"),
        start_line=node.start_point[0]+1,
        end_line=node.end_point[0]+1
      )
    )
  return functions


def analyze_file(file_metadata: FileMetadata) -> CodeStructure:
  source_code = file_metadata.absolute_path.read_text(encoding="utf-8", errors="ignore")
  
  tree = parse_source(source_code=source_code, language=file_metadata.language)
  
  return CodeStructure(
    file_path=file_metadata.relative_path,
    language=file_metadata.language,
    imports=extract_imports(tree=tree),
    functions=extract_functions(tree=tree),
    classes=extract_classes(tree=tree)
  )