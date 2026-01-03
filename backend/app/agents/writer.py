from app.config import llm
from app.orchestration.graph import AgentState

def writer_agent(state: AgentState) -> AgentState:
    prompt = f"""
    Write a clear final answer using:

    Task: {state['task']}
    Plan: {state['plan']}
    Research: {state['research']}
    Analysis: {state['analysis']}
    """

    try:
        response = llm.invoke(prompt)
        state["final_answer"] = response.content
    except Exception as e:
        state["final_answer"] = (
            "LLM could not generate a response due to API limits.\n"
            f"Error: {str(e)}"
        )

    return state
