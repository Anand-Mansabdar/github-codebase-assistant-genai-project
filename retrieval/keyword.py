import re
from rank_bm25 import BM25Okapi
from retrieval.models import SearchResult

class KeywordIndex:
  def __init__(
    self,
    documents: list[SearchResult],
  ):
    self.documents = documents
    self.tokenized_documents = [
      self._tokenize(document.content) for document in documents
    ]
    
    self.bm25 = BM25Okapi(
      self.tokenized_documents
    )
  
  
  def _tokenize(
    self,
    text: str,
  ) -> list[str]:
    return re.findall(
      r"\b\w+\b",
      text.lower()
    )
    
  
  def search(
    self,
    query: str,
    n_results: int = 5,
  ) -> list[tuple[SearchResult, float]]:
    query_tokens = self._tokenize(query)
    scores = self.bm25.get_scores(
      query_tokens
    )
    
    ranked = sorted(
      zip(self.documents, scores),
      key=lambda item: item[1],
      reverse=True,
    )
    
    return ranked[:n_results]