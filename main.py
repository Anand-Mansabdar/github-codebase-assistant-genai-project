from repository.clone_repo import clone_repository
from repository.file_loader import load_repository_files
from chunking.splitter import split_file
from parsing.parser import analyze_file
from chunking.enricher import enrich_chunk

repo_path = clone_repository(
    "https://github.com/Anand-Mansabdar/AskAnand.AI---AI-Portfolio-Assistant-for-my-resumes.git"
)

files = load_repository_files(repo_path)
python_files = next(
    file for file in files if file.language == "Python"
)

structure = analyze_file(python_files)

chunks = split_file(python_files)

for chunk in chunks:
    enrich_chunk(chunk=chunk, structure=structure)
    
    print("=" * 80)

    print("File:", chunk.source_file)
    print("Lines:", chunk.start_line, "-", chunk.end_line)
    print("Class:", chunk.class_name)
    print("Function:", chunk.function_name)

    print(chunk.content)