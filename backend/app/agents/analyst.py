from app.orchestration.graph import AgentState
from app.tools.calculator import calculator_tool, CalculatorInput

def analyst_agent(state: AgentState) -> AgentState:
    calculation = calculator_tool(
        CalculatorInput(expression="2 + 2 * 3")
    )

    state["analysis"] = calculation
    return state
