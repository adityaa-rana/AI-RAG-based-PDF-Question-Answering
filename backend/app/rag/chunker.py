from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.core.config import settings


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=settings.CHUNK_SIZE,
    chunk_overlap=settings.CHUNK_OVERLAP,
)


def split_documents(documents):
    """
    Split LangChain documents into smaller chunks.

    Args:
        documents (list[Document]): Documents returned by the PDF loader.

    Returns:
        list[Document]: Split document chunks.
    """

    split_docs = text_splitter.split_documents(documents)

    return split_docs