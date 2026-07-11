from app.core.resources import embedding_model

from app.core.config import settings
from app.rag.vector_store import (
    load_vector_store,
    search_vector_store
)

from app.core import resources

def retrieve_relevant_chunks(
    question: str,
    top_k: int = 3
) -> list[dict]:
    """
    Retrieve the most relevant chunks for a question.

    Args:
        question (str): User's question.
        top_k (int): Number of chunks to retrieve.

    Returns:
        list[dict]
    """

    # Generate question embedding
    query_embedding = embedding_model.encode(
        question,
        convert_to_numpy=True
    )

    # Load FAISS index and metadata
    index, metadata = load_vector_store()

    # Search the vector database
    _, indices = search_vector_store(
        resources.faiss_index,
        query_embedding,
        top_k
    )

    # Retrieve matching chunks
    retrieved_chunks = []

    for index in indices[0]:

        for index in indices[0]:
            retrieved_chunks.append(
                resources.metadata[index]
            )

    return retrieved_chunks