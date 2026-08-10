from pathlib import Path
from tree_sitter import Parser
from parsing.language import get_language


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
    
    functions.append({
      "name": function_name,
      "start_line": node.start_point[0] +1, 
      "end_line": node.end_point[0] +1, 
    })
    
  return functions


def extract_classes(tree):
  classes = []
  
  for node in walk_tree(tree.root_node):
    if node.type != "class_definition":
      continue
    
    name_node = node.child_by_field_name("name")
        
    if name_node is None:
      continue
        
    class_name = name_node.text.decode("utf-8")
        
    classes.append({
      "name": class_name,
      "start_line": node.start_point[0] +1, 
      "end_line": node.end_point[0] +1, 
    })
        
    return classes
    
    