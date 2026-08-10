from repository.clone_repo import clone_repository
from repository.file_loader import load_repository_files
from chunking.splitter import split_file


repo_path = clone_repository(
    "https://github.com/Anand-Mansabdar/github-codebase-assistant-genai-project.git"
)

files = load_repository_files(repo_path)

print(f"Files discovered: {len(files)}")

first_file = files[0]

chunks = split_file(first_file)

print(f"Chunks generated: {len(chunks)}")

for chunk in chunks[:3]:
    print("\n" + "=" * 80)
    print(f"File: {chunk.source_file}")
    print(f"Language: {chunk.language}")
    print(f"Lines: {chunk.start_line}-{chunk.end_line}")
    print("=" * 80)
    print(chunk.content)