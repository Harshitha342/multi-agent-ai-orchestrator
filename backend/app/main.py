from fastapi import FastAPI
from app.orchestration.graph import build_graph

app = FastAPI(title="Multi-Agent AI Orchestrator")

graph = build_graph()

@app.get("/run")
def run_agents():
    initial_state = {
        "task": "Explain how multi-agent systems work",
        "plan": [],
        "research": {},
        "analysis": {},
        "final_answer": ""
    }

    result = graph.invoke(initial_state)
    return result
