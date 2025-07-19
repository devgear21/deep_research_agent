import requests
from bs4 import BeautifulSoup
from langchain_core.runnables import RunnableLambda

def scraper_node(state: dict) -> dict:
    links = state.get("links", [])
    contents = []

    for url in links:
        try:
            print(f"[Scraper] Fetching: {url}")
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            }
            response = requests.get(url, headers=headers, timeout=30)

            if response.status_code != 200:
                print(f"[Scraper] Failed ({response.status_code}): {url}")
                continue

            soup = BeautifulSoup(response.text, "html.parser")
            text = soup.get_text(separator="\n", strip=True)
            contents.append(text[:2000])  # Limit per page

        except Exception as e:
            print(f"[Scraper] Error fetching {url}:", e)
            continue

    print(f"[Scraper] Extracted content from {len(contents)} pages")
    return {**state, "content": contents}

scraper_node = RunnableLambda(scraper_node).with_config({"name": "scraper"})
