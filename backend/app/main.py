from fastapi import FastAPI

app = FastAPI(title="Multi-Agent AI Orchestrator")

@app.get("/")
def root():
    return {
        "message": "Backend is running successfully 🚀"
    }
