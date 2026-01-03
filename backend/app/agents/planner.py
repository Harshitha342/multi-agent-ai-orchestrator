from app.config import llm
from app.orchestration.graph import AgentState

def planner_agent(state: AgentState) -> AgentState:
    prompt = f"""
    You are a planner agent.
    Break the following task into clear steps:

    Task: {state['task']}
    """

    try:
        response = llm.invoke(prompt)
        state["plan"] = response.content.split("\n")
    except Exception as e:
        state["plan"] = [
            "Understand the task",
            "Research relevant information",
            "Analyze the data",
            "Write the final answer"
        ]
        state["analysis"] = {
            "llm_error": str(e)
        }

    return state
