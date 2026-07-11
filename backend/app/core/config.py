from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):

    GEMINI_API_KEY: str

    UPLOAD_DIR: str = "uploads"

    VECTOR_STORE_DIR: str = "vector_store"

    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"

    GEMINI_MODEL: str = "gemini-2.5-flash"

    CHUNK_SIZE: int = 500

    CHUNK_OVERLAP: int = 100

    class Config:
        env_file = ".env"


settings = Settings()