
from gemini_ai import ask_gemini
from text_to_speech import speak
from speech_to_text import listen
from datetime import datetime
import os


# Get the current time or date
def get_time_or_date(question):
    question = question.lower()
    now = datetime.now()

    if "time" in question:
        return f"It's {now.strftime('%I:%M %p')}."

    if "date" in question or "today" in question:
        return f"Today is {now.strftime('%A, %B %d, %Y')}."

    return None


# Open or close applications
def open_application(question):
    question = question.lower()

    # Open Notepad
    if "open notepad" in question:
        os.startfile("notepad.exe")
        return "Opening Notepad."

    # Close Notepad
    if "close notepad" in question:
        result = os.system('taskkill /IM notepad.exe /F')

        if result == 0:
            return "Closing Notepad."
        else:
            return "Notepad is not running."

    # Open Chrome
    if "open chrome" in question:
        chrome_paths = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        ]

        for path in chrome_paths:
            if os.path.exists(path):
                os.startfile(path)
                return "Opening Chrome."

        return "I couldn't find Chrome on your computer."

    return None


# Start Jarvis
speak("Hello! I am Jarvis. How can I help you?")

while True:
    # Listen to the user's voice
    question = listen()

    if not question:
        continue

    question = question.lower().strip()

    print("You:", question)

    # Exit Jarvis
    if question in ["exit", "stop jarvis", "goodbye"]:
        speak("Goodbye!")
        break

    # Handle application commands
    app_answer = open_application(question)

    if app_answer:
        print("Jarvis:", app_answer)
        speak(app_answer)
        continue

    # Handle time and date questions
    local_answer = get_time_or_date(question)

    if local_answer:
        print("Jarvis:", local_answer)
        speak(local_answer)
        continue

    # Ask Gemini AI for other questions
    try:
        answer = ask_gemini(question)

        if answer:
            print("Jarvis:", answer)
            speak(answer)
        else:
            speak("Sorry, I couldn't get an answer.")

    except Exception as error:
        print("Error:", error)
        speak("Sorry, something went wrong. Please try again.")
