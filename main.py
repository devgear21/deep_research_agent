from server import handle

def main():
    print("\U0001F50D Deep Research Agent (LangGraph + MCP)")
    query = input("Enter your research topic or question: ").strip()

    if not query:
        print("\u26A0\uFE0F No query provided. Exiting.")
        return

    print("\n\u23F3 Running research workflow...\n")
    result = handle({"query": query})

    print("\n\U0001F4C4 ===== FINAL REPORT =====\n")
    print(result.get("report", "\u274C No report generated."))

if __name__ == "__main__":
    main()
