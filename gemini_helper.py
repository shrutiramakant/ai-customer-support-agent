
import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None

AI_ERROR_MESSAGE = "AI_SUPPORT_ERROR"

# Stores conversation messages during the current session
conversation_history = []


def ask_gemini(message):
    """Get a customer-support response using Gemini."""

    if client is None:
        return AI_ERROR_MESSAGE

    try:
        start_time = time.time()

        # Add the customer's latest message
        conversation_history.append(
            {
                "role": "user",
                "parts": [{"text": message}]
            }
        )

        # Keep the latest 10 messages to limit request size
        recent_history = conversation_history[-10:]

        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=recent_history,
            config=types.GenerateContentConfig(
                system_instruction="""
You are a polite customer support assistant.
Answer customer questions clearly and briefly.
Do not invent order details, payment status, or account information.
If you cannot confidently answer, recommend contacting human support.
""",
                thinking_config=types.ThinkingConfig(
                    thinking_level="low"
                )
            )
        )

        print(
            "Gemini response time:",
            round(time.time() - start_time, 2),
            "seconds"
        )

        if response.text:
            answer = response.text.strip()

            # Save Gemini's answer for future follow-up questions
            conversation_history.append(
                {
                    "role": "model",
                    "parts": [{"text": answer}]
                }
            )

            return answer

        # Remove the unanswered customer message
        conversation_history.pop()
        return AI_ERROR_MESSAGE

    except Exception as e:
      print("Gemini error:", e)

    # Remove the failed message from conversation history
    if (
        conversation_history
        and conversation_history[-1]["role"] == "user"
        and conversation_history[-1]["parts"][0]["text"] == message
    ):
        conversation_history.pop()

    # Return a safe message to the chatbot
    return AI_ERROR_MESSAGE

    
