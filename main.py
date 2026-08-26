from repository.clone_repo import clone_repository
from repository.file_loader import load_repository_files
from chunking.splitter import split_file
from parsing.parser import analyze_file
from chunking.enricher import enrich_chunk
from indexing.indexer import build_repository_index

repo_path = clone_repository(
    "https://github.com/Anand-Mansabdar/AskAnand.AI---AI-Portfolio-Assistant-for-my-resumes"
)

files = load_repository_files(repo_path)

repository_index = build_repository_index(
    repository_path=repo_path,
    files=files
)

print(f"Total chunks: {repository_index.total_chunks}")

for chunk in repository_index.chunks[:10]:
    print("=" * 80)

    print("File:", chunk.source_file)
    print("Language:", chunk.language)
    print("Lines:", chunk.start_line, "-", chunk.end_line)
    print("Class:", chunk.class_name)
    print("Function:", chunk.function_name)

    print(chunk.content[:300])