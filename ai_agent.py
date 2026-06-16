import os
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages.ai import AIMessage
# API Keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# LLM
groq_llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)
gemini_llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
# Tool
tavily_tool = TavilySearch(max_results=2)

# System Prompt
system_prompt = """
You are a helpful assistant.
Use the available tools when necessary to answer the user's question.
"""

# ReAct Agent

def get_response_from_ai_agent(llm_id,query,allow_search,system_prompt,provider):
    if provider=="groq":
        llm=ChatGroq(model=llm_id)
    elif provider=="google":
        llm=ChatGoogleGenerativeAI(model=llm_id) 
    tools=[TavilySearch(max_results=2)] if allow_search else []
    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=system_prompt
    )
    query_str = "\n".join(query) if isinstance(query, list) else query
    state = {
        "messages": [
            {
                "role": "user",
                "content": query_str
            }
        ]
    }
    # Invoke agent
    result = agent.invoke(state)
    messages = result.get("messages")

    ai_messages = [
        msg.content
        for msg in messages
        if isinstance(msg, AIMessage)
    ]

    return ai_messages[-1]