import os
import json
from langchain_core.runnables import RunnableLambda
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq

from langchain.prompts import PromptTemplate

EVENT_PROMPT = PromptTemplate.from_template(
    "From the following analysis, extract any current or upcoming events, meetings, or conferences related to the topic:\n\n{analysis}"
)

def event_finder_node(state: dict) -> dict:
    print("[EventFinder] Running with state:", state)
    try:
        analysis = state.get("analysis", "")
        result = f"Detected events from analysis: {analysis[:100]}..."
        print("[EventFinder] Events extracted")
        return {**state, "events": result}
    except Exception as e:
        print("[EventFinder] ERROR:", e)
        return {**state, "error": str(e)}


event_finder_node = RunnableLambda(event_finder_node).with_config({"name": "event_finder"})
