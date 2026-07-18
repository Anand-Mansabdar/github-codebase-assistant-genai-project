# Every file should have information attached.
# {
#     "path": ".../auth/login.py",
#     "language": "python",
#     "extension": ".py",
#     "size": 2418
# }

from dataclasses import dataclass
from pathlib import Path

@dataclass
class FileMetadata:
  absolute_path: Path
  relative_path: Path
  filename: str
  extension: str
  size: int
  language: str
  

LANGUAGE_MAP = {
    ".py": "Python",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".tsx": "TypeScript React",
    ".jsx": "JavaScript React",
    ".java": "Java",
    ".cpp": "C++",
    ".cc": "C++",
    ".cxx": "C++",
    ".c": "C",
    ".h": "C Header",
    ".hpp": "C++ Header",
    ".cs": "C#",
    ".go": "Go",
    ".rs": "Rust",
    ".php": "PHP",
    ".rb": "Ruby",
    ".swift": "Swift",
    ".kt": "Kotlin",
    ".scala": "Scala",
    ".sql": "SQL",
    ".html": "HTML",
    ".css": "CSS",
    ".scss": "SCSS",
    ".json": "JSON",
    ".yaml": "YAML",
    ".yml": "YAML",
    ".xml": "XML",
    ".toml": "TOML",
    ".ini": "INI",
    ".cfg": "Config",
    ".env": "Environment",
    ".md": "Markdown",
    ".txt": "Text",
    ".sh": "Shell",
    ".bat": "Batch",
    ".dockerfile": "Dockerfile",
}
  
def detect_language(extension: str) -> str:
  """
    Returns the programming language corresponding
    to a file extension.

    Unknown extensions return 'Unknown'.
  """
  
  return LANGUAGE_MAP.get(extension.lower(), "Unknown")