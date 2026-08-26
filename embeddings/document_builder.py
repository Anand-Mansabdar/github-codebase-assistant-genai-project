from chunking.models import ChunkMetaData
from embeddings.models import EmbeddingDocument

def build_embedding_text(chunk: ChunkMetaData) -> str:
  parts = [
    f"File: {chunk.source_file}",
    f"Language: {chunk.language}"
  ]
  
  if chunk.class_name:
    parts.append(
      f"Class: {chunk.class_name}"
    )
  
  if chunk.function_name:
    parts.append(
      f"Function: {chunk.function_name}"
    )
  
  parts.append(
    f"Lines: {chunk.start_line}-{chunk.end_line}"
  )
  
  parts.append(
    f"\nCode:\n{chunk.content}"
  )
  
  return "\n".join(parts)


# Build the Metadata Dictionary
def build_metadata(chunk: ChunkMetaData) -> dict:
  return {
    "source_file": str(chunk.source_file),
    "language": chunk.language,
    "start_line": chunk.start_line,
    "end_line": chunk.end_line,
    "class_name": chunk.class_name or "",
    "function_name": chunk.function_name or "",
  }
  
# Build the Final Document
def build_embedding_document(chunk: ChunkMetaData) -> EmbeddingDocument:
  return EmbeddingDocument(
    text=build_embedding_text(chunk=chunk),
    metadata=build_metadata(chunk=chunk),
    chunk=chunk
  )
  
  
# Build Documents for the Whole Repository
def build_embedding_documents(chunks: list[ChunkMetaData]) -> list[EmbeddingDocument]:
  return [
    build_embedding_document(chunk=chunk) for chunk in chunks
  ]