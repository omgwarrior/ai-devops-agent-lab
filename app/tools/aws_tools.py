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


def cloudwatch_alarms_tool(region: str = "us-west-2"):
    alarms = run_aws_command([
        "aws",
        "cloudwatch",
        "describe-alarms",
        "--region",
        region,
    ])

    alarm_count = 0
    alarm_states = {
        "OK": 0,
        "ALARM": 0,
        "INSUFFICIENT_DATA": 0,
    }

    if isinstance(alarms, dict):
        metric_alarms = alarms.get("MetricAlarms", [])
        alarm_count = len(metric_alarms)

        for alarm in metric_alarms:
            state = alarm.get("StateValue", "UNKNOWN")
            if state in alarm_states:
                alarm_states[state] += 1

    return {
        "tool": "cloudwatch_alarms_tool",
        "region": region,
        "alarm_count": alarm_count,
        "alarm_states": alarm_states,
        "alarms": alarms,
    }


def cloudwatch_metrics_tool(region: str = "us-west-2"):
    metrics = run_aws_command([
        "aws",
        "cloudwatch",
        "list-metrics",
        "--region",
        region,
        "--max-items",
        "20",
    ])

    metric_count = 0
    namespaces = []

    if isinstance(metrics, dict):
        metric_list = metrics.get("Metrics", [])
        metric_count = len(metric_list)
        namespaces = sorted(list(set(
            metric.get("Namespace", "UNKNOWN")
            for metric in metric_list
        )))

    return {
        "tool": "cloudwatch_metrics_tool",
        "region": region,
        "metric_count_returned": metric_count,
        "namespaces": namespaces,
        "metrics": metrics,
    }


def s3_buckets_tool():
    buckets = run_aws_command([
        "aws",
        "s3api",
        "list-buckets",
    ])

    bucket_count = 0
    bucket_names = []

    if isinstance(buckets, dict):
        bucket_list = buckets.get("Buckets", [])
        bucket_count = len(bucket_list)
        bucket_names = [
            bucket.get("Name")
            for bucket in bucket_list
        ]

    return {
        "tool": "s3_buckets_tool",
        "bucket_count": bucket_count,
        "bucket_names": bucket_names,
        "buckets": buckets,
    }
