# AI DevOps Agent Lab

## Overview

AI DevOps Agent Lab is a Python-based AI Agent platform designed to demonstrate modern DevOps, SRE, Platform Engineering, Cloud Engineering, Infrastructure as Code (IaC), and AI Agent concepts.

The project combines FastAPI, Redis memory, AWS integrations, Terraform generation, Ansible automation, Docker, Docker Compose, GitHub Actions CI/CD, and an extensible Agent architecture using a Router and Tool Registry pattern.

The goal is to simulate how modern AI Agents interact with cloud platforms, infrastructure automation, and operational tooling.

---

## Architecture

```text
User
  ↓
FastAPI API
  ↓
Agent
  ↓
Router
  ↓
Tool Registry
  ↓
┌─────────────────────────────┐
│ Redis Memory                │
│ AWS Identity Tool           │
│ AWS EC2 Inventory Tool      │
│ AWS EKS Inventory Tool      │
│ Cloud Inventory Tool        │
│ Terraform Generators        │
│ Ansible Generators          │
│ NBA Stats Tool              │
│ Tool Discovery              │
└─────────────────────────────┘
```

---

## Technology Stack

### Languages

* Python 3.12

### Frameworks

* FastAPI
* Uvicorn

### Memory Layer

* Redis

### Cloud

* AWS CLI
* IAM
* EC2
* EKS
* STS

### Infrastructure as Code

* Terraform

### Configuration Management

* Ansible

### Containerization

* Docker
* Docker Compose

### CI/CD

* GitHub Actions
* GitHub CLI

---

## Current Features

### Memory

* Save user information into Redis
* Retrieve stored user information
* Persistent memory between requests

Example:

```text
my name is Alvin
```

```text
what is my name
```

---

### AWS Identity Tool

Retrieve current AWS identity:

```text
who am i in aws
```

Returns:

* AWS Account ID
* IAM User
* AWS ARN

---

### AWS EKS Inventory Tool

Retrieve Kubernetes cluster inventory:

```text
show eks clusters
```

Returns:

* Cluster Names
* AWS Region

---

### AWS EC2 Inventory Tool

Retrieve EC2 inventory:

```text
show ec2 instances
```

Returns:

* Instance IDs
* Instance State
* Instance Type

---

### Cloud Inventory Tool

Retrieve AWS environment information:

```text
show cloud inventory
```

Returns:

* EKS Clusters
* EC2 Instances
* AWS Identity

---

## Terraform Generators

### S3 Generator

```text
create terraform for s3
```

Generates Terraform HCL for:

* AWS S3 Bucket

### VPC Generator

```text
create terraform for vpc
```

Generates Terraform HCL for:

* VPC
* Public Subnet

### EC2 Generator

```text
create terraform for ec2
```

Generates Terraform HCL for:

* EC2 Instance
* Security Groups

### EKS Generator

```text
create terraform for eks
```

Generates Terraform HCL for:

* EKS Cluster
* Managed Node Groups
* IRSA
* VPC Integration

---

## Ansible Generators

### Inventory Skeleton Generator

```text
create ansible inventory
```

Generates:

```text
inventory/
group_vars/
host_vars/
playbooks/
roles/
```

### NGINX Playbook Generator

```text
create ansible playbook for nginx
```

Generates:

* NGINX Installation
* Service Startup
* Service Enablement

---

## Tool Discovery

The agent can list available tools.

Example:

```text
what tools do you have
```

Returns:

* Redis Memory
* AWS Identity
* EKS Inventory
* EC2 Inventory
* Cloud Inventory
* Terraform Generators
* Ansible Generators
* NBA Tool

---

## Agent Routing

The platform uses a Router pattern to determine user intent.

Example:

```text
create terraform for eks
```

Router:

```text
terraform_eks
```

Tool Registry:

```text
terraform_eks_tool()
```

Response:

```text
Terraform HCL
```

---

## Tool Registry

The Tool Registry provides dynamic tool dispatching.

Benefits:

* Centralized tool management
* Easier extensibility
* Cleaner architecture
* Similar design patterns used by modern AI Agent frameworks

---

## Docker

Build:

```bash
docker build -t ai-devops-agent .
```

Run:

```bash
docker run -p 8000:8000 ai-devops-agent
```

---

## Docker Compose

Start:

```bash
docker compose up --build
```

Components:

* FastAPI
* Redis

---

## GitHub Actions CI/CD

Pipeline validates:

* Dependency installation
* Redis availability
* FastAPI startup
* Health endpoint
* Terraform generation
* Ansible generation
* Redis memory functionality

Manual execution:

```bash
gh workflow run ci.yml --ref main
```

Watch workflow:

```bash
gh run watch
```

---

## API Examples

Health Check:

```bash
curl http://127.0.0.1:8001/health
```

Tool Discovery:

```bash
curl "http://127.0.0.1:8001/ask?question=what%20tools%20do%20you%20have"
```

AWS Identity:

```bash
curl "http://127.0.0.1:8001/ask?question=who%20am%20i%20in%20aws"
```

Terraform EKS:

```bash
curl "http://127.0.0.1:8001/ask?question=create%20terraform%20for%20eks"
```

Ansible Playbook:

```bash
curl "http://127.0.0.1:8001/ask?question=create%20ansible%20playbook%20for%20nginx"
```

---

## Roadmap

### v0.3

* GitHub Actions Tool
* Workflow Execution Tool
* Tool Metadata Registry
* Enhanced Cloud Inventory

### v0.4

* OpenAI Integration
* Anthropic Integration
* Local LLM Support (Ollama)

### v0.5

* Autonomous Tool Selection
* Multi-step Agent Workflows
* Infrastructure Deployment Automation

---

## Author

Alvin Cly

AI DevOps Agent Lab is a personal portfolio project demonstrating AI Agent Engineering, Platform Engineering, DevOps, SRE, Cloud Engineering, Infrastructure Automation, and Operational Excellence concepts.
