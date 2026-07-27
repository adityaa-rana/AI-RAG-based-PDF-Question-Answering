from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import HTTPException

from app.models.schemas import (
    AskRequest,
    AskResponse,
    Video,
    WebResource,
)

from app.utils.helpers import save_uploaded_file

from app.rag.pdf_parser import load_pdf
from app.rag.chunker import split_documents
from app.rag.vector_store import create_vector_store
from app.rag.chain import ask_question

from app.agent.youtube_tool import youtube_tool
from app.agent.web_tool import web_tool


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

    # Load PDF
    documents = load_pdf(file_path)

    # Split into chunks
    chunks = split_documents(documents)

    # Create Vector Store
    create_vector_store(chunks)

    return {
        "message": "PDF processed successfully.",
        "pages": len(documents),
        "chunks": len(chunks)
    }


@router.post(
    "/ask",
    response_model=AskResponse
)
async def ask(request: AskRequest):

    try:

        # Step 1: Get answer + search queries from RAG
        rag_result = ask_question(request.question)

        # Step 2: Search YouTube
        youtube_results = youtube_tool.invoke(
            rag_result["youtube_query"]
        )

        # Step 3: Search Web
        web_results = web_tool.invoke(
            rag_result["web_query"]
        )

        return AskResponse(
            answer=rag_result["answer"],
            confidence=rag_result["confidence"],
            youtube=[
                Video(**video)
                for video in youtube_results
            ],
            web=[
                WebResource(**resource)
                for resource in web_results
            ]
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )