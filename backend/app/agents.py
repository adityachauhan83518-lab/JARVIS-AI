from dataclasses import dataclass

@dataclass
class AgentPlan:
    agent: str
    task: str

def route_message(message: str) -> AgentPlan:
    text = message.lower()
    if any(word in text for word in ("code", "python", "debug", "website", "app")):
        return AgentPlan("coding", message)
    if any(word in text for word in ("search", "browse", "url")):
        return AgentPlan("browser", message)
    return AgentPlan("general", message)
