#  Deep Research Agent

A modular, AI-powered research assistant built with *Streamlit, **LangGraph, **LangChain, **SerpAPI, and **Groq*. It automates web research on any topic i.e. extracting links, scraping pages, analyzing content, identifying events, and generating structured reports.

---

##  Features

-  *Streamlit UI* for interactive research queries
-  *SerpAPI-based search* to fetch relevant web pages
-  *Content scraper* using BeautifulSoup
-  *LLM-powered analyst* (Groq + LLaMA3 70B) for extracting insights
-  *Event Finder* to identify upcoming conferences or meetings
-  *Research Writer* to synthesize a clean, structured final report
-  Built using *LangGraph stateful workflows*
-  *LangSmith* used for debugging, monitoring, and tracing agent execution

---

##  Demo

<p align="center">
  <a href="https://youtu.be/hxuwwLcTe_s">
    <img src="https://img.youtube.com/vi/hxuwwLcTe_s/0.jpg" alt="Watch the video" />
  </a>
</p>

---

##  Architecture Overview

<div align="center">

```plaintext
User Input (Query)
        ↓
[Searcher Node] → Search via SerpAPI → Extract links
        ↓
[Scraper Node] → Scrape page content
        ↓
[Analyst Node] → AI-powered insights
        ↓
[Event Finder Node] → Detect related events
        ↓
[Writer Node] → Final structured report
