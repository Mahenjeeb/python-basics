# from openai import OpenAI
from ollama import Client
from dotenv import load_dotenv
import os, json
from prompt import prompts
from tools import get_weather_details

load_dotenv()
# Open AI client
# client = OpenAI(
#     api_key= "ollama",
#     base_url=os.getenv('OLLAMA_BASE_URL')
# )
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")
client = Client(OLLAMA_BASE_URL)
_SYSTEM_PROMPTS = prompts()
_PROMPTS = [{
    "role": "system",
    "content": _SYSTEM_PROMPTS
}]
user_input =  input("> ")
_PROMPTS.append({
    "role": "user",
    "content": user_input
})
available_tools = {
    "get_weather_details": get_weather_details
}

def initChat():
    while True:
        # response = client.chat.completions.create(
        #     model="gemma:2b",
        #     messages=_PROMPTS
        # )
        response = client.chat(
            model="gemma:2b",
            messages=_PROMPTS,
            stream=False
        )
        # choice = response.choices[0]
        # raw_resp = choice.message.content
        raw_resp = response["message"]["content"]
        if not raw_resp:
            raise RuntimeError("The model returned an empty response.")

        _PROMPTS.append({"role": "assistant", "content": raw_resp})
        print(raw_resp)
        break
        json_parse = json_parse = json.JSONDecoder().raw_decode(raw_resp[raw_resp.index('{'):])[0] if '{' in raw_resp else {"step": "OUTPUT", "content": raw_resp}   
        step = json_parse.get("step")

        if step in ("START", "PLAN"):
            print(json_parse.get("content"))
            continue

        if step == "TOOL":
            tool_name = json_parse.get("tool")
            tool_input = json_parse.get("input")
            tool_response = available_tools[tool_name](tool_input)
            _PROMPTS.append({
                "role": "developer",
                "content": json.dumps({
                    "step": "OBSERVE",
                    "tool": tool_name,
                    "output": tool_response
                })
            })
            continue

        if step == "OUTPUT":
            print(json_parse.get("content"))
            break