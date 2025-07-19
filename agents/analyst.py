from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnableLambda
import os

llm = ChatGroq(
    model="llama3-70b-8192",
    api_key=os.getenv("GROQ_API_KEY")
)

ANALYSIS_PROMPT = PromptTemplate.from_template(
    "Analyze this content and extract key findings:\n\n{content}"
)

def analyst_node(state: dict) -> dict:
    print("[Analyst] Running with state:", state)
    try:
        content_list = state.get("content", [])
        if not content_list:
            return {**state, "analysis": "No content available to analyze."}

        content = "\n".join(content_list)
        prompt = ANALYSIS_PROMPT.format(content=content)
        result = llm.invoke(prompt)
        analysis = result.content  # Assuming the LLM returns a string with the analysis
        print("[Analyst] Analysis result:", analysis[:100])
        return {**state, "analysis": analysis}
    except Exception as e:
        print("[Analyst] ERROR:", e)
        return {**state, "error": str(e)}

analyst_node = RunnableLambda(analyst_node).with_config({"name": "analyst"})
