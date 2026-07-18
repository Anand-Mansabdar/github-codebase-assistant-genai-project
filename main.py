from config.settings import settings
from repository.clone_repo import get_repository_name, validate_github_url, clone_repository

print("=" * 50)
print(settings.app_name)
print(f"Version : {settings.app_version}")
print(f"Debug   : {settings.debug}")
print(f"Repo    : {settings.repository_path}")
print("=" * 50)

repo = clone_repository("https://github.com/Anand-Mansabdar/github-codebase-assistant-genai-project.git")

print(repo)