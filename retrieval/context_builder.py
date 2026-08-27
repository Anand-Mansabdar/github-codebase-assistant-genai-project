from collections import defaultdict
from retrieval.models import SearchResult
from config.settings import settings

class MultiFileContextBuilder:
  """
    Builds structured LLM context from retrieved code chunks.

    Chunks are grouped by source file so the LLM can reason
    about relationships between multiple files.
  """

  def __init__(
    self,
  ):
    self.max_files =settings.MAX_CONTENT_FILES
    self.max_chunks_per_file = settings.MAX_CHUNKS_PER_FILE
    self.max_context_chars = settings.MAX_CONTENT_CHARS

  def build(
    self,
    results: list[SearchResult],
  ) -> str:
    if not results:
      return ""

    grouped = self._group_by_file(results)
    sections: list[str] = []
    current_length = 0

    for source_file, file_results in grouped.items():
      file_section = self._format_file(
        source_file,
        file_results
      )

      if current_length + len(file_section) > self.max_context_chars: break

      sections.append(file_section)
      current_length += len(file_section)
    
    return "\n\n".join(sections)

  def _group_by_file(
    self,
    results: list[SearchResult],
  ) -> dict[str, list[SearchResult]]:

    grouped: dict[str, list[SearchResult]] = (defaultdict(list))

    for result in results:
      grouped[result.source_file].append(result)
      
    ranked_files = sorted(
      grouped.items(),
      key=lambda item: max(
        result.score
        for result in item[1]
      ),
      reverse=True,
    )

    return dict(
      ranked_files[:self.max_files]
    )

  def _format_file(
    self,
    source_file: str,
    results: list[SearchResult],
  ) -> str:

    results = sorted(
      results,
      key=lambda result: result.start_line,
    )
    
    results = results[:self.max_chunks_per_file]
    
    parts = [
      f"FILE: {source_file}"
    ]
    
    for result in results:
      metadata: list[str] = []

      if result.language:
        metadata.append(f"Language: {result.language}")

      if result.class_name:
        metadata.append(f"Class: {result.class_name}")

      if result.function_name:
        metadata.append(f"Function: {result.function_name}")

      metadata.append(
        f"Lines: "
        f"{result.start_line}-{result.end_line}"
      )

      parts.append("\n".join(metadata))
      
      language = (
        result.language.lower() if result.language else ""
      )

      parts.append(
        f"```{language}\n"
        f"{result.content}\n"
        f"```"
      )

    return "\n\n".join(parts)