from llm.client import GroqClient
from llm.prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE

class CodebaseAnswerGenerator:
  def __init__(self, llm_client: GroqClient):
    self.llm_client = llm_client
    
  def generate(
    self,
    question: str,
    context: str
  ) -> str:
    user_prompt = USER_PROMPT_TEMPLATE.format(
      context=context,
      question=question
    )
    
    return self.llm_client.generate(
      system_prompt=SYSTEM_PROMPT,
      user_prompt=user_prompt,
    )