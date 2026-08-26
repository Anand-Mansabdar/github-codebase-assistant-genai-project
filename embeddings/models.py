from dataclasses import dataclass
from chunking.models import ChunkMetaData

@dataclass
class EmbeddingDocument:
  text: str
  metadata: dict
  chunk: ChunkMetaData
  
  