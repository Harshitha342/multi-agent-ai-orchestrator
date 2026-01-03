from pydantic import BaseModel

class CalculatorInput(BaseModel):
    expression: str

def calculator_tool(input: CalculatorInput) -> dict:
    try:
        result = eval(input.expression)
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}
