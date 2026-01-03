from app.orchestration.graph import AgentState

def writer_agent(state: AgentState) -> AgentState:
    state["final_answer"] = (
        f"Task: {state['task']}\n\n"
        f"Plan: {state['plan']}\n\n"
        f"Research: {state['research']}\n\n"
        f"Analysis: {state['analysis']}"
    )
    return state
