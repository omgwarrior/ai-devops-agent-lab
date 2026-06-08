def terraform_s3_tool():
    return {
        "tool": "terraform_s3_tool",
        "description": "Generates Terraform HCL for a basic AWS S3 bucket.",
        "terraform": """resource "aws_s3_bucket" "ai_devops_agent_demo" {
  bucket = "ai-devops-agent-demo-bucket"

  tags = {
    Name        = "ai-devops-agent-demo-bucket"
    Environment = "dev"
    Project     = "ai-devops-agent-lab"
  }
}
"""
    }
