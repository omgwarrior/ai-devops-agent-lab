from app.tools.aws_tools import (
    aws_identity_tool,
    eks_clusters_tool,
    ec2_instances_tool,
    cloud_inventory_tool,
    aws_health_tool,
    cloudwatch_alarms_tool,
    cloudwatch_metrics_tool,
    s3_buckets_tool,
)

from app.tools.ansible_tools import (
    ansible_nginx_playbook_tool,
    ansible_inventory_skeleton_tool,
)

from app.tools.terraform_tools import (
    terraform_s3_tool,
    terraform_ec2_tool,
    terraform_eks_tool,
)

from app.tools.terraform_vpc import terraform_vpc_tool
from app.tools.tool_info import list_tools_tool
from app.tools.github_tools import github_workflow_tool, github_workflow_status_tool
from app.tools.agent_status import agent_status_tool
from app.tools.system_overview import system_overview_tool

TOOLS = {
    "aws_identity": aws_identity_tool,
    "eks_clusters": eks_clusters_tool,
    "ec2_instances": ec2_instances_tool,
    "cloud_inventory": cloud_inventory_tool,

    "ansible_playbook": ansible_nginx_playbook_tool,
    "ansible_inventory": ansible_inventory_skeleton_tool,

    "terraform_s3": terraform_s3_tool,
    "terraform_vpc": terraform_vpc_tool,
    "terraform_ec2": terraform_ec2_tool,
    "terraform_eks": terraform_eks_tool,

    "list_tools": list_tools_tool,

    "github_workflow": github_workflow_tool,

    "agent_status": agent_status_tool,
    "github_workflow_status": github_workflow_status_tool,

    "aws_health": aws_health_tool,
    "system_overview": system_overview_tool,
    "cloudwatch_alarms": cloudwatch_alarms_tool,
    "cloudwatch_metrics": cloudwatch_metrics_tool,

    "s3_buckets": s3_buckets_tool,
}

def run_tool(route: str):
    tool = TOOLS.get(route)

    if not tool:
        return None

    return tool()
