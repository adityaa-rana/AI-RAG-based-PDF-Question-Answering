import fitz

from app.utils.helpers import clean_text


def extract_text_from_pdf(file_path: str) -> list[dict]:
    """
    Extract text from a PDF page by page.

    Args:
        file_path (str): Path of the PDF.

    Returns:
        list[dict]:
        [
            {
                "page": 1,
                "text": "..."
            }
        ]
    """

    document = fitz.open(file_path)

    pages = []

    for page_number, page in enumerate(document, start=1):

        text = page.get_text()

        text = clean_text(text)

        if text:

            pages.append(
                {
                    "page": page_number,
                    "text": text
                }
            )

    document.close()

    return pages