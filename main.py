from config.settings import settings

print("=" * 50)
print(settings.app_name)
print(f"Version : {settings.app_version}")
print(f"Debug   : {settings.debug}")
print(f"Repo    : {settings.repository_path}")
print("=" * 50)