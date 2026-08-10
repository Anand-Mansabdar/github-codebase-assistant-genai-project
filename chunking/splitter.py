from pathlib import Path
from uuid import uuid4

from chunking.models import ChunkMetaData
from repository.metadata import FileMetadata
from chunking.strategies import create_splitter

def read_file(path: Path) -> str:
  with path.open("r", encoding="utf-8", errors="ignore") as file:
    return file.read()
  
  
def split_file(file_metadata: FileMetadata, chunk_size: int = 1200, chunk_overlap: int=200) -> list[ChunkMetaData]:
  content = read_file(file_metadata.absolute_path)
  
  if not content.strip():
    return []
  
  splitter = create_splitter(
    language=file_metadata.language,
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap
  )
  
  chunks = splitter.split_text(content)
  
  results = []
  
  search_position = 0
  
  for chunk in chunks:
    start_position = content.find(chunk, search_position)
    
    if start_position == -1:
      start_position = search_position
  
    end_position = start_position + len(chunk)
  
    start_line = content.count("\n", 0, start_position) + 1
    end_line = content.count("\n", 0, end_position) + 1
  
    chunk_id = str(uuid4())
  
    results.append(
      ChunkMetaData(
        chunk_id= chunk_id,
        content=chunk,
        source_file=file_metadata.relative_path,
        language=file_metadata.language,
        start_line=start_line,
        end_line=end_line
      )
    )
  
    search_position = start_position + len(chunk)

  return results