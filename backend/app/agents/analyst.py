from app.orchestration.graph import AgentState

def analyst_agent(state: AgentState) -> AgentState:
    state["analysis"] = {
        "insights": "Key insights derived from research"
    }
    return state
