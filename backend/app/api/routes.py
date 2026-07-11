from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import HTTPException

from app.models.schemas import AskRequest
from app.models.schemas import AskResponse

from app.utils.helpers import save_uploaded_file

from app.rag.pdf_parser import extract_text_from_pdf
from app.rag.chunker import chunk_pages
from app.rag.embeddings import generate_embeddings
from app.rag.vector_store import (
    create_vector_store,
    load_vector_store
)
from app.rag.retriever import retrieve_relevant_chunks
from app.rag.prompt import build_prompt
from app.rag.generator import generate_answer

from app.core import resources


router = APIRouter()


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    # Save uploaded PDF
    file_path = save_uploaded_file(file)

    # Extract text
    pages = extract_text_from_pdf(file_path)

    # Split into chunks
    chunks = chunk_pages(pages)

    # Generate embeddings
    embedded_chunks = generate_embeddings(chunks)

    # Build vector database
    create_vector_store(embedded_chunks)

    # Load vector database into memory
    index, metadata = load_vector_store()

    # initialize none to value
    resources.faiss_index = index
    resources.metadata = metadata

    return {
        "message": "PDF processed successfully.",
        "pages": len(pages),
        "chunks": len(chunks)
    }


@router.post(
    "/ask",
    response_model=AskResponse
)
async def ask_question(request: AskRequest):

    if resources.faiss_index is None:
        raise HTTPException(
            status_code=400,
            detail="Please upload a PDF first."
        )

    retrieval_result = retrieve_relevant_chunks(
    request.question
)

    prompt = build_prompt(
        request.question,
        retrieval_result["chunks"]
    )

    answer = generate_answer(prompt)

    return AskResponse(

    answer=answer,

    confidence=round(retrieval_result["confidence"],2)

)