import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)   # Zira
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)

print("Speaking...")

engine.say("Hello")
engine.runAndWait()

print("Finished")