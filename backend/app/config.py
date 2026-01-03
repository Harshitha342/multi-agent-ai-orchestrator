from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3
)
