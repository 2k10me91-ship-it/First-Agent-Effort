import json
import os
import subprocess
import sys

def test_agent_task_mock_outputs_json():
    env = os.environ.copy()
    env["MOCK_OPENAI"] = "1"

    result = subprocess.run(
        [sys.executable, "scripts/agent_task.py", "fix my bug"],
        capture_output=True,
        text=True,
        env=env,
        check=True,
    )

    out = result.stdout.strip().splitlines()
    assert out[0].strip() == "AGENT_TASK_RESULT"

    payload = json.loads("\n".join(out[1:]))
    for key in ["prompt", "mode", "plan", "files_to_edit", "commands_to_run", "commit_message"]:
        assert key in payload

    assert payload["mode"] == "mock"
