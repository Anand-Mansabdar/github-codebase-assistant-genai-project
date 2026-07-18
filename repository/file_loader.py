# Once the repo exists locally, this module walks through it.

from pathlib import Path
from repository.file_filter import should_index
from repository.metadata import (
  FileMetadata,
  detect_language
)
from utils.progress import progress


def load_repository_files(repo_path: Path) -> list[FileMetadata]:
  files = []
  
  if not repo_path.exists():
    raise FileNotFoundError("The file does not exist.")
  
  all_paths = list(repo_path.rglob("*"))
  
  for path in progress(all_paths, "📂Scanning Repository..."):
    if not path.is_file():
      continue
    
    if path.is_symlink():
      continue
    
    if not should_index(path=path):
      continue
    
    relative_path = path.relative_to(repo_path)
    
    metadata = FileMetadata(
      absolute_path=path, 
      relative_path=relative_path,
      filename=path.name,
      extension=path.suffix,
      size=path.stat().st_size,
      language=detect_language(path.suffix)
    )
    
    files.append(metadata)
    
  return files
