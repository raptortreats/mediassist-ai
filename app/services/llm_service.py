import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-3.5-flash-lite")

def answer_question(question: str, context: str) -> str:
    """
    Generate an answer using the retrieved context.
    """

    prompt = f"""
You are a medical document assistant.

Answer ONLY using the provided context.

If the answer is not present, say:
"I couldn't find that information in the uploaded document."

Context:
{context}

Question:
{question}
"""

    response = model.generate_content(prompt)

    return response.text