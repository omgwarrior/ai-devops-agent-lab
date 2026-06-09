from app.tools.tool_registry import TOOLS


def agent_status_tool():
    return {
        "tool": "agent_status_tool",
        "agent": "healthy",
        "version": "0.3.0",
        "memory": "redis",
        "tools_registered": len(TOOLS),
        "architecture": [
            "FastAPI",
            "Router",
            "Tool Registry",
            "Redis Memory",
            "AWS Tools",
            "Terraform Generators",
            "Ansible Generators",
            "GitHub Actions Tool",
            "Docker",
            "Docker Compose",
        ],
    }
