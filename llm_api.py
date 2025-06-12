import os
from dotenv import load_dotenv
import anthropic

load_dotenv()

API_KEY = os.getenv("ANTHROPIC_API_KEY")

if API_KEY is None:
    raise ValueError("ANTHROPIC_API_KEY not found in .env file.")

client = anthropic.Anthropic(api_key=API_KEY)

def call_anthropic(prompt: str, model: str = "claude-3-haiku-20240307", max_tokens: int = 256) -> str:
    """
    Calls Anthropic LLM with the given prompt and returns the response.
    """
    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text
