import math

from retrieval.keyword import KeywordIndex
from retrieval.models import SearchResult
from retrieval.retriever import CodeRetriever
from embeddings.model import EmbeddingModel

class HybridRetriever:
  def __init__(
    self,
    semantic_retriever: CodeRetriever,
    keyword_index: KeywordIndex,
    embedding_model: EmbeddingModel,
  ):
    self.semantic_retriever = semantic_retriever
    self.keyword_index = keyword_index
    self.embedding_model = embedding_model
    
  def retrieve(
    self,
    query: str,
    n_results: int = 5,
  ) -> list[SearchResult]:

    semantic_results = (
      self.semantic_retriever.retrieve(
          query=query,
          n_results=10,
      )
    )

    keyword_results = (
      self.keyword_index.search(
          query=query,
          n_results=10,
      )
    )
    
    candidates = self._combine_results(
      semantic_results,
      keyword_results,
    )
    
    candidates = candidates[:20]
    query_embedding = (
    self.embedding_model.embed_text(query))
    
    candidate_embeddings = self._get_embeddings(
    candidates)
    return self._mmr(
      query_embedding=query_embedding,
      candidate_results=candidates,
      candidate_embeddings=candidate_embeddings,
      k=n_results,
      lambda_param=0.7,
    )
    
  def _normalize(
    self,
    scores: list[float],
  ) -> list[float]:
    if not scores:
      return []

    minimum = min(scores)
    maximum = max(scores)

    if maximum == minimum:
      return [1.0 for _ in scores]

    return [
      (score - minimum) / (maximum - minimum) for score in scores
    ]
      
  def _combine_results(
    self,
    semantic_results: list[SearchResult],
    keyword_results: list[tuple[SearchResult, float]],
  ) -> list[SearchResult]:

    scores: dict[tuple, float] = {}

    semantic_scores = [
      result.relevance_score
      for result in semantic_results
    ]

    normalized_semantic = self._normalize(
      semantic_scores
    )

    for result, score in zip(
      semantic_results,
      normalized_semantic,
    ):
      key = (
        result.source_file,
        result.start_line,
        result.end_line,
      )

      scores[key] = (
        scores.get(key, 0.0)+ 0.6 * score
      )
    
    keyword_raw_scores = [
      score  for _, score in keyword_results
    ]

    normalized_keyword = self._normalize(
      keyword_raw_scores
    )

    for (result, _), score in zip(keyword_results,normalized_keyword):
      key = (
        result.source_file,
        result.start_line,
        result.end_line,
      )

      scores[key] = (
        scores.get(key, 0.0)+ 0.4 * score
      )
    
    result_map = {}

    for result in semantic_results:
      key = (
        result.source_file,
        result.start_line,
        result.end_line,
      )

      result_map[key] = result

    for result, _ in keyword_results:
      key = (
        result.source_file,
        result.start_line,
        result.end_line,
      )

      result_map[key] = result
      
    ranked = sorted(
      result_map.items(),
      key=lambda item: scores[item[0]],
      reverse=True,
    )

    return [
        result_map[key]
        for key, _ in ranked
    ]
    
  def _get_embeddings(
    self,
    results: list[SearchResult],
  ) -> list[list[float]]:

    texts = [
      result.content for result in results
    ]

    return self.embedding_model.embed_documents(texts) 
  
  def _cosine_similarity(
    self,
    a: list[float],
    b: list[float],
  ) -> float:

    dot_product = sum(
      x * y
      for x, y in zip(a, b)
    )

    magnitude_a = math.sqrt(
      sum(x * x for x in a)
    )

    magnitude_b = math.sqrt(
      sum(x * x for x in b)
    )

    if magnitude_a == 0 or magnitude_b == 0:
      return 0.0

    return dot_product / (magnitude_a * magnitude_b)
  
  def _mmr(
    self,
    query_embedding: list[float],
    candidate_results: list[SearchResult],
    candidate_embeddings: list[list[float]],
    k: int = 5,
    lambda_param: float = 0.7,
  ) -> list[SearchResult]:

    if not candidate_results:
      return []

    selected = []
    selected_indices = set()

    query_similarities = [
      self._cosine_similarity(
        query_embedding,
        embedding,
      )
      for embedding in candidate_embeddings
    ]

    while (
      len(selected) < k
      and len(selected_indices)
      < len(candidate_results)
    ):
      best_index = None
      best_score = float("-inf")

      for index in range(len(candidate_results)):
        if index in selected_indices: continue
        relevance = query_similarities[index]

        if not selected:
          diversity = 0.0

        else:
          diversity = max(
            self._cosine_similarity(
              candidate_embeddings[index],
              candidate_embeddings[selected_index],
            )
            for selected_index in selected_indices
          )

        mmr_score = (
          lambda_param * relevance- (1 - lambda_param) * diversity)

        if mmr_score > best_score:
          best_score = mmr_score
          best_index = index

        selected_indices.add(best_index)
        selected.append(candidate_results[best_index])

    return selected