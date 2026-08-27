from groq import Groq
from config.settings import settings

class GroqClient:
  def __init__(self):
    self.client = Groq(
      api_key=settings.GROQ_API_KEY
    )
  
  def generate(
    self, 
    system_prompt: str,
    user_prompt: str,
  ) -> str:
    response = self.client.chat.completions.create(
      model=settings.GROQ_MODEL,
      messages=[
        {
          "role": "system",
          "content": system_prompt
        },
        {
          "role": "user",
          "content": user_prompt
        }
      ],
      temperature=0.1
    )
  
    return response.choices[0].message.content