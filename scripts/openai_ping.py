import os

if os.getenv("MOCK_OPENAI") == "1":
    print("OK")
else:
    from openai import OpenAI
    client = OpenAI()
    resp = client.responses.create(model="gpt-5", input="Reply with exactly: OK")
    print(resp.output_text)
