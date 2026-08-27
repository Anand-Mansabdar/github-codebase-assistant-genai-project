from dataclasses import dataclass

@dataclass
class SearchResult:
  content: str
  source_file: str
  language: str
  start_line: int
  end_line: int
  class_name: str | None
  function_name: str | None
  distance: float
  
  
  @property
  def relevance_score(self) -> float:
    return 1 / (1 + self.distance)
  