def route_request(text: str) -> str:
    text = text.lower()

    if "agent status" in text or "system status" in text:
        return "agent_status"

    if "github workflow status" in text or "github actions status" in text or "ci status" in text:
        return "github_workflow_status"
    
    if "aws health" in text or "check aws health" in text:
        return "aws_health"

    if "what tools" in text or "list tools" in text or "available tools" in text:
        return "list_tools"

    if "terraform" in text and "eks" in text:
        return "terraform_eks"

    if "terraform" in text and "ec2" in text:
        return "terraform_ec2"

    if "terraform" in text and "vpc" in text:
        return "terraform_vpc"

    if "terraform" in text and "s3" in text:
        return "terraform_s3"

    if "who am i in aws" in text or "aws identity" in text:
        return "aws_identity"

    if "aws environment" in text or "cloud inventory" in text:
        return "cloud_inventory"

    if "ec2" in text or "instances" in text:
        return "ec2_instances"

    if "eks" in text or "kubernetes cluster" in text:
        return "eks_clusters"

    if "nba" in text or "playoff" in text or "finals" in text:
        return "nba"

    if "my name is" in text:
        return "save_name"

    if "what is my name" in text:
        return "get_name"

    if "ansible inventory" in text or "inventory skeleton" in text:
        return "ansible_inventory"

    if "ansible" in text and ("nginx" in text or "playbook" in text):
        return "ansible_playbook"

    if "run github workflow" in text or "trigger github actions" in text or "run ci" in text:
        return "github_workflow"

    if "aws" in text or "terraform" in text or "ansible" in text or "devops" in text:
        return "devops"
    
    return "default"
