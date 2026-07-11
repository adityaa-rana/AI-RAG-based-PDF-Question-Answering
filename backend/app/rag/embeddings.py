
from app.core.resources import embedding_model
from app.core.config import settings


def generate_embeddings(chunks: list[dict]) -> list[dict]:

    texts = [chunk["text"] for chunk in chunks]

    embeddings = embedding_model.encode(
        texts,
        convert_to_numpy=True,
        show_progress_bar=True
    )

    embedded_chunks = []

    for chunk, embedding in zip(chunks, embeddings):
        embedded_chunks.append({
            "page": chunk["page"],
            "text": chunk["text"],
            "embedding": embedding
        })

    return embedded_chunks