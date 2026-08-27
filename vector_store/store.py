# Responsible for:
# Adding and searching documents.

from typing import Any
from chromadb.api.models.Collection import Collection
from embeddings.models import EmbeddingDocument
from vector_store.client import get_chroma_client
from config.settings import settings

class ChromaVectorStore:
  def __init__(self):
    self.client = get_chroma_client()
    self.collection = self.client.get_or_create_collection(
      name=settings.COLLECTION_NAME
    )
    
  def add_documents(
    self, 
    documents: list[EmbeddingDocument],
    embeddings: list[list[float]],
  ) -> None:
    if len (documents) != len(embeddings):
      raise ValueError("Number of documents and embeddings must match.")
    
    self.collection.add(
      ids=[
        document.chunk.chunk_id for document in documents
      ],
      documents=[
        document.text for document in documents
      ],
      embeddings=embeddings,
      metadatas=[
        document.metadata for document in documents
      ]
    )
  
  def reset(self) -> None:
    self.client.delete_collection(
      name=settings.COLLECTION_NAME
    )
    
    self.collection = self.client.get_or_create_collection(
      name=settings.COLLECTION_NAME
    )
  
  # Add Collection Statistics - Useful for debugging:
  def count(self) -> int:
    return self.collection.count()
  
  # Implement Semantic Search
  def search(
    self,
    query_embedding: list[float],
    n_results: 5,
  ) -> dict[str, Any]:
    return self.collection.query(
      query_embeddings=[query_embedding],
      n_results=n_results
    )