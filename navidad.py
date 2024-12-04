import time 
import speech_recognition as sr
import pyttsx3,keyboard
import pywhatkit
from pygame import mixer


engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def cuenta_regresiva(numero):
  if isinstance(numero, str):
    print("ERROR systnaxis invalida") 
  elif  numero < 0:
    print("ERROR numero invalido")
  else:
    while numero > 0:
        numero -= 1
        print(numero)
        talk(numero)
        time.sleep(1)
        if numero == 0:
          talk("!se siente que viene diciembre, gozate lo que quedaaaa!")
          print("booommm se siente que viene diciembre gozate lo que queda 🎵🎶🎼 ")
          mixer.init()
          mixer.music.load("asistente_virtual/utomp3.com - Feliz NocheBuena  Rodolfo Aicardi  Discos Fuentes.mp3")
          mixer.music.play()
          time.sleep(35)
          

cuenta_regresiva(11)