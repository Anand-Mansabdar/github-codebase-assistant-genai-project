# from llm.client import GroqClient


# client = GroqClient()

# answer = client.generate(
#     system_prompt="You are a helpful coding assistant.",
#     user_prompt="Explain what a Python decorator is.",
# )

# print(answer)

from embeddings.model import EmbeddingModel
from vector_store.store import ChromaVectorStore

from retrieval.retriever import CodeRetriever

from llm.client import GroqClient
from llm.generator import CodebaseAnswerGenerator

from rag.pipeline import CodebaseRAG


embedding_model = EmbeddingModel()

vector_store = ChromaVectorStore()

retriever = CodeRetriever(
    embedding_model=embedding_model,
    vector_store=vector_store,
)

llm_client = GroqClient()

generator = CodebaseAnswerGenerator(
    llm_client=llm_client,
)

rag = CodebaseRAG(
    retriever=retriever,
    generator=generator,
)

answer = rag.answer(
    "Where is JWT authentication implemented?"
)

print(answer)