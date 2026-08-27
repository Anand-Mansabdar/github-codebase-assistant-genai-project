from repository.clone_repo import clone_repository
from repository.file_loader import load_repository_files
from indexing.indexer import build_repository_index
from embeddings.document_builder import build_embedding_documents
from embeddings.model import EmbeddingModel
from vector_store.store import ChromaVectorStore
from retrieval.retriever import CodeRetriever
from retrieval.formatter import format_context

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
vector_store = ChromaVectorStore()

retriever = CodeRetriever(
    embedding_model=embedding_model,
    vector_store=vector_store
)

results = retriever.retrieve(
    query="Where is JWT authentication implemented?",
    n_results=5,
)

for result in results:

    print("=" * 80)

    print("File:", result.source_file)
    print(
        "Lines:",
        result.start_line,
        "-",
        result.end_line,
    )

    print("Language:", result.language)
    print("Class:", result.class_name)
    print("Function:", result.function_name)
    print("Distance:", result.distance)

    print()
    print(result.content[:500])

context = format_context(results)
print(context)