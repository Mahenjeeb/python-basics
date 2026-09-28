from dotenv import load_dotenv
load_dotenv()

from google import genai
from typing import TypedDict, Annotated, Sequence, Optional
from langgraph.graph import StateGraph, END, START

class State(TypedDict):
    user_query: str
    llm_output: Optional[str]
    is_good: Optional[bool]
    
def call_gemini_first(state: State):
    client =  genai.Client()
    resp = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="Explain how AI works in a few words"
    )
    state["llm_output"] = resp.text
    
def call_gemini_second(state: State):
    client =  genai.Client()
    resp = client.models.generate_content(
        model="gemini-3.8-flash",
        contents="Explain how AI works in a few words"
    )
    state["llm_output"] = resp.text
    
def check_resp(state: State):
    if(state["is_good"] == False):
        return "call_gemini_second"
    else:
        return "end_process"
    
def end_process(state: State):
    return state

agent = StateGraph(State)

agent.add_node("call_gemini_first", call_gemini_first)
agent.add_node("call_gemini_second", call_gemini_second)
agent.add_node("end_process", end_process)

agent.add_edge(START, "call_gemini_first")
agent.add_conditional_edges("call_gemini_first", check_resp)
agent.add_edge("call_gemini_second", "end_process")
agent.add_edge("end_process", END)

agent_compiled = agent.compile()
updt_state = agent_compiled.invoke({
    "user_query": "What is langchain ?",
    "llm_output": None,
    "is_good": False,
})

print(updt_state)