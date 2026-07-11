from app.core.resources import embedding_model
import faiss
import numpy as np
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
    query_embedding = resources.embedding_model.encode(question)

    query_embedding = np.array(
        query_embedding,
        dtype="float32"
    )

    faiss.normalize_L2(
        query_embedding.reshape(1, -1)
    )

    # Load FAISS index and metadata
    index, metadata = load_vector_store()

    # Search the vector database
    similarities, indices = search_vector_store(
        resources.faiss_index,
        query_embedding,
        top_k
    )

    # Retrieve matching chunks
    retrieved_chunks = []

    for similarity, idx in zip(
        similarities[0],
        indices[0]
    ):

        chunk = resources.metadata[idx].copy()

        chunk["confidence"] = round(
            float(similarity) * 100,
            2
        )

        retrieved_chunks.append(chunk)

    return {

    "chunks": retrieved_chunks,

    "confidence": retrieved_chunks[0]["confidence"]

}