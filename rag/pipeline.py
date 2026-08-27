from retrieval.retriever import CodeRetriever
from retrieval.formatter import format_context
from llm.generator import CodebaseAnswerGenerator

class CodebaseRAG:
  def __init__(
    self,
    retriever: CodeRetriever,
    generator: CodebaseAnswerGenerator,
  ):
    self.retriever = retriever
    self.generator =generator
    
  def answer(
    self,
    question: str,
    n_results: int=5,
  ) -> str:
    results = self.retriever.retrieve(
      query=question,
      n_results=n_results,
      max_results=n_results
    )
    
    if not results:
      return "I couldn't find relevant code in the repository to answer this question."
    
    context = format_context(results=results)
    
    return self.generator.generate(
      question=question,
      context=context
    )
    