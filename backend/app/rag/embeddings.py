from app.core.resources import embedding_model


def get_embedding_model():
    """
    Return the shared HuggingFace embedding model.
    """

    return embedding_model