from langgraph.graph import StateGraph, END
from typing import TypedDict, List, Optional

from agents.searcher import searcher_node as raw_searcher
from agents.scraper import scraper_node as raw_scraper
from agents.analyst import analyst_node as raw_analyst
from agents.event_finder import event_finder_node as raw_event_finder
from agents.writer import writer_node as raw_writer

# agent state structure
class AgentState(TypedDict, total=False):
    query: str
    links: List[str]
    content: List[str]
    analysis: str
    events: str
    report: str
    error: Optional[str]

#Wraping nodes with config only 
searcher_node = raw_searcher.with_config({"name": "searcher"})
scraper_node = raw_scraper.with_config({"name": "scraper"})
analyst_node = raw_analyst.with_config({"name": "analyst"})
event_finder_node = raw_event_finder.with_config({"name": "event_finder"})
writer_node = raw_writer.with_config({"name": "writer"})

# Building the workflow
workflow = StateGraph(AgentState)
workflow.add_node("searcher", searcher_node)
workflow.add_node("scraper", scraper_node)
workflow.add_node("analyst", analyst_node)
workflow.add_node("event_finder", event_finder_node)
workflow.add_node("writer", writer_node)

workflow.set_entry_point("searcher")
workflow.add_edge("searcher", "scraper")
workflow.add_edge("scraper", "analyst")
workflow.add_edge("analyst", "event_finder")
workflow.add_edge("event_finder", "writer")
workflow.add_edge("writer", END)

# Compiling the workflow
research_graph = workflow.compile()
