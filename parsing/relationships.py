from parsing.ast_models import CodeStructure

def find_function_for_lines(structure: CodeStructure, start_line:int, end_line:int) -> str | None:
  for function in structure.functions:
    if ranges_overlap(start_line, end_line, function.start_line, function.end_line):
      return function.name
    
  for class_info in structure.classes:
    if ranges_overlap(start_line, end_line, class_info.start_line, class_info.end_line):
      return class_info.name
      
  return None

def find_class_for_lines(structure: CodeStructure, start_line:int, end_line:int) -> str | None:
  for class_info in structure.classes:
    if ranges_overlap(start_line, end_line, class_info.start_line, class_info.end_line):
      return class_info.name
  
  return None

def ranges_overlap(start_a: int, end_a: int, start_b:int, end_b:int) -> bool:
  return start_a <= end_b and start_b <= end_a