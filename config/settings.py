from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
  """
    Centralized application configuration.

    Values are loaded from the .env file.
    If a variable is missing, the default value defined here is used.
  """
  
  # App Configuration
  app_name: str = "AI Codebase Assistant - GitHub"
  app_version: str = "1.0"
  debug: bool = False
  
  # API Keys Configuration - comes from .env
  groq_api_key: SecretStr | None = None
  github_token: SecretStr | None = None
  mistral_api_key: SecretStr | None = None
  gemini_api_key: SecretStr | None = None
  
  # Path configuration
  repository_path: str = "data/repositories"
  vector_db_path: str = "data/chroma"
  
  EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"


  # To tell Pydantic where .env is
  model_config = SettingsConfigDict(
    env_file=".env",
    env_file_encoding="utf-8" 
  )


# creating a global object for settings
settings = Settings()