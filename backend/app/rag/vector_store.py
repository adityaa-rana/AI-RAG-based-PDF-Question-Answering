import pickle
from pathlib import Path

import faiss
import numpy as np

from app.core.config import settings
from app.utils.helpers import create_directory

def create_vector_store(chunks: list[dict]) -> None:
    """
    Create and save a FAISS vector store.
    """

    create_directory(settings.VECTOR_STORE_DIR)

    embeddings = np.array(
        [chunk["embedding"] for chunk in chunks],
        dtype="float32"
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    faiss.write_index(
        index,
        str(Path(settings.VECTOR_STORE_DIR) / "faiss_index.bin")
    )

    metadata = [
        {
            "page": chunk["page"],
            "text": chunk["text"]
        }
        for chunk in chunks
    ]

    with open(
        Path(settings.VECTOR_STORE_DIR) / "metadata.pkl",
        "wb"
    ) as file:

        pickle.dump(metadata, file)


def load_vector_store():
    """
    Load FAISS index and metadata.
    """

    index = faiss.read_index(
        str(Path(settings.VECTOR_STORE_DIR) / "faiss_index.bin")
    )

    with open(
        Path(settings.VECTOR_STORE_DIR) / "metadata.pkl",
        "rb"
    ) as file:

        metadata = pickle.load(file)

    return index, metadata

def search_vector_store(
    index,
    query_embedding,
    top_k: int = 3
):
    """
    Search the vector store.
    """

    distances, indices = index.search(
        np.array([query_embedding], dtype="float32"),
        top_k
    )

    return distances, indices