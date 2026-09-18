from openai import OpenAI
from dotenv import load_dotenv
import os, json
from prompts import prompts

load_dotenv()
SYSTEM_PROMPTS = prompts()
client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

messages_output = []
messages_output.append({"role": "system","content": SYSTEM_PROMPTS})
print("\n\n")
user_input = input(">>")
messages_output.append({"role": "user","content": user_input})
while True:
    response = client.chat.completions.create(
        model="gemini-3.5-flash",
        messages=messages_output
    )

    raw_result = response.choices[0].message.content
    if raw_result is None:
        raise ValueError("The model returned an empty response.")

    raw_result = raw_result.strip()
    if raw_result.startswith("```"):
        raw_result = raw_result.removeprefix("```json").removeprefix("```").removesuffix("```").strip()

    messages_output.append({"role": "assistant", "content": raw_result})
    parsed_result = json.loads(raw_result)
    results = parsed_result if isinstance(parsed_result, list) else [parsed_result]

    for result in results:
        if not isinstance(result, dict):
            raise ValueError("The model response must contain JSON step objects.")

        step = result.get("step")
        content = result.get("content")
        if step == "START":
            print(f"🚀,{content}")
        elif step == "PLAN":
            print(f"🕐,{content}")
        elif step == "OUTPUT":
            print(f"✅,{content}")
            break
        else:
            raise ValueError(f"Unknown step returned by model: {step!r}")
    else:
        continue
    break
print("\n\n")