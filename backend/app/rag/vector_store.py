from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores.utils import DistanceStrategy
from app.core.config import settings
from app.core.resources import embedding_model
from app.utils.helpers import create_directory


def create_vector_store(documents):
    """
    Create and save a FAISS vector store.
    """

    create_directory(settings.VECTOR_STORE_DIR)

    vector_store = FAISS.from_documents(
        documents=documents,
        embedding=embedding_model,
        distance_strategy=DistanceStrategy.COSINE
    )

    vector_store.save_local(settings.VECTOR_STORE_DIR)


def load_vector_store():
    """
    Load the saved FAISS vector store.
    """

    vector_store = FAISS.load_local(
        folder_path=settings.VECTOR_STORE_DIR,
        embeddings=embedding_model,
        allow_dangerous_deserialization=True
    )

    return vector_store


def get_vector_store():
    """
    Return the loaded vector store.
    """

    return load_vector_store()


def get_retriever(top_k: int = 3):
    """
    Return a LangChain retriever.
    """

    vector_store = load_vector_store()

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": top_k
        }
    )

    return retriever