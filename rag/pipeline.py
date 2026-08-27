from retrieval.retriever import CodeRetriever
from retrieval.formatter import format_context
from llm.generator import CodebaseAnswerGenerator
from retrieval.context_builder import MultiFileContextBuilder
from retrieval.hybrid import HybridRetriever

class CodebaseRAG:
  def __init__(
    self,
    retriever: HybridRetriever,
    generator: CodebaseAnswerGenerator,
    context_builder: MultiFileContextBuilder
  ):
    self.retriever = retriever
    self.generator =generator
    self.context_builder=context_builder
    
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
    
    context = self.context_builder.build(results=results)
    
    if not context:
      return "I couldn't find enough relevant repository content to answer this question."
    
    return self.generator.generate(
      question=question,
      context=context
    )
    