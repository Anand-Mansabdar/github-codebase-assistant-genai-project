# This module decides:
# Useful?
# ↓
# Yes → Keep
# No → Ignore

from pathlib import Path
from repository.metadata import LANGUAGE_MAP

SUPPORTED_EXTENSIONS = set(LANGUAGE_MAP.keys())

# SUPPORTED_EXTENSIONS = {
#     ".py",
#     ".js",
#     ".ts",
#     ".tsx",
#     ".jsx",
#     ".java",
#     ".cpp",
#     ".c",
#     ".cc",
#     ".cxx",
#     ".h",
#     ".hpp",
#     ".cs",
#     ".go",
#     ".rs",
#     ".php",
#     ".rb",
#     ".swift",
#     ".kt",
#     ".scala",
#     ".html",
#     ".css",
#     ".scss",
#     ".json",
#     ".yaml",
#     ".yml",
#     ".xml",
#     ".toml",
#     ".ini",
#     ".cfg",
#     ".env",
#     ".md",
#     ".txt",
#     ".sh",
#     ".bat",
# }

IGNORED_DIRECTORIES = {
    ".git",
    ".github",
    ".idea",
    ".vscode",
    "__pycache__",
    "node_modules",
    "venv",
    ".venv",
    "env",
    "build",
    "dist",
    ".cache",
    ".pytest_cache",
    ".mypy_cache",
}

def should_index(path: Path) -> bool:
  """
    Returns True if a file should be indexed.

    Rules:
    1. Ignore hidden/system directories.
    2. Ignore unsupported file extensions.
  """
  if any(part in IGNORED_DIRECTORIES for part in path.parts):
    return False
  
  if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
    return False
  
  return True