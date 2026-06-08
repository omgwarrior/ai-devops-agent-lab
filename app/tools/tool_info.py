def list_tools_tool():
    return {
        "tool": "list_tools_tool",
        "available_tools": [
            "redis_memory",
            "aws_identity",
            "eks_clusters",
            "ec2_instances",
            "cloud_inventory",
            "terraform_s3",
            "terraform_vpc",
            "terraform_ec2",
            "terraform_eks",
            "ansible_inventory",
            "ansible_playbook",
            "nba_playoffs",
        ],
        "message": "These are the current tools available in the AI DevOps Agent Lab.",
    }
