import asyncio
import edge_tts
import pygame
import os

VOICE = "en-US-AriaNeural"

async def speak_async(text):
    output_file = "jarvis_voice.mp3"

    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(output_file)

    pygame.mixer.init()
    pygame.mixer.music.load(output_file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)

    pygame.mixer.music.unload()
    pygame.mixer.quit()

    if os.path.exists(output_file):
        os.remove(output_file)


def speak(text):
    asyncio.run(speak_async(text))