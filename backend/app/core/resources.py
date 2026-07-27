from langchain_huggingface import HuggingFaceEmbeddings

from app.core.config import settings


# Shared embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name=settings.EMBEDDING_MODEL,
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True}
)

faiss_index = None

metadata = None