import speech_recognition as sr

r = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print("🎤 Speak something...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source, timeout=10)

    print("Recognizing...")

    text = r.recognize_google(audio)
    print("✅ You said:", text)

except sr.UnknownValueError:
    print("❌ Could not understand your voice.")

except sr.RequestError as e:
    print("❌ Google Speech service error:", e)

except Exception as e:
    print("❌ Error:", e)