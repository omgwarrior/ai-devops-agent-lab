from fastapi import FastAPI
from app.agent import agent

app = FastAPI(
    title="AI DevOps Agent Lab",
    description="Python FastAPI AI agent lab for DevOps, AWS, Terraform, Ansible, and Redis/MongoDB.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "project": "AI DevOps Agent Lab",
        "status": "running",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "ai-devops-agent-lab",
    }


@app.get("/ask")
def ask(question: str):
    return {
        "question": question,
        "response": agent(question),
    }
