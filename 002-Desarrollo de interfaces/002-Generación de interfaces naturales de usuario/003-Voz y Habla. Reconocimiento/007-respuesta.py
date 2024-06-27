from gtts import gTTS
# Programa de interfaz natural
from playsound import playsound
import time
import speech_recognition as sr

recognizer = sr.Recognizer()

def text_to_speech_gtts(text, lang='es'):
    tiempo = time.time()
    tts = gTTS(text=text, lang=lang)
    tts.save(str(int(tiempo))+".mp3")
    playsound(str(int(tiempo))+".mp3")

def recognize_speech_from_mic():
    with sr.Microphone() as source:
        print("Ajustando ruido de fondo")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Escuchamos...")
        audio = recognizer.listen(source)

        try:
            print("Reconociendo...")
            text = recognizer.recognize_google(audio, language="es-ES")
            return text
            
        except sr.RequestError:
             return "Error 1"
        except sr.UnknownValueError:
             return "Error 2"

text_to_speech_gtts("Hola, ¿qué operación deseas realizar?")
opcion = recognize_speech_from_mic()
if opcion == "leer":
    text_to_speech_gtts("Vale, te devuelvo los registros de la base de datos")
elif opcion == "insertar":
    text_to_speech_gtts("Vale, vamos a insertar un nuevo registro")
else:
    text_to_speech_gtts("No he entendido el comando")
time.sleep(2)


