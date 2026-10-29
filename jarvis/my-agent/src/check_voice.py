import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")

print(f"Found {len(voices)} voice(s)\n")

for i, voice in enumerate(voices):
    print(f"Voice {i}")
    print("Name :", voice.name)
    print("ID   :", voice.id)
    print("-" * 50)