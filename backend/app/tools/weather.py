from pydantic import BaseModel

class WeatherInput(BaseModel):
    city: str

def weather_tool(input: WeatherInput) -> dict:
    try:
        return {
            "city": input.city,
            "temperature": "32°C",
            "condition": "Sunny"
        }
    except Exception as e:
        return {"error": str(e)}
