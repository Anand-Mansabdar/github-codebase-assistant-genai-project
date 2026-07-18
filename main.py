from config.settings import settings
from repository.clone_repo import clone_repository
from repository.file_loader import load_repository_files

print("=" * 50)
print(settings.app_name)
print(f"Version : {settings.app_version}")
print(f"Debug   : {settings.debug}")
print(f"Repo    : {settings.repository_path}")
print("=" * 50)

repo = clone_repository(
    "https://github.com/Anand-Mansabdar/github-codebase-assistant-genai-project.git"
)

files = load_repository_files(repo)

print(f"Indexed {len(files)} files")

for file in files[:10]:
    print(file)