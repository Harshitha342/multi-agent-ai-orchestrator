from sqlalchemy import Column, Integer, String, Text, DateTime, JSON, ForeignKey
from datetime import datetime
from app.database import Base

class AgentRun(Base):
    __tablename__ = "agent_runs"

    id = Column(Integer, primary_key=True)
    task = Column(Text, nullable=False)
    status = Column(String, default="running")
    created_at = Column(DateTime, default=datetime.utcnow)


class AgentLog(Base):
    __tablename__ = "agent_logs"

    id = Column(Integer, primary_key=True)
    run_id = Column(Integer, ForeignKey("agent_runs.id"))
    agent_name = Column(String)
    message = Column(Text)
    tool_name = Column(String)
    tool_input = Column(JSON)
    tool_output = Column(JSON)
    error = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
