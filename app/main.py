from fastapi import FastAPI
from app.agent import agent

app = FastAPI()

@app.get("/")
def root():
    return {"project": "AI DevOps Agent Lab"}

@app.get("/ask")
def ask(question: str):
    return {"response": agent(question)}