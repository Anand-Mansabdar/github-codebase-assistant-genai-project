from repository.clone_repo import clone_repository
from repository.file_loader import load_repository_files
from indexing.indexer import build_repository_index
from embeddings.document_builder import build_embedding_documents
from embeddings.model import EmbeddingModel
from vector_store.store import ChromaVectorStore

repo_path = clone_repository(
    "https://github.com/Anand-Mansabdar/ai-coding-agent-assignment.git"
)

files = load_repository_files(repo_path)

repository_index = build_repository_index(
    repository_path=repo_path,
    files=files
)

documents = build_embedding_documents(repository_index.chunks)

embedding_model = EmbeddingModel()

texts = [
    document.text
    for document in documents
]

vectors = embedding_model.embed_documents(
    texts
)

store = ChromaVectorStore()

store.reset()

store.add_documents(
    documents=documents,
    embeddings=vectors
)

print(f"Chroma Documents: {store.count()}")

query = "Query about your project"

query_embedding = embedding_model.embed_text(
    query
)

results = store.search(
    query_embedding=query_embedding,
    n_results=5,
)

for document, metadata, distance in zip(
    results["documents"][0],
    results["metadatas"][0],
    results["distances"][0],
):

    print("=" * 80)

    print("Distance:", distance)
    print("File:", metadata["source_file"])
    print("Class:", metadata["class_name"])
    print("Function:", metadata["function_name"])

    print(document[:500])