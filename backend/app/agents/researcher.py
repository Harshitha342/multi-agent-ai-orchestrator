from app.config import llm
from app.orchestration.graph import AgentState
from app.tools.web_search import web_search_tool, WebSearchInput

def researcher_agent(state: AgentState) -> AgentState:
    query = state["task"]

    tool_result = web_search_tool(
        WebSearchInput(query=query)
    )

    state["research"] = tool_result
    return state
