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