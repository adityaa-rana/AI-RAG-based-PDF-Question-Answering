def build_prompt(
    question: str,
    retrieved_chunks: list[dict]
) -> str:
    """
    Build the prompt for Gemini.

    Args:
        question (str): User question.
        retrieved_chunks (list[dict]): Retrieved chunks.

    Returns:
        str: Prompt for Gemini.
    """

    context = ""

    for chunk in retrieved_chunks:

        context += (
            f"Page {chunk['page']}:\n"
            f"{chunk['text']}\n\n"
        )

    prompt = f"""
You are a helpful AI assistant.

Use ONLY the context below to answer the user's question.

If the answer cannot be found in the context,
reply with:

"I couldn't find the answer in the uploaded PDF."

Context:
{context}

Question:
{question}

Answer:
"""

    return prompt