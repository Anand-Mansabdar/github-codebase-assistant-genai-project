from config.settings import settings
from repository.clone_repo import get_repository_name, validate_github_url

print("=" * 50)
print(settings.app_name)
print(f"Version : {settings.app_version}")
print(f"Debug   : {settings.debug}")
print(f"Repo    : {settings.repository_path}")
print("=" * 50)

print(get_repository_name("https://github.com/microsoft/vscode"))

print(validate_github_url("hello"))
print(validate_github_url("https://google.com"))
print(validate_github_url("https://github.com/langchain-ai/langchain"))