from embeddings.model import EmbeddingModel
from retrieval.models import SearchResult
from vector_store.store import ChromaVectorStore

class CodeRetriever:
  def __init__(self, embedding_model: EmbeddingModel, vector_store: ChromaVectorStore):
    self.embedding_model = embedding_model
    self.vector_store =vector_store
      
  
  def retrieve(self, query: str, n_results: int = 5) -> list[SearchResult]:
    query_embedding = self.embedding_model.embed_text(query)
    
    raw_results = self.vector_store.search(
      query_embedding=query_embedding,
      n_results=n_results
    )
    
    return self._parse_results(raw_results)
  
  
  def _parse_results(self, results: dict) -> list[SearchResult]:
    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]
    
    search_results = []
    
    for document, metadata, distance in zip(
      documents, metadatas, distances,
    ):
      search_results.append(
        SearchResult(
          content=document,
          source_file=metadata["source_file"],
          language=metadata["language"],
          start_line=int(metadata["start_line"]),
          end_line=int(metadata["end_line"]),
          class_name=metadata.get("class_name") or None,
          function_name=metadata.get("function_name") or None,
          distance=float(distance),
        )
      )

    return search_results
  