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
            f"Page {chunk['page']}\n"
            f"{chunk['text']}\n\n"
        )

    prompt = f"""
You are an expert AI assistant for question answering over PDF documents.

Your task is to answer the user's question ONLY using the provided document context.

Instructions:

1. Use ONLY the information present in the context.
2. Do NOT use your own knowledge.
3. Do NOT guess or hallucinate.
4. If the answer is not available in the context, reply exactly:
   "I couldn't find the answer in the uploaded PDF."
5. Write the answer in clear, concise English.
6. Use bullet points whenever appropriate.
7. If the answer is spread across multiple pages, combine the information naturally.
8. At the end of the answer, mention the page number(s) used in the following format:

Sources:
Page X
or
Pages X, Y, Z

----------------------------
DOCUMENT CONTEXT
----------------------------

{context}

----------------------------
USER QUESTION
----------------------------

{question}

----------------------------
ANSWER
----------------------------
"""

    return prompt