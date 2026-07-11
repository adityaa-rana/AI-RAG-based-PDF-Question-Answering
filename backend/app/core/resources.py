from sentence_transformers import SentenceTransformer

from app.core.config import settings


# Shared embedding model
embedding_model = SentenceTransformer(
    settings.EMBEDDING_MODEL
)

faiss_index = None

metadata = None