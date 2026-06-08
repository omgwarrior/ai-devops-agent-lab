def terraform_vpc_tool():
    return {
        "tool": "terraform_vpc_tool",
        "description": "Generates Terraform for a simple VPC.",
        "terraform": """
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name = "ai-devops-agent-vpc"
  }
}

resource "aws_subnet" "public_1" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true

  tags = {
    Name = "public-1"
  }
}
"""
    }