from dotenv import load_dotenv
load_dotenv()

from langgraph.graph import StateGraph, END, START
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage, HumanMessage
from typing import TypedDict, Annotated, Sequence
from langchain_google_genai import ChatGoogleGenerativeAI

# Created a state for nodes
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]

# LLM Config
llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash")
# llm_tools = llm.bind_tools([generate_resp])

# Node to call LLM
def call_llm(state: AgentState):
    "Node to call LLM"
    print("LLM Call ...")
    # response = llm_tools.invoke(state["messages"])
    response = llm.invoke(state["messages"])
    return {"messages": response}

# Assiging state schema
workflow = StateGraph(AgentState)

# Add Nodes
workflow.add_node("agent", call_llm)

workflow.add_edge(START, "agent")
workflow.add_edge("agent", END)
agent = workflow.compile()

# Run Workflow

result = agent.invoke({"messages": [HumanMessage(content="Search for LangGraph docs")]})
print(result["messages"][-1].content)