import speech_recognition as sr
import pyttsx3,pywhatkit,wikipedia,datetime,keyboard,colors,os
from pygame import mixer
# Crear un objeto reconocedor
recognizer = sr.Recognizer()
engine = pyttsx3.init()
name = "mia"

    
def listen():
    try:
        with sr.Microphone() as source:
            talk("Hola, esto es una prueba")
            print("hola")
            pc = recognizer.listen(source)
            rec =recognizer.recognize_google(pc,language="es")
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name,'')
            else:
               pass
            
    
    except:
        pass
    return rec 

def talk(text):
    engine.say(text)
    engine.runAndWait()
    

escuchar =listen()

if "hola me entiendes" in escuchar:
    talk("te escucho")
elif "quién eres" in escuchar:
    talk("soy un simple programa,para mejorar, a mia")
else:
    print(escuchar)
    talk(escuchar)
    


