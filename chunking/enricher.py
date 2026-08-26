from parsing.ast_models import CodeStructure
from parsing.relationships import find_class_for_lines, find_function_for_lines
from chunking.models import ChunkMetaData


def enrich_chunk(chunk: ChunkMetaData, structure: CodeStructure) -> ChunkMetaData:
  class_name = find_class_for_lines(structure, chunk.start_line, chunk.end_line)
  
  function_name = find_function_for_lines(structure, chunk.start_line, chunk.end_line)
  
  chunk.class_name = class_name
  chunk.function_name = function_name
  
  return chunk