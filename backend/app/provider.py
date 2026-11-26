import httpx
from .config import AI_BASE_URL, AI_API_KEY, AI_MODEL

async def complete_chat(messages: list[dict]) -> str:
    if not (AI_BASE_URL and AI_API_KEY and AI_MODEL):
        return ("JARVIS backend is running, but no AI provider is configured yet. "
                "Set AI_BASE_URL, AI_API_KEY, and AI_MODEL in backend/.env.")
    url = f"{AI_BASE_URL}/chat/completions"
    headers = {"Authorization": f"Bearer {AI_API_KEY}", "Content-Type": "application/json"}
    payload = {"model": AI_MODEL, "messages": messages, "temperature": 0.4}
    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
    return data["choices"][0]["message"]["content"]
