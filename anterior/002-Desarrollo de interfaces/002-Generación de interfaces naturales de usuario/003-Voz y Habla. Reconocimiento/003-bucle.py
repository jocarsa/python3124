# pip install SpeechRecognition
# pip install pyaudio

import speech_recognition as sr

recognizer = sr.Recognizer()

def recognize_speech_from_mic():
    with sr.Microphone() as source:
        print("Ajustando ruido de fondo")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Escuchamos...")
        audio = recognizer.listen(source)

        try:
            print("Reconociendo...")
            text = recognizer.recognize_google(audio, language="es-ES")
            print(f"Reconocido: {text}")
        except sr.RequestError:
            print("Error 1")
        except sr.UnknownValueError:
            print("Error 2")
while True:
    recognize_speech_from_mic()
