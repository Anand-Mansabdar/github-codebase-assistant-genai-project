from embeddings.model import EmbeddingModel
from vector_store.store import ChromaVectorStore

from retrieval.retriever import CodeRetriever
from retrieval.evaluator import display_results


embedding_model = EmbeddingModel()

vector_store = ChromaVectorStore()

retriever = CodeRetriever(
  embedding_model=embedding_model,
  vector_store=vector_store,
)

queries = [
  "Where is JWT authentication implemented?",
  "Where are API endpoints defined?",
  "How are exceptions handled?",
  "Where is conversation memory implemented?",
  "Where is the LLM initialized?",
]

for query in queries:
  results = retriever.retrieve(
    query=query,
    n_results=5,
  )

  display_results(
    query=query,
    results=results,
  )