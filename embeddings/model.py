from sentence_transformers import SentenceTransformer
from config.settings import settings

class EmbeddingModel:
  def __init__(self):
    self.model = SentenceTransformer(
      settings.EMBEDDING_MODEL
    )
    
  def embed_text(self, text: str) -> list[float]:
    vector = self.model.encode(text, convert_to_numpy=True)
    
    return vector.tolist()
  
  
  def embed_documents(self, texts: list[str]) -> list[list[float]]:
    vectors = self.model.encode(texts, convert_to_numpy=True, show_progress_bar=True)
    
    return vectors.tolist()