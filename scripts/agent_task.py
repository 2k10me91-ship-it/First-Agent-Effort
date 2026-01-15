import json
import os
import sys
from datetime import datetime

def build_mock(prompt: str) -> dict:
    return {
        "prompt": prompt,
        "mode": "mock",
        "plan": [
            "Read the prompt and identify the smallest change that moves things forward.",
            "List files likely involved and the commands to validate.",
            "Apply the change and run tests.",
        ],
        "files_to_edit": [
            {"path": "src/app.py", "change": "Example change placeholder (no-op)."},
        ],
        "commands_to_run": ["py -m pytest -q"],
        "commit_message": f"Mock agent task: {prompt[:50]}",
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }

def build_live_placeholder(prompt: str) -> dict:
    return {
        "prompt": prompt,
        "mode": "live",
        "plan": [
            "Live mode requested, but OpenAI API calls are not enabled in this project yet.",
            "Enable billing/quota and add real OpenAI call later.",
        ],
        "files_to_edit": [],
        "commands_to_run": ["py -m pytest -q"],
        "commit_message": f"Agent task (live placeholder): {prompt[:50]}",
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }

def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python scripts/agent_task.py \"your prompt here\"")
        return 2

    prompt = " ".join(sys.argv[1:]).strip()
    mock = os.getenv("MOCK_OPENAI") == "1"

    data = build_mock(prompt) if mock else build_live_placeholder(prompt)

    print("AGENT_TASK_RESULT")
    print(json.dumps(data, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
