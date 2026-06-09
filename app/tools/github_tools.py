import subprocess


def github_workflow_tool():
    try:
        result = subprocess.run(
            ["gh", "workflow", "run", "ci.yml", "--ref", "main"],
            capture_output=True,
            text=True,
            check=True,
        )

        return {
            "tool": "github_workflow_tool",
            "workflow": "ci.yml",
            "branch": "main",
            "status": "triggered",
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
        }

    except subprocess.CalledProcessError as e:
        return {
            "tool": "github_workflow_tool",
            "status": "failed",
            "error": "GitHub workflow command failed",
            "stdout": e.stdout,
            "stderr": e.stderr,
        }

    except FileNotFoundError:
        return {
            "tool": "github_workflow_tool",
            "status": "failed",
            "error": "GitHub CLI is not installed or not found in PATH",
        }
