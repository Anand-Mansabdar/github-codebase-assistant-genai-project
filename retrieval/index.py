from retrieval.models import SearchResult
from vector_store.store import ChromaVectorStore


def load_search_documents(
  vector_store: ChromaVectorStore,
) -> list[SearchResult]:

    data = vector_store.get_all()
    documents = data.get("documents", [])
    metadatas = data.get("metadatas", [])
    results = []

    for document,metadata in zip(
      documents,
      metadatas,
    ):
      results.append(
        SearchResult(
          content=document,
          source_file=metadata["source_file"],
          language=metadata["language"],
          start_line=int(metadata["start_line"]),
          end_line=int(metadata["end_line"]),
          class_name=metadata.get("class_name") or None,
          function_name=metadata.get("function_name") or None,
          distance=0.0,
        )
      )

    return results