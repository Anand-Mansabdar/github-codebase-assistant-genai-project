from pathlib import Path
from pydantic.dataclasses import dataclass
from langchain_text_splitters import RecursiveCharacterTextSplitter

@dataclass
class ChunkMetaData:
  chunk_id: str
  content: str
  source_file: Path
  language: str
  start_line: int
  end_line: int
  class_name: str | None = None
  function_name: str | None = None