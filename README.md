# 🤖 AI DevOps Agent Lab

An operational AI-powered DevOps and Site Reliability Engineering (SRE) platform built with Python, FastAPI, Redis, AWS, Terraform, Ansible, Docker, and GitHub Actions.

The goal of this project is to build a practical AI-driven operations assistant capable of discovering cloud infrastructure, generating automation, monitoring environments, and interacting with CI/CD pipelines.

---

## 🚀 Current Features

### 🧠 AI Agent Core

* FastAPI REST API
* Tool Router
* Tool Registry
* Dynamic Tool Discovery
* Modular Architecture
* JSON Responses

---

### 💾 Redis Memory

Store and retrieve user information.

Examples:

```bash
curl -s "http://127.0.0.1:8001/ask?question=my%20name%20is%20Alvin"
curl -s "http://127.0.0.1:8001/ask?question=what%20is%20my%20name"
```

---

## ☁️ AWS Operations Tools

### AWS Identity

```text
who am i in aws
```

Returns:

* AWS Account
* User ARN
* User ID

---

### EC2 Inventory

```text
show ec2 instances
```

Returns:

* Running Instances
* Instance Metadata

---

### EKS Inventory

```text
show eks clusters
```

Returns:

* Kubernetes Clusters
* Cluster Names

---

### S3 Inventory

```text
show s3 buckets
```

Returns:

* Bucket Count
* Bucket Names

---

### Cloud Inventory

```text
show cloud inventory
```

Returns:

* EC2
* EKS
* AWS Environment Information

---

### AWS Health

```text
check aws health
```

Performs:

* STS Identity Check
* EC2 Inventory Check
* EKS Inventory Check

Returns:

```json
{
  "status": "healthy"
}
```

---

## 📊 CloudWatch Monitoring

### CloudWatch Metrics

```text
show cloudwatch metrics
```

Returns:

* AWS Metrics
* Namespaces
* EC2 Metrics
* EKS Metrics
* EBS Metrics

---

### CloudWatch Alarms

```text
show cloudwatch alarms
```

Returns:

* Alarm Count
* Alarm State Summary
* Alarm Details

---

## 🏗️ Terraform Generators

Generate Infrastructure as Code automatically.

### S3 Generator

```text
create terraform for s3
```

### VPC Generator

```text
create terraform for vpc
```

### EC2 Generator

```text
create terraform for ec2
```

### EKS Generator

```text
create terraform for eks
```

Generated output is valid Terraform HCL.

---

## ⚙️ Ansible Automation

### NGINX Playbook Generator

```text
create ansible playbook for nginx
```

Returns:

* Playbook YAML
* Installation Tasks
* Service Configuration

---

### Inventory Generator

```text
ansible inventory skeleton
```

Returns:

* Inventory Template
* Host Groups

---

## 🔄 GitHub Actions Integration

### Trigger Workflow

```text
run github workflow
```

Executes:

```bash
gh workflow run ci.yml --ref main
```

---

### Workflow Status

```text
github workflow status
```

Returns:

* Latest Workflow
* Status
* Success/Failure
* Duration

---

## 📈 Operational Dashboard

### Agent Status

```text
agent status
```

Returns:

* Agent Health
* Version
* Tool Count
* Architecture Summary

---

### System Overview

```text
system overview
```

Aggregates:

* Agent Status
* AWS Health
* CloudWatch Metrics
* CloudWatch Alarms
* S3 Inventory
* GitHub Actions Status

Provides a single operational view of the platform.

---

## 🐳 Containerization

### Docker

Build:

```bash
docker build -t ai-devops-agent-lab .
```

Run:

```bash
docker run -p 8001:8001 ai-devops-agent-lab
```

---

### Docker Compose

```bash
docker compose up --build
```

Includes:

* FastAPI
* Redis

---

## 🔧 CI/CD

GitHub Actions automatically validates:

* FastAPI Startup
* Health Endpoint
* Redis Connectivity
* Terraform Generator
* Ansible Generator
* Agent Status

Example:

```bash
gh workflow run ci.yml --ref main
gh run watch
```

---

## 🏛️ Real-World SRE Focus Areas

This project was built to simulate modern Platform Engineering and Site Reliability Engineering workflows:

* AWS Operations
* CloudWatch Monitoring
* Infrastructure as Code
* Terraform
* Kubernetes
* GitHub Actions
* CI/CD
* Automation
* Observability
* Operational Dashboards
* Reliability Engineering

---

## 🛣️ Roadmap

### v0.4

* EKS Nodegroup Discovery
* GitHub Workflow History
* Terraform Validation
* CloudWatch Dashboard Inventory

### v0.5

* OpenAI Integration
* Local LLM Integration (Ollama)
* Tool Calling via LLM
* AI Decision Engine

### v1.0

* AI SRE Platform Agent
* Multi-Cloud Support
* Automated Remediation
* Incident Response Workflows
* Operational Runbook Automation

---

## 👨‍💻 Author

Alvin Cly

Site Reliability Engineer | Platform Engineer | DevOps Engineer

AWS • Kubernetes • Terraform • Python • Cloud Engineering • Observability • Automation

---

## ⭐ Project Status

Current Version:

```text
v0.4.0
Operational Platform Agent
```

Status:

```text
Healthy
Actively Developed
Production-Style Architecture
```
