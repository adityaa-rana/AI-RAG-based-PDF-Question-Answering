from pathlib import Path
import shutil
import re

from fastapi import UploadFile

from app.core.config import settings


def create_directory(directory_path: str) -> None:
    """
    Create a directory if it does not already exist.

    Args:
        directory_path (str): Path of the directory.
    """

    Path(directory_path).mkdir(parents=True, exist_ok=True)


def save_uploaded_file(file: UploadFile) -> str:
    """
    Save an uploaded PDF into the uploads folder.

    Args:
        file (UploadFile): Uploaded PDF file.

    Returns:
        str: Path where the file is saved.
    """

    create_directory(settings.UPLOAD_DIR)

    file_path = Path(settings.UPLOAD_DIR) / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return str(file_path)


def delete_uploaded_file(file_path: str) -> None:
    """
    Delete a file if it exists.

    Args:
        file_path (str): Path of the file.
    """

    path = Path(file_path)

    if path.exists():
        path.unlink()


def clean_text(text: str) -> str:
    """
    Clean extracted PDF text.

    Operations:
    - Remove extra spaces
    - Remove multiple newlines
    - Remove tabs
    - Strip leading/trailing spaces

    Args:
        text (str): Raw extracted text.

    Returns:
        str: Cleaned text.
    """

    text = text.replace("\t", " ")

    text = re.sub(r"\n+", "\n", text)

    text = re.sub(r" +", " ", text)

    return text.strip()