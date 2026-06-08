from datetime import datetime

from app.memory.redis_memory import save_memory, get_memory
from app.tools.router import route_request
from app.tools.tool_registry import run_tool


def nba_playoffs_tool():
    return {
        "tool": "nba_playoffs_tool",
        "topic": "NBA Finals",
        "status": "Knicks lead Spurs 2-0",
        "games": [
            {"game": 1, "result": "Knicks 105, Spurs 95"},
            {"game": 2, "result": "Knicks 105, Spurs 104"},
            {"game": 3, "schedule": "Spurs @ Knicks, June 8, 2026"},
            {"game": 4, "schedule": "Spurs @ Knicks, June 10, 2026"},
        ],
    }


def devops_tool():
    return {
        "tool": "devops_tool",
        "stack": [
            "Python FastAPI",
            "Terraform",
            "Ansible",
            "AWS",
            "Redis",
            "CloudWatch/Grafana",
        ],
        "purpose": "AI DevOps Agent Lab for SRE/DevOps portfolio work",
    }


def agent(user_input: str):
    route = route_request(user_input)

    if route == "save_name":
        name = user_input.split("is", 1)[1].strip()
        save_memory("user:name", name)
        return {
            "tool": "redis_memory_tool",
            "action": "save",
            "key": "user:name",
            "value": name,
            "message": f"Nice to meet you, {name}. I saved your name in Redis memory.",
        }

    if route == "get_name":
        name = get_memory("user:name")
        return {
            "tool": "redis_memory_tool",
            "action": "get",
            "key": "user:name",
            "value": name,
            "message": f"Your name is {name}." if name else "I do not have your name saved yet.",
        }

    if route == "nba":
        return nba_playoffs_tool()

    tool_response = run_tool(route)
    if tool_response:
        return tool_response

    if route == "devops":
        return devops_tool()

    return {
        "tool": "default_agent_response",
        "input": user_input,
        "capabilities": [
            "NBA playoff status",
            "AWS/DevOps lab planning",
            "Terraform/Ansible/Python app ideas",
            "Redis memory",
        ],
        "timestamp": str(datetime.now()),
    }
