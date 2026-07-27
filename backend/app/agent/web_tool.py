from langchain.tools import tool
from tavily import TavilyClient

from app.core.config import settings


client = TavilyClient(api_key=settings.TAVILY_API_KEY)


@tool
def web_tool(query: str):
    """
    Search the web and return the top 5 relevant resources.
    """

    response = client.search(
        query=query,
        max_results=5,
    )

    resources = []

    for result in response["results"]:

        resources.append(
            {
                "title": result["title"],
                "url": result["url"],
                "content": result["content"],
            }
        )

    return resources