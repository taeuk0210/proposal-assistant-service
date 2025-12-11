from openai import OpenAI

from app.cores.config import settings

client = OpenAI(api_key="EMPTY", base_url=settings.VLLM_BASE_URL)


def send_message(content: str) -> str:
    response = client.completions.create(
        prompt=content,
        model="openai-community/gpt2",
        stream=None,
        max_tokens=256,
    )
    return response.choices[0].text
