from app.orchestration.graph import AgentState

def researcher_agent(state: AgentState) -> AgentState:
    state["research"] = {
        "summary": "Relevant information gathered for the task"
    }
    return state
