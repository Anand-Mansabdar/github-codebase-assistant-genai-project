from config.settings import settings
from repository.clone_repo import get_repository_name

print("=" * 50)
print(settings.app_name)
print(f"Version : {settings.app_version}")
print(f"Debug   : {settings.debug}")
print(f"Repo    : {settings.repository_path}")
print("=" * 50)

print(get_repository_name("https://github.com/microsoft/vscode"))