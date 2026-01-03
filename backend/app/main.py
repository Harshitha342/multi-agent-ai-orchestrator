from fastapi import FastAPI
from app.database import engine
from app.models import logs

app = FastAPI(title="Multi-Agent AI Orchestrator")

logs.Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Backend + PostgreSQL running 🚀"}
