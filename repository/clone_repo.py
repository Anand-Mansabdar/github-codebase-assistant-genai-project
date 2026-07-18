# Only responsible for cloning repositories.

# It should not know:

# embeddings
# LangChain
# AST parsing
# LLMs

from pathlib import Path
from git import Repo
from urllib.parse import urlparse
from config.settings import settings
from utils.logger import console
from exceptions.repository_exceptions import RepositoryCloneError

# Function to get the repository name
def get_repository_name(url: str) -> str:
  parsed_url = urlparse(url=url)
  repo_name = Path(parsed_url.path).stem
  return repo_name


def validate_github_url(url: str) -> bool:
  parsed_url = urlparse(url=url)
  
  return (
    parsed_url.scheme in ("http", "https") 
    and parsed_url.netloc == "github.com"
    and len(parsed_url.path.strip("/").split("/")) >= 2
  )
  
  
def clone_repository(url: str) -> Path:
  if not validate_github_url(url):
    raise ValueError("Invalid GitHub repository URL.")
  
  repo_name = get_repository_name(url=url)
  repositories_root = Path(settings.repository_path)
  
  repositories_root.mkdir(
    parents=True,
    exist_ok=True
  )
  
  local_repository_path = repositories_root / repo_name
  
  if local_repository_path.exists():
    return local_repository_path
  
  console.print("📦 Cloning repository...")
  
  try:
    Repo.clone_from(
      url=url, 
      to_path=local_repository_path
    )
    console.print("✓ Clone successful.")
  except RepositoryCloneError:
    console.print("RepositoryCloneError")
  
  
  return local_repository_path