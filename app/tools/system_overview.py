from app.tools.agent_status import agent_status_tool
from app.tools.aws_tools import (
    aws_health_tool,
    cloudwatch_alarms_tool,
    cloudwatch_metrics_tool,
    s3_buckets_tool,
)
from app.tools.github_tools import github_workflow_status_tool


def system_overview_tool():
    return {
        "tool": "system_overview_tool",
        "agent": agent_status_tool(),
        "aws": aws_health_tool(),
        "cloudwatch": {
            "alarms": cloudwatch_alarms_tool(),
            "metrics": cloudwatch_metrics_tool(),
        },
        "s3": s3_buckets_tool(),
        "github_actions": github_workflow_status_tool(),
        "summary": {
            "agent_status": "healthy",
            "aws_status": "checked",
            "cloudwatch_status": "checked",
            "s3_status": "checked",
            "github_actions": "checked",
            "purpose": "Single operational overview for the AI DevOps Agent Lab",
        },
    }
