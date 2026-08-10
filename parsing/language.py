from tree_sitter import Language
import tree_sitter_python as tsp

PYTHON_LANGUAGE = Language(tsp.language())

LANGUAGE_MAP = {
  "Python": PYTHON_LANGUAGE
}

def get_language(language: str) -> Language:
  """
    Return the Tree-sitter Language object for the given programming language.
  """
  try:
    return LANGUAGE_MAP[language]
  except KeyError:
    raise ValueError(
      f"Unsupported language: {language}"
    )