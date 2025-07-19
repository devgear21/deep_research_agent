from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_groq import ChatGroq
import os

llm = ChatGroq(
    model="llama3-70b-8192",
    api_key=os.getenv("GROQ_API_KEY")
)

REPORT_PROMPT = PromptTemplate.from_template("""
You are a professional research report writer.

Given the following:
- User query: {query}
- AI-generated insights and analysis: {analysis}
- Extracted web data: {search_results}
- Events and conferences: {events}

Write a clear, well-structured final report. Include:
- Introduction
- Key Findings
- Upcoming Events (if any)
- Recommendations (if applicable)
- Conclusion

Return only the report text.
""")

def write_report(state: dict) -> dict:
    print("[Writer] Received state:", state)

    query = state.get("query", "No query provided")
    analysis = state.get("analysis", "No analysis available")
    search_results = "\n".join(state.get("content", [])) or "No web content available"
    events = state.get("events", "No events found")

    prompt = REPORT_PROMPT.format(
        query=query,
        analysis=analysis,
        search_results=search_results,
        events=events
    )

    try:
        result = llm.invoke(prompt)
        final_report = result.content
    except Exception as e:
        print("[Writer] LLM error:", e)
        final_report = " An error occurred while generating the report."

    return {**state, "report": final_report}

writer_node = RunnableLambda(write_report).with_config({"name": "writer"})
