from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from .agents import route_message
from .provider import complete_chat

app = FastAPI(title="JARVIS API", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=False, allow_methods=["GET", "POST"], allow_headers=["*"])

class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=12000)

@app.get("/health")
async def health():
    return {"status": "ok", "service": "jarvis-api"}

@app.post("/api/chat")
async def chat(request: ChatRequest):
    plan = route_message(request.message)
    system = ("You are JARVIS, a helpful personal AI assistant. Be clear and honest. "
              "Do not claim to have executed actions or accessed devices unless a tool confirms it. "
              "Ask before consequential external actions. Specialized agent execution is not enabled yet.")
    reply = await complete_chat([{"role": "system", "content": system}, {"role": "user", "content": request.message}])
    return {"reply": reply, "routed_agent": plan.agent}
