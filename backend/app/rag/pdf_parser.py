from app.utils.helpers import clean_text

from langchain_community.document_loaders import PyMuPDFLoader


def load_pdf(file_path: str):
    """
    Load a PDF and clean the text of each page.
    """

    loader = PyMuPDFLoader(file_path)

    documents = loader.load()

    for document in documents:
        document.page_content = clean_text(document.page_content)

    return documents