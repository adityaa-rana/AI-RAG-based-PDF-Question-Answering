import google.generativeai as genai

from app.core.config import settings


genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel(settings.GEMINI_MODEL)


def generate_answer(prompt: str) -> str:
    """
    Generate an answer using Gemini.
    """

    try:

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        raise Exception(f"Gemini Error: {str(e)}")