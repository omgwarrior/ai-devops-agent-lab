import subprocess
import json

def aws_identity_tool():
    try:
        result = subprocess.run(
            ["aws", "sts", "get-caller-identity"],
            capture_output=True,
            text=True,
            check=True,
        )

        return {
            "tool": "aws_identity_tool",
            "identity": json.loads(result.stdout),
        }

    except subprocess.CalledProcessError as e:
        return {
            "tool": "aws_identity_tool",
            "error": "AWS CLI command failed",
            "stderr": e.stderr,
            "stdout": e.stdout,
        }

    except FileNotFoundError:
        return {
            "tool": "aws_identity_tool",
            "error": "AWS CLI is not installed or not found in PATH",
        }

    except Exception as e:
        return {
            "tool": "aws_identity_tool",
            "error": str(e),
        }