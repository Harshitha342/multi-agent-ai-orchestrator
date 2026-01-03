from sqlalchemy.orm import Session
from app.models.logs import AgentRun, AgentLog

def create_agent_run(db: Session, task: str) -> AgentRun:
    run = AgentRun(task=task)
    db.add(run)
    db.commit()
    db.refresh(run)
    return run


def log_agent_step(
    db: Session,
    run_id: int,
    agent_name: str,
    message: str = None,
    tool_name: str = None,
    tool_input: dict = None,
    tool_output: dict = None,
    error: str = None
):
    log = AgentLog(
        run_id=run_id,
        agent_name=agent_name,
        message=message,
        tool_name=tool_name,
        tool_input=tool_input,
        tool_output=tool_output,
        error=error
    )
    db.add(log)
    db.commit()
