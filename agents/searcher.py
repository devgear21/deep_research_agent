import os
from dotenv import load_dotenv
from serpapi import GoogleSearch
from langchain_core.runnables import RunnableLambda

load_dotenv()
API_KEY = os.getenv("SERPAPI_API_KEY")

def searcher_node(state):
    query = state["query"]
    print(f"[Searcher] Searching using SerpAPI: {query}")

    try:
        search = GoogleSearch({
            "q": query,
            "api_key": API_KEY
        })
        results = search.get_dict()
        organic_results = results.get("organic_results", [])

        links = [r.get("link") for r in organic_results if r.get("link")]
        links = list(set(links))
        print(f"[Searcher] Found {len(links)} links")
        return {**state, "links": links[:5]}
    except Exception as e:
        print(f"[Searcher] SerpAPI Error: {e}")
        return {**state, "links": [], "error": str(e)}

searcher_node = RunnableLambda(searcher_node).with_config({"name": "searcher"})
