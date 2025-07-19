# Deep Research Agent

A multi-agent research system built with LangGraph that performs comprehensive research and analysis.

## Overview

This project implements a workflow of specialized agents that work together to:
- Search for information
- Scrape web content
- Analyze data
- Find relevant events
- Generate comprehensive reports

## Architecture

The system uses a state-based workflow with the following agents:
- **Searcher**: Finds relevant links and sources
- **Scraper**: Extracts content from web sources
- **Analyst**: Analyzes the collected content
- **Event Finder**: Identifies relevant events
- **Writer**: Generates the final report

## Project Structure

```
deepResearcher/
├── app.py              # Main application entry point
├── graph.py            # LangGraph workflow definition
├── main.py             # Alternative entry point
├── server.py           # Server implementation
├── requirements.txt    # Python dependencies
├── agents/
│   ├── searcher.py     # Search agent
│   ├── scraper.py      # Web scraping agent
│   ├── analyst.py      # Analysis agent
│   ├── event_finder.py # Event detection agent
│   └── writer.py       # Report generation agent
└── mcp_config/
    └── manifest.yaml   # Configuration file
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/devgear21/deep_research_agent.git
cd deep_research_agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python app.py
```

Or use the server:
```bash
python server.py
```

## Dependencies

See `requirements.txt` for a complete list of dependencies.

## License

This project is open source. Please see the LICENSE file for details.
