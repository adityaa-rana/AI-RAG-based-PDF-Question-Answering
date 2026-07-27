import json

from langchain_core.output_parsers import StrOutputParser

from app.rag.llm import get_llm
from app.rag.prompt import get_prompt
from app.rag.retriever import retrieve_documents
from app.rag.chat_history import (
    add_ai_message,
    add_human_message,
    get_chat_history,
)


def format_context(documents):

    context = []

    for document in documents:

        page = document.metadata.get("page", 0) + 1

        context.append(
            f"Page {page}\n{document.page_content}"
        )

    return "\n\n".join(context)


def ask_question(question: str):

    results = retrieve_documents(question)

    documents = [doc for doc, score in results]

    scores = [score for doc, score in results]

    context = format_context(documents)

    prompt = get_prompt()

    llm = get_llm()

    chain = (
        prompt
        | llm
        | StrOutputParser()
    )
    history = get_chat_history()
    response = chain.invoke(
        {
            "chat_history": history,
            "context": context,
            "question": question,
        }
    )

    data = json.loads(response)

    add_human_message(question)
    add_ai_message(data["answer"])
    best_score = max(scores)

    confidence = round(best_score * 100, 2)
    data["confidence"] = confidence
    return data