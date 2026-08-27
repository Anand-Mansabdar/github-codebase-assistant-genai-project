from retrieval.models import SearchResult

def display_results(
  query: str,
  results: list[SearchResult],
) -> None:
  print("=" * 80)
  print(f"QUERY: {query}")
  print("=" * 80)

  if not results:
    print("No results found.")
    return

  for index, result in enumerate(results, start=1):
    print(f"\nRESULT #{index}")
    print("-" * 80)

    print(f"File: {result.source_file}")
    print(
      f"Lines: "
      f"{result.start_line}-{result.end_line}"
    )

    print(f"Language: {result.language}")

    if result.class_name:
      print(f"Class: {result.class_name}")

    if result.function_name:
      print(f"Function: {result.function_name}")

    print(f"Distance: {result.distance}")
    
    print(
      f"Relevance: {result.relevance_score:.3f}"
    )

    print("\nCode:")
    print(result.content[:1000])