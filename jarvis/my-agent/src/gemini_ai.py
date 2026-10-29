import os
from dotenv import load_dotenv
from google import genai

load_dotenv(".env.local")

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_gemini(prompt):
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=f"""
You are Jarvis, a friendly personal AI voice assistant.

Your personality:
- Talk naturally, like a real human in conversation.
- Keep answers short, usually 1 to 3 sentences.
- Use simple, everyday English.
- Be friendly, calm, and helpful.
- Answer directly without unnecessary introductions.
- Avoid bullet points and long explanations when speaking.
- If the user asks for details, explain more.
- If the user greets you, greet them naturally.
- Never repeat the user's question unnecessarily.

User says: {prompt}
"""
    )
    return response.text
