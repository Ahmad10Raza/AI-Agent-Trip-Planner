
from langchain_community.tools import DuckDuckGoSearchResults
from crewai.tools import tool

# ✅ CrewAI-compatible tool for web search
@tool
def search_web_tool(input) -> str:
    """
    Searches the web using DuckDuckGo and returns the top results.
    """
    try:
        query = input if isinstance(input, str) else input.get("query", "")
        search = DuckDuckGoSearchResults(num_results=5)
        return search.run(query)
    except Exception as e:
        return f"Web search failed: {e}"
