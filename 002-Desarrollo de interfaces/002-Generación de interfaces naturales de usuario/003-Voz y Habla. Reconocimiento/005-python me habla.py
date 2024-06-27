from gtts import gTTS
from playsound import playsound
import time

def text_to_speech_gtts(text, lang='es'):
    tiempo = time.time()
    tts = gTTS(text=text, lang=lang)
    tts.save(str(int(tiempo))+".mp3")
    playsound(str(int(tiempo))+".mp3")

text_to_speech_gtts("Hola, ¿cómo estás?")
time.sleep(2)
text_to_speech_gtts("Este es un texto de prueba")
time.sleep(2)
text_to_speech_gtts("Esta es otra prueba que estoy haciendo")
