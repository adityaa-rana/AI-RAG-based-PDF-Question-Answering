from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.core.config import settings


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=settings.CHUNK_SIZE,
    chunk_overlap=settings.CHUNK_OVERLAP,
)


def chunk_pages(pages: list[dict]) -> list[dict]:
    """
    Split extracted PDF pages into smaller chunks.

    Args:
        pages (list[dict]):
        [
            {
                "page": 1,
                "text": "..."
            }
        ]

    Returns:
        list[dict]
    """

    chunks = []

    for page in pages:

        page_number = page["page"]

        page_text = page["text"]

        split_text = text_splitter.split_text(page_text)

        for chunk in split_text:

            chunks.append(
                {
                    "page": page_number,
                    "text": chunk
                }
            )

    return chunks