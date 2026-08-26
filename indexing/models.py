from dataclasses import dataclass, field
from pathlib import Path
from chunking.models import ChunkMetaData

@dataclass
class RepositoryIndex:
  repository_path: Path
  chunks: list[ChunkMetaData] = field(default_factory=list)
  
  @property
  def total_chunks(self) -> int:
    return len(self.chunks)
  
  @property
  def total_files(self) -> int:
    return len({
      chunk.source_file for chunk in self.chunks
    })
  
  @property
  def languages(self) -> set[str]:
    return {
      chunk.language for chunk in self.chunks
    }