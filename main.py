from repository.clone_repo import clone_repository
from repository.file_loader import load_repository_files
from indexing.indexer import build_repository_index
from embeddings.document_builder import build_embedding_documents
from embeddings.model import EmbeddingModel

repo_path = clone_repository(
    "https://github.com/Anand-Mansabdar/AskAnand.AI---AI-Portfolio-Assistant-for-my-resumes"
)

files = load_repository_files(repo_path)

repository_index = build_repository_index(
    repository_path=repo_path,
    files=files
)

documents = build_embedding_documents(repository_index.chunks)

embedding_model = EmbeddingModel()
text = """
File: backend/api.py
Language: Python
Class: ChatRequest
Function: validate_question

Code:
def validate_question(value):
    ...
"""

vector = embedding_model.embed_text(text)

print("Vector dimensions:", len(vector))
print("First 10 values:", vector[:10])


texts = [
    document.text
    for document in documents
]

vectors = embedding_model.embed_documents(
    texts
)

print("Documents:", len(documents))
print("Vectors:", len(vectors))
print("Dimensions:", len(vectors[0]))