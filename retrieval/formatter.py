from retrieval.models import SearchResult

def format_context(
  results: list[SearchResult]
) -> str:
  sections = []
  
  for index, result in enumerate(results, start=1):
    section = f"""
      --- Code Context {index} ---
      File: {result.source_file}
      Language: {result.language}
      Lines: {result.start_line}-{result.end_line}
    """
    
    if result.class_name:
      section += f"Class: {result.class_name}\n"
      
    if result.function_name:
      section += f"Function: {result.function_name}\n"
    
    section += f"""
    Code: 
    {result.content}
    """
    
    sections.append(section.strip())
  return "\n\n".join(sections)