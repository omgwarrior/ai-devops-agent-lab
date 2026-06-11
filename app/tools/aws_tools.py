import subprocess
import json


def run_aws_command(command: list):
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
        )

        return json.loads(result.stdout)

    except subprocess.CalledProcessError as e:
        return {
            "error": "AWS CLI command failed",
            "stderr": e.stderr,
            "stdout": e.stdout,
        }

    except FileNotFoundError:
        return {
            "error": "AWS CLI is not installed or not found in PATH",
        }

    except Exception as e:
        return {
            "error": str(e),
        }


def aws_identity_tool():
    return {
        "tool": "aws_identity_tool",
        "identity": run_aws_command(["aws", "sts", "get-caller-identity"]),
    }


def eks_clusters_tool(region: str = "us-west-2"):
    return {
        "tool": "eks_clusters_tool",
        "region": region,
        "clusters": run_aws_command(["aws", "eks", "list-clusters", "--region", region]),
    }
def ec2_instances_tool(region="us-west-2"):
    return {
        "tool": "ec2_instances_tool",
        "region": region,
        "instances": run_aws_command([
            "aws",
            "ec2",
            "describe-instances",
            "--region",
            region
        ]),
    }
def cloud_inventory_tool(region="us-west-2"):
    return {
        "tool": "cloud_inventory_tool",
        "identity": run_aws_command([
            "aws", "sts", "get-caller-identity"
        ]),
        "eks": run_aws_command([
            "aws", "eks", "list-clusters",
            "--region", region
        ]),
        "ec2": run_aws_command([
            "aws", "ec2", "describe-instances",
            "--region", region
        ]),
        "ecr": run_aws_command([
            "aws", "ecr", "describe-repositories",
            "--region", region
        ]),
    }
def terraform_s3_tool():
    return {
        "tool": "terraform_s3_tool",
        "terraform": """
resource "aws_s3_bucket" "demo" {
  bucket = "ai-devops-agent-demo"
}
"""
    }

def aws_health_tool(region: str = "us-west-2"):
    identity = run_aws_command(["aws", "sts", "get-caller-identity"])
    eks = run_aws_command(["aws", "eks", "list-clusters", "--region", region])
    ec2 = run_aws_command(["aws", "ec2", "describe-instances", "--region", region])

    ec2_count = 0
    if isinstance(ec2, dict) and "Reservations" in ec2:
        for reservation in ec2.get("Reservations", []):
            ec2_count += len(reservation.get("Instances", []))

    eks_count = 0
    if isinstance(eks, dict) and "clusters" in eks:
        eks_count = len(eks.get("clusters", []))

    return {
        "tool": "aws_health_tool",
        "region": region,
        "status": "healthy",
        "identity": identity,
        "summary": {
            "eks_clusters": eks_count,
            "ec2_instances": ec2_count,
        },
        "checks": {
            "sts_identity": "ok" if "Account" in identity else "error",
            "eks_inventory": "ok" if "clusters" in eks else "error",
            "ec2_inventory": "ok" if "Reservations" in ec2 else "error",
        },
    }
