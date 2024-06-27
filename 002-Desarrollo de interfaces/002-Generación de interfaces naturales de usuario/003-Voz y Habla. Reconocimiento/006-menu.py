from gtts import gTTS
from playsound import playsound
import time

def text_to_speech_gtts(text, lang='es'):
    tiempo = time.time()
    tts = gTTS(text=text, lang=lang)
    tts.save(str(int(tiempo))+".mp3")
    playsound(str(int(tiempo))+".mp3")

text_to_speech_gtts("Hola, ¿qué operación deseas realizar?")
time.sleep(2)


