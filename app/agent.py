from datetime import datetime

def nba_playoffs_tool():
    return """
NBA Finals status:
- Knicks lead Spurs 2-0
- Game 1: Knicks 105, Spurs 95
- Game 2: Knicks 105, Spurs 104
- Game 3: Spurs @ Knicks, June 8, 2026
- Game 4: Spurs @ Knicks, June 10, 2026
"""

def devops_tool():
    return """
DevOps lab stack:
- Python FastAPI app
- Terraform for AWS infrastructure
- Ansible for server/config automation
- Redis or MongoDB for agent memory
- CloudWatch/Grafana for observability
"""

def agent(user_input: str):
    text = user_input.lower()

    if "nba" in text or "playoff" in text or "finals" in text:
        return nba_playoffs_tool()

    if "aws" in text or "terraform" in text or "ansible" in text or "devops" in text:
        return devops_tool()

    return f"""
AI DevOps Agent response:
I received: {user_input}

I can currently help with:
- NBA playoff status
- AWS/DevOps lab planning
- Terraform/Ansible/Python app ideas

Timestamp: {datetime.now()}
"""
