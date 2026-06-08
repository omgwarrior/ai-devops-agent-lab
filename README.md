# AI DevOps Agent Lab

## Overview

AI DevOps Agent Lab is a Python/FastAPI-based AI DevOps assistant designed to learn:

- AI Agents
- AWS
- Terraform
- Ansible
- Redis
- Docker
- Platform Engineering
- SRE Practices

## Features

### AWS Tools

- AWS Identity Tool
- AWS EKS Inventory Tool
- AWS EC2 Inventory Tool
- AWS Cloud Inventory Tool

### Terraform Generators

- Terraform S3 Generator
- Terraform VPC Generator
- Terraform EC2 Generator
- Terraform EKS Generator

### Ansible Generators

- Ansible Inventory Generator
- Ansible Nginx Playbook Generator

### Memory

- Redis Memory Support

### API

- FastAPI
- /health endpoint
- /ask endpoint

### Docker

- Dockerized FastAPI Application

## Project Structure

\`\`\`
ai-devops-agent-lab/
├── app/
│   ├── main.py
│   ├── agent.py
│   ├── memory/
│   └── tools/
├── Dockerfile
├── requirements.txt
└── README.md
\`\`\`

## Running Locally

\`\`\`bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

uvicorn app.main:app --reload --port 8001
\`\`\`

## Health Check

\`\`\`bash
curl -s http://127.0.0.1:8001/health | python3 -m json.tool
\`\`\`

## Example Commands

### AWS Identity

\`\`\`
who am i in aws
\`\`\`

### EKS Inventory

\`\`\`
do i have eks clusters
\`\`\`

### Cloud Inventory

\`\`\`
show my aws environment
\`\`\`

### Terraform S3

\`\`\`
create terraform for s3
\`\`\`

### Terraform VPC

\`\`\`
create terraform for vpc
\`\`\`

### Terraform EC2

\`\`\`
create terraform for ec2
\`\`\`

### Terraform EKS

\`\`\`
create terraform for eks
\`\`\`

### Ansible Playbook

\`\`\`
create ansible playbook for nginx
\`\`\`

## Docker

Build:

\`\`\`bash
docker build -t ai-devops-agent-lab .
\`\`\`

Run:

\`\`\`bash
docker run -p 8000:8000 ai-devops-agent-lab
\`\`\`

## Roadmap

Completed:

- FastAPI
- Redis Memory
- AWS Identity Tool
- AWS EKS Tool
- AWS EC2 Tool
- Cloud Inventory Tool
- Terraform S3 Generator
- Terraform VPC Generator
- Terraform EC2 Generator
- Terraform EKS Generator
- Ansible Inventory Generator
- Ansible Playbook Generator
- Docker Support

Next:

- GitHub Actions CI/CD
- Docker Compose
- Redis Container
- OpenAI Integration
- ECS Deployment
- EKS Deployment
- Web UI
- Grafana Observability

## Philosophy

Learn by Building.

Build.
Break.
Fix.
Improve.
Repeat.
