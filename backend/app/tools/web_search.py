from pydantic import BaseModel

class WebSearchInput(BaseModel):
    query: str

def web_search_tool(input: WebSearchInput) -> dict:
    try:
        return {
            "results": f"Search results for '{input.query}'"
        }
    except Exception as e:
        return {"error": str(e)}
