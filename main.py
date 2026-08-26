from repository.clone_repo import clone_repository
from repository.file_loader import load_repository_files
from indexing.indexer import build_repository_index
from embeddings.document_builder import build_embedding_documents

repo_path = clone_repository(
    "https://github.com/Anand-Mansabdar/AskAnand.AI---AI-Portfolio-Assistant-for-my-resumes"
)

files = load_repository_files(repo_path)

repository_index = build_repository_index(
    repository_path=repo_path,
    files=files
)

documents = build_embedding_documents(repository_index.chunks)

print(
    f"Embedding documents: {len(documents)}"
)

document = documents[1]

print(document.text)
print()
print(document.metadata)