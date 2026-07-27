from langchain.tools import tool
from yt_dlp import YoutubeDL


@tool
def youtube_tool(query: str):
    """
    Search YouTube and return the top 5 most relevant videos.
    """

    ydl_opts = {
        "quiet": True,
        "extract_flat": True,
        "skip_download": True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        results = ydl.extract_info(
            f"ytsearch5:{query}",
            download=False
        )

    videos = []

    for entry in results.get("entries", []):
        videos.append(
            {
                "title": entry.get("title", ""),
                "url": f"https://www.youtube.com/watch?v={entry.get('id', '')}",
                "channel": entry.get("channel", ""),
                "duration": str(entry.get("duration", "")),
                "thumbnail": f"https://i.ytimg.com/vi/{entry.get('id', '')}/hqdefault.jpg",
            }
        )

    return videos