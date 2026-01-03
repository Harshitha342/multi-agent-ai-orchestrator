from fastapi import FastAPI
from app.orchestration.graph import build_graph
from fastapi import WebSocket, Depends
from app.websocket import ConnectionManager
from app.database import get_db
from sqlalchemy.orm import Session
from app.models.logger import create_agent_run, log_agent_step
from fastapi import BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Multi-Agent AI Orchestrator")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


graph = build_graph()

@app.get("/run")
def run_agents(db: Session = Depends(get_db)):
    task = "Explain how multi-agent systems work"

    run = create_agent_run(db, task)

    log_agent_step(db, run.id, "system", "Agent run started")

    initial_state = {
        "task": task,
        "plan": [],
        "research": {},
        "analysis": {},
        "final_answer": ""
    }

    result = graph.invoke(initial_state)

    log_agent_step(db, run.id, "writer", "Final answer generated")

    return result

manager = ConnectionManager()
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except:
        manager.disconnect(websocket)


