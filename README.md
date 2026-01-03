# 🧠 Multi-Agent AI Orchestrator

## 📌 Project Purpose and Functionality

This project implements a **multi-agent AI system** capable of solving complex, multi-step tasks by orchestrating multiple specialized AI agents.

Instead of relying on a single LLM call, the system coordinates multiple agents—each with a defined role—using a shared state and a controlled workflow. The agents collaborate to plan, research, analyze, and generate a final response. The system is designed to be **robust, modular, and observable**, with support for tool usage, error handling, and real-time frontend interaction.

The application is built as a **full-stack system** with:
- A FastAPI backend for agent orchestration
- A React frontend for user interaction and visualization
- PostgreSQL for logging agent runs and actions
- Redis and Celery for asynchronous and long-running task execution (architecture-ready)

---

## 🏗️ System Architecture

### 🔹 Architecture Diagram

┌────────────────────┐
│ React Frontend │
│ (User Interface) │
└─────────┬──────────┘
│ REST / WebSocket
▼
┌────────────────────┐
│ FastAPI Backend │
│ (API + Orchestrator)│
└─────────┬──────────┘
│
▼
┌────────────────────┐
│ LangGraph Workflow │
│ (Agent State Graph)│
└─────────┬──────────┘
│
▼
┌──────────────────────────────────────────┐
│ Planner → Researcher → Analyst → Writer │
│ (Specialized AI Agents) │
└─────────┬──────────┬──────────┬──────────┘
│ │ │
▼ ▼ ▼
Custom Tools Custom Tools LLM
(Web Search, (Calculator, (Text
Weather API) Analysis) Generation)

markdown
Copy code
      │
      ▼
┌────────────────────┐
│ PostgreSQL DB │
│ (Agent Runs & Logs)│
└────────────────────┘

(Optional / Async Ready)
┌────────────────────┐
│ Redis + Celery │
│ (Task Queue) │
└────────────────────┘

pgsql
Copy code

### 🔹 Architecture Explanation

- **Frontend (React):** Allows users to submit tasks and view results.
- **Backend (FastAPI):** Manages agent orchestration and exposes REST/WebSocket APIs.
- **LangGraph:** Controls agent execution order using a state-machine approach.
- **Agents:** Perform specialized reasoning steps on a shared state.
- **Custom Tools:** Enable agents to interact with external logic or APIs.
- **PostgreSQL:** Stores agent runs, tool calls, and errors for traceability.
- **Redis & Celery:** Enable asynchronous execution for long-running or parallel tasks.

---

## ⚙️ Setup and Running the Application

### 1️⃣ Clone the Repository

git clone https://github.com/your-username/multi-agent-ai-orchestrator.git
cd multi-agent-ai-orchestrator

### 2️⃣ Backend Setup

cd backend
python -m venv venv
source venv/Scripts/activate   # Windows

Install dependencies:

pip install -r requirements.txt

Create environment file backend/.env:

DATABASE_URL=postgresql://postgres:postgres@localhost:5432/multi_agent_ai
OPENAI_API_KEY=your_api_key_here

Run the backend server:

uvicorn app.main:app --reload

Backend will run at:

http://127.0.0.1:8000

### 3️⃣ Frontend Setup

cd frontend

npm install

npm run dev

Frontend will run at:

http://localhost:5173


🧪 Example Tasks and Agent Workflow
🔹 Example Task 1
Task:

Explain how multi-agent systems work

Expected Agent Workflow:

Planner Agent – Breaks the task into logical steps

Researcher Agent – Gathers relevant information using tools

Analyst Agent – Processes and analyzes structured data

Writer Agent – Generates the final response

Result:
A structured output containing:

Task

Plan

Research data

Analysis results

Final answer

🔹 Example Task 2

Task:

Analyze current weather conditions and perform a related calculation


Expected Agent Workflow:

Planner defines subtasks

Researcher calls external weather tool

Analyst performs calculations using the calculator tool

Writer summarizes findings in a clear response