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


def terraform_ec2_tool():
    return {
        "tool": "terraform_ec2_tool",
        "description": "Generates Terraform HCL for a basic AWS EC2 instance.",
        "terraform": """resource "aws_security_group" "web_sg" {
  name        = "ai-devops-agent-web-sg"
  description = "Allow SSH and HTTP inbound traffic"

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["YOUR_PUBLIC_IP/32"]
  }

  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name    = "ai-devops-agent-web-sg"
    Project = "ai-devops-agent-lab"
  }
}

resource "aws_instance" "web" {
  ami           = "ami-PLACEHOLDER"
  instance_type = "t3.micro"

  vpc_security_group_ids = [
    aws_security_group.web_sg.id
  ]

  tags = {
    Name        = "ai-devops-agent-ec2"
    Environment = "dev"
    Project     = "ai-devops-agent-lab"
  }
}
"""
    }


def terraform_eks_tool():
    return {
        "tool": "terraform_eks_tool",
        "description": "Generates Terraform HCL for a basic AWS EKS cluster using the terraform-aws-modules/eks module.",
        "terraform": """module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 20.0"

  cluster_name    = "ai-devops-agent-eks"
  cluster_version = "1.30"

  vpc_id     = aws_vpc.main.id
  subnet_ids = [
    aws_subnet.public_1.id
  ]

  enable_irsa = true

  eks_managed_node_groups = {
    default = {
      desired_size = 2
      min_size     = 1
      max_size     = 3

      instance_types = ["t3.medium"]
    }
  }

  tags = {
    Environment = "dev"
    Project     = "ai-devops-agent-lab"
  }
}
"""
    }
