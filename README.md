# PDF AI - Research Paper Question Answering using RAG

An AI-powered Research Paper Assistant that allows users to upload PDF documents and ask natural language questions about their contents. The application leverages **Retrieval-Augmented Generation (RAG)** to retrieve the most relevant sections from the uploaded document and uses **Google Gemini** to generate context-aware answers.

The project combines **FastAPI**, **React**, **Sentence Transformers**, **FAISS**, **PyMuPDF**, and **Google Gemini** to build an end-to-end AI application capable of semantic document search and intelligent question answering.

---

# Why this Project?

Large PDF documents such as research papers, books, lecture notes, and technical documentation often contain hundreds of pages, making it difficult to locate specific information quickly.

Traditional keyword search only finds exact word matches and fails to understand the semantic meaning of a user's query.

This project addresses these limitations by implementing a **Retrieval-Augmented Generation (RAG)** pipeline. Instead of searching for exact keywords, the system converts document chunks and user queries into vector embeddings, retrieves the most semantically relevant content using **FAISS**, and generates accurate answers grounded entirely in the uploaded PDF.

---

# Features

- Upload PDF documents
- Automatic PDF text extraction
- Intelligent document chunking
- Semantic search using Sentence Transformers
- FAISS Vector Database
- Retrieval-Augmented Generation (RAG)
- Google Gemini powered answer generation
- Retrieval Confidence Score
- Source Page References
- Copy AI Responses
- Clear Chat History
- Modern Minimal React UI
- FastAPI REST Backend

---

# Tech Stack

| Category | Technologies |
|------------|-------------------------------|
| Frontend | React, Vite, Axios, Tailwind CSS |
| Backend | FastAPI, Python |
| PDF Parsing | PyMuPDF |
| Embedding Model | Sentence Transformers (all-MiniLM-L6-v2) |
| Vector Database | FAISS |
| Large Language Model | Google Gemini 2.5 Flash |
| Validation | Pydantic |
| Environment | Python Virtual Environment |

---

# Project Workflow

```text
                Upload PDF
                     │
                     ▼
         Extract Text using PyMuPDF
                     │
                     ▼
            Split into Chunks
                     │
                     ▼
 Generate Embeddings (MiniLM-L6-v2)
                     │
                     ▼
      Store Embeddings in FAISS
                     │
──────────────────────────────────────────

             User Question
                     │
                     ▼
      Generate Query Embedding
                     │
                     ▼
 Retrieve Most Relevant Chunks (Top-K)
                     │
                     ▼
         Build Context Prompt
                     │
                     ▼
      Google Gemini 2.5 Flash
                     │
                     ▼
       Context-Aware AI Answer
```

---

# Demo
<img width="1167" height="996" alt="Screenshot 2026-07-12 011539" src="https://github.com/user-attachments/assets/5d0aa497-c940-445a-aad0-e5fb3d79a48d" />

<img width="1178" height="1017" alt="Screenshot 2026-07-12 012619" src="https://github.com/user-attachments/assets/5e732223-0694-40ca-b488-8c20e79aa479" />


- Home Page
- Upload PDF
- Chat Interface
- AI Generated Answers
- Retrieval Confidence Display

- # RAG Pipeline

The application follows a **Retrieval-Augmented Generation (RAG)** architecture, where the Large Language Model answers questions using only the relevant information retrieved from the uploaded document instead of relying solely on its pretrained knowledge.

```text
                   PDF Document
                        │
                        ▼
              PDF Text Extraction
                        │
                        ▼
               Text Chunking
                        │
                        ▼
      Sentence Transformer Embeddings
                        │
                        ▼
           FAISS Vector Database
──────────────────────────────────────────

                User Question
                        │
                        ▼
        Sentence Transformer Embedding
                        │
                        ▼
         Cosine Similarity Search
                        │
                        ▼
          Top-K Relevant Chunks
                        │
                        ▼
            Prompt Construction
                        │
                        ▼
           Google Gemini 2.5 Flash
                        │
                        ▼
               Generated Answer
```

---

# System Architecture

```text
                  React Frontend
                        │
                        ▼
                FastAPI REST API
                        │
        ┌───────────────┼────────────────┐
        │               │                │
        ▼               ▼                ▼

 PDF Processing   Vector Retrieval   Gemini API
        │               │                │
        ▼               ▼                ▼

 PDF Parser      Sentence Embeddings  AI Answer
        │               │
        ▼               ▼

    Chunking        FAISS Vector Store
```

---

# AI Modules

## pdf_parser.py

### Purpose

Extracts text from uploaded PDF documents.

### Input

- PDF Document

### Output

- Extracted text page by page

### Library Used

- PyMuPDF

---

## chunker.py

### Purpose

Splits extracted text into overlapping chunks while preserving semantic context.

### Why?

Large Language Models have context limits.

Instead of embedding an entire document, it is divided into smaller overlapping chunks for better retrieval accuracy.

---

## embeddings.py

### Purpose

Generates dense vector embeddings for every text chunk.

### Model Used

```
Sentence Transformers

↓

all-MiniLM-L6-v2
```

Each chunk is converted into a **384-dimensional embedding vector** representing its semantic meaning.

---

## vector_store.py

### Purpose

Stores document embeddings inside a FAISS vector database.

### Responsibilities

- Create FAISS Index
- Store Embeddings
- Store Chunk Metadata
- Load Existing Vector Store
- Perform Similarity Search

---

## retriever.py

### Purpose

Retrieves the most relevant document chunks for a given user query.

### Pipeline

```text
Question

↓

Generate Query Embedding

↓

Cosine Similarity Search

↓

Top-K Chunks
```

The retrieved chunks are then passed to the prompt builder.

---

## prompt.py

### Purpose

Constructs a structured prompt containing:

- Retrieved document context
- User question
- Instructions to avoid hallucination

This ensures the LLM answers **only from the uploaded document**.

---

## generator.py

### Purpose

Sends the final prompt to **Google Gemini 2.5 Flash** and generates a context-aware response.

---

# Project Structure

```text
PDF-AI/
│
├── backend/
│   │
│   ├── app/
│   │   │
│   │   ├── api/
│   │   │      routes.py
│   │   │
│   │   ├── core/
│   │   │      config.py
│   │   │      resources.py
│   │   │
│   │   ├── models/
│   │   │      schemas.py
│   │   │
│   │   ├── rag/
│   │   │      pdf_parser.py
│   │   │      chunker.py
│   │   │      embeddings.py
│   │   │      vector_store.py
│   │   │      retriever.py
│   │   │      prompt.py
│   │   │      generator.py
│   │   │
│   │   ├── utils/
│   │   │      helpers.py
│   │   │
│   │   └── main.py
│   │
│   ├── uploads/
│   ├── vector_store/
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   │
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/pdf-ai-rag.git

cd pdf-ai-rag
```

---

# Backend Setup

Navigate to the backend folder

```bash
cd backend
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file inside the backend directory.

```env
GEMINI_API_KEY=YOUR_GOOGLE_GEMINI_API_KEY
```

---

# Running the Backend

```bash
uvicorn app.main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

Navigate to frontend

```bash
cd frontend
```

Install dependencies

```bash
npm install
```

Run development server

```bash
npm run dev
```

Frontend URL

```
http://localhost:5173
```

---

# API Endpoints

## Upload PDF

```
POST /upload
```

Uploads a PDF, extracts text, generates embeddings, and creates the FAISS vector database.

---

## Ask Question

```
POST /ask
```

Accepts a user question and returns:

- AI-generated answer
- Retrieval confidence score

---

## Health Check

```
GET /health
```

Checks whether the backend server is running.

---

# How to Use

### Step 1

Upload a PDF document.

↓

### Step 2

The backend automatically

- Extracts text
- Splits text into chunks
- Generates embeddings
- Stores embeddings in FAISS

↓

### Step 3

Ask a question in natural language.

↓

### Step 4

The system retrieves the most relevant chunks using semantic similarity.

↓

### Step 5

The retrieved chunks are passed to Google Gemini.

↓

### Step 6

Gemini generates a context-aware answer grounded in the uploaded document.

↓

### Step 7

The frontend displays

- AI Answer
- Retrieval Confidence
- Source Page References

---

# Retrieval Confidence

The application displays a **Retrieval Confidence Score** for every generated answer.

Unlike LLM confidence, this score represents how well the retrieved document chunks match the user's query.

The confidence is computed using **cosine similarity** between the question embedding and the top retrieved chunk stored in the FAISS vector database.

Higher confidence indicates a stronger semantic match between the question and the retrieved document context.
---

# Challenges Faced

Developing this Retrieval-Augmented Generation (RAG) system involved solving several challenges across document processing, semantic search, and AI integration.

## 1. Extracting Text from PDFs

PDF documents often contain multiple columns, tables, figures, and inconsistent formatting, making reliable text extraction challenging.

To address this, **PyMuPDF** was used to efficiently extract page-wise text while preserving document structure as much as possible.

---

## 2. Choosing an Optimal Chunk Size

Very small chunks lose important context, while very large chunks reduce retrieval accuracy.

After experimentation, the document was divided into overlapping chunks to balance semantic context and retrieval performance.

---

## 3. Semantic Retrieval

Traditional keyword search only matches exact words and fails to understand meaning.

To overcome this limitation, the project uses **Sentence Transformers** to convert text into dense vector embeddings, enabling semantic similarity search.

---

## 4. Efficient Similarity Search

Searching every embedding sequentially becomes computationally expensive as document size increases.

To solve this, **FAISS** was used as the vector database, enabling fast nearest-neighbor search over document embeddings.

---

## 5. Reducing Hallucinations

Large Language Models may generate answers that are not present in the uploaded document.

A carefully designed prompt ensures that Gemini answers **only from the retrieved document context**, minimizing hallucinations and improving reliability.

---

# Future Improvements

The current implementation focuses on a clean single-document RAG pipeline. Several enhancements can be added in future versions.

- Multi-PDF Question Answering
- Semantic Chunking
- Hybrid Retrieval (Dense + BM25)
- Reranking Models
- PDF Preview Panel
- Highlight Retrieved Text
- Source Citation Links
- Conversation Memory
- Streaming AI Responses
- Docker Deployment
- Cloud Deployment

---

# Key Learnings

Through this project, I gained practical experience with:

- Retrieval-Augmented Generation (RAG)
- FastAPI REST API Development
- React Frontend Development
- PDF Parsing using PyMuPDF
- Sentence Transformers
- Vector Embeddings
- FAISS Vector Database
- Cosine Similarity Search
- Prompt Engineering
- Google Gemini API Integration
- End-to-End AI Application Development

---
