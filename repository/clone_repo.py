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