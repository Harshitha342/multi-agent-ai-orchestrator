from app.orchestration.graph import AgentState

def planner_agent(state: AgentState) -> AgentState:
    task = state["task"]

    state["plan"] = [
        "Understand the task",
        "Research relevant information",
        "Analyze gathered data",
        "Write a final response"
    ]

    return state
