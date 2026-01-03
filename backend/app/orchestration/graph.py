from typing import TypedDict, List, Dict, Any

class AgentState(TypedDict):
    task: str
    plan: List[str]
    research: Dict[str, Any]
    analysis: Dict[str, Any]
    final_answer: str

from langgraph.graph import StateGraph
from app.agents.planner import planner_agent
from app.agents.researcher import researcher_agent
from app.agents.analyst import analyst_agent
from app.agents.writer import writer_agent

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("planner", planner_agent)
    graph.add_node("researcher", researcher_agent)
    graph.add_node("analyst", analyst_agent)
    graph.add_node("writer", writer_agent)

    graph.set_entry_point("planner")

    graph.add_edge("planner", "researcher")
    graph.add_edge("researcher", "analyst")
    graph.add_edge("analyst", "writer")

    graph.set_finish_point("writer")

    return graph.compile()
