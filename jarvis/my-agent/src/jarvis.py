import os
from text_to_speech import speak
import speech_recognition as sr
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv(".env.local")

# Gemini Client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Text-to-Speech



# Speech Recognition
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("\n🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

            print("Recognizing...")

            text = recognizer.recognize_google(audio)

            print("👤 You:", text)

            return text

        except sr.WaitTimeoutError:
            return None

        except sr.UnknownValueError:
            print("❌ Sorry, I didn't understand.")
            return None

        except Exception as e:
            print("Error:", e)
            return None


# Welcome Message
speak("Hello! I am Jarvis. How can I help you?")

# Main Loop
while True:

    query = listen()

    if not query:
        continue

    # Exit command
    if query.lower() in ["exit", "quit", "stop"]:
        speak("Goodbye!")
        break

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=query
        )

        answer = response.text.strip()

        print("\n" + "=" * 60)
        print("🤖 Jarvis:")
        print(answer)
        print("=" * 60)

        # Speak the answer
        speak(answer)

    except Exception as e:
        print("Gemini Error:", e)
        speak("Sorry, I couldn't get a response.")

