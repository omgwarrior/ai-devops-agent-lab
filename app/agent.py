from datetime import datetime
from app.memory.redis_memory import save_memory, get_memory
from app.tools.aws_tools import aws_identity_tool, eks_clusters_tool, cloud_inventory_tool
from app.tools.ansible_tools import ansible_nginx_playbook_tool, ansible_inventory_skeleton_tool
from app.tools.terraform_tools import terraform_s3_tool

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
    text = user_input.lower()

    if "my name is" in text:
        name = user_input.split("is", 1)[1].strip()
        save_memory("user:name", name)
        return {
            "tool": "redis_memory_tool",
            "action": "save",
            "key": "user:name",
            "value": name,
            "message": f"Nice to meet you, {name}. I saved your name in Redis memory.",
        }

    
    if "what is my name" in text:
        name = get_memory("user:name")
        return {
            "tool": "redis_memory_tool",
            "action": "get",
            "key": "user:name",
            "value": name,
            "message": f"Your name is {name}." if name else "I do not have your name saved yet.",
        }

    if "nba" in text or "playoff" in text or "finals" in text:
        return nba_playoffs_tool()

    if "who am i in aws" in text or "aws identity" in text:
        return aws_identity_tool()
    if "eks" in text or "kubernetes cluster" in text:
        return eks_clusters_tool()

    if "who am i in aws" in text or "aws identity" in text:
        return aws_identity_tool()

    if "terraform" in text and "s3" in text:
        return terraform_s3_tool()
    
    if "aws" in text or "terraform" in text or "ansible" in text or "devops" in text:
        return devops_tool()
    
    if "ec2" in text or "instances" in text:
        return ec2_instances_tool()
    
    if "ansible inventory" in text or "inventory skeleton" in text:
        return ansible_inventory_skeleton_tool()

    if "ansible" in text and ("nginx" in text or "playbook" in text):
        return ansible_nginx_playbook_tool()
       
    if "aws environment" in text or "cloud inventory" in text:
        return cloud_inventory_tool()
    
    
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
