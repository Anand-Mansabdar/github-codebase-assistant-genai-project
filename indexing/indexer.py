import logging
from pathlib import Path
from repository.metadata import FileMetadata
from chunking.models import ChunkMetaData
from chunking.splitter import split_file
from chunking.enricher import enrich_chunk
from parsing.parser import analyze_file
from indexing.models import RepositoryIndex

logger = logging.getLogger(__name__)

def index_file(file_metadata: FileMetadata) -> list[ChunkMetaData]:
  chunks = split_file(file_metadata)
  
  if not chunks:
    return []
  
  if file_metadata.language == "Unknown":
    return chunks
  
  try:
    structure = analyze_file(file_metadata)
  except Exception:
    logger.exception("AST analysis filed for %s", file_metadata.relative_path)
    return chunks
  
  enriched_chunks = []
  
  for chunk in chunks:
    enriched_chunk = enrich_chunk(chunk, structure)
    
    enriched_chunks.append(enriched_chunk)
  return enriched_chunks 


def build_repository_index(repository_path: Path, files: list[FileMetadata]) -> RepositoryIndex:
  all_chunks = []
  
  for file_metadata in files:
    chunks = index_file(file_metadata=file_metadata)
    
    all_chunks.extend(chunks)
  
  return RepositoryIndex(
    repository_path=repository_path,
    chunks=all_chunks
  )