from app.rag.vector_store import get_vector_store


def retrieve_documents(
    question: str,
    top_k: int = 3
):
    """
    Retrieve LangChain Document objects.

    This function will be used by chain.py.
    """

    vector_store = get_vector_store()

    return vector_store.similarity_search_with_score(
        question,
        k=top_k
    )


def retrieve_relevant_chunks(
    question: str,
    top_k: int = 3
):
    """
    Retrieve the most relevant chunks along with confidence.

    This function is used by the API/frontend.
    """

    vector_store = get_vector_store()

    results = vector_store.similarity_search_with_score(
        query=question,
        k=top_k
    )

    retrieved_chunks = []

    confidence = 0

    for document, score in results:

        similarity = max(0, min(1, 1 - score))

        confidence_score = round(similarity * 100, 2)

        if confidence_score > confidence:
            confidence = confidence_score

        retrieved_chunks.append(
            {
                "page": document.metadata["page"] + 1,
                "text": document.page_content,
                "confidence": confidence_score
            }
        )

    return {
        "chunks": retrieved_chunks,
        "confidence": confidence
    } 