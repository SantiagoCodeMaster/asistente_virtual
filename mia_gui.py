#importamos las librerias
import speech_recognition as sr
import pyttsx3,pywhatkit,wikipedia,datetime,keyboard,colors,os
from pygame import mixer
import time 
import subprocess as sub 
from tkinter import * 
from PIL import Image,ImageTk
import threading as tr

main_window = Tk()
main_window.title("Mia AI")

main_window.geometry("900x600")
main_window.resizable(0,0)
main_window.configure(bg='#C5796D')

comandos  = """"
         Comandos que puedes usar :
         -reproduce...(youtube)
         -colores...(detecta rojo,
         amarillo)
         -pon...(una cancion)
         -abre...(una pagina web)
         -para...(no te escucha)
"""

label_title= Label(main_window,text="Mia IA",bg='#DBE6F6',fg='#000428', font=('Arial',30,'bold'))
label_title.pack(pady=10)

canvas_comandos = Canvas(bg='#C5796D',height= 320,width=300)
canvas_comandos.place(x=0,y=0)

canvas_comandos.create_text(115,135, text = comandos,fill = 'black',font ='Arial 10')

Texto_info = Text(main_window,bg='#ff9068',fg = "black")
Texto_info.place(x=0,y=320,height=280,width=300)



Mia_photo = ImageTk.PhotoImage(Image.open("asistente_virtual/foto robot.png"))
window_photo = Label(main_window,image=Mia_photo)
window_photo.pack(pady=5)

def change_voices(id):
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[id].id)
def mexican_voice():
    change_voices(1)
    talk("hola , soy mia , ¿en que puedo ayudarte?")
def english_voice():
    change_voices(2)
    talk("hai there, its mia , ¿mey ai help iu?")
 
    

sites = {"google" : "https://www.google.com/?hl=es",
         "youtube" : "https://www.youtube.com/",
         "colab"   : "https://colab.research.google.com/#scrollTo=wApJGNfBGvPG",
         "gmail"  : "https://mail.google.com/mail/u/0/?hl=es#inbox",
         "campus virtual" : "https://campusvirtual.ugc.edu.co/virtual/login/index.php",
         "whatsapp" : "https://web.whatsapp.com/"
         }

#files = {
      
#}

#creamos variables de nombres y las demas para inciar la paqueteria y la funcion de reconocer voz
name = "mia"
listener = sr.Recognizer()
engine = pyttsx3.init()

#elegimos el idioma de la voz donde de una lista de dos elementos el indice 0 es el español
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

#creamos la funcion talk de hablar  
def talk(text):
    engine.say(text)
    engine.runAndWait()
    
def read_and_talk():
    text = Texto_info.get("1.0", "end")
    talk(text)

def write_text(text_wiki):
    Texto_info.insert(INSERT,text_wiki)
    
    

def listen2():
    try:
        with sr.Microphone() as source:
            talk("Hola, soy Mia. ¿En qué puedo ayudarte?")
            pc = listener.listen(source)
            rec2 = listener.recognize_google(pc,language="es")
            rec2 = rec2.lower()
            if name in rec2:
                rec2= rec2.replace(name,'')
            else:
               pass
            
    
    except:
        pass
    return rec2

#la funcion listen permite abrir el microfono y con la variable listener para que pueda reconocer el texto
#creamos una condicion para que reconozca que se activa con el nombre mia 
def listen():
    try:
        with sr.Microphone() as source:
            talk("Hola, soy Mia. ¿En qué puedo ayudarte?")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc,language="es")
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name,'')
            else:
               pass
            
    
    except:
        pass
    return rec 
      
      
#la funcion run_mia permite que ella tome accion dependiendo de lo que escucho   
def run_mia():
    while True:
     rec = listen()
     if 'reproduce' in rec:
        music = rec.replace("reproduce",'')
        print("reproduciendo " + music)
        talk("reproduciendo" + music)
        pywhatkit.playonyt(music)
     elif 'busca' in rec:
         print(rec)
         search = rec.replace('busca','')   
         wikipedia.set_lang('esp')
         wiki = wikipedia.summary(search,1)
         write_text(search +":"+ wiki)
         talk(wiki)
         break
     elif 'alarma' in rec:
         num = rec.replace("alarma",'')
         num = num.strip()
         talk("alarma puesta para las "+num+" horas" )
         print(rec)
         while True:
           if datetime.datetime.now().strftime('%H:%M') == num:
             print("DESPIERTAAA")
             mixer.init()
             mixer.music.load("asistente_virtual/utomp3.com - Alexa timer sound.mp3")
             mixer.music.play()
             if keyboard.read_key() == "s":
                mixer.music.stop()
                break
         else:
             print("no sirvio")
             break
     elif 'colores' in rec:
         talk('enseguida')
         colors.capture()
         
     elif "termina" in rec:
         break 
     elif 'abre' in rec:
         for site in sites:
             if site in rec:
                 sub.call(f'start chrome.exe {sites[site]}',shell=True)
                 talk(f'abriendo {site}')
     elif 'pon sabor navideño' in rec: 
             talk("reproduciendo sabor navideño de afrosound")
             musica_lista = ["asistente_virtual/Sabor Navideño  - Afrosound ( Video Oficial )  - Discos Fuentes.mp3","asistente_virtual/utomp3.com - Feliz NocheBuena  Rodolfo Aicardi  Discos Fuentes.mp3","asistente_virtual/Amaneciendo  - Adolfo Echeverria y Su Conjunto  ( Video Oficial ) - Discos Fuentes.mp3","asistente_virtual/Soundtrack (S3E5) #27 - Para la Luna - Narcos (2017).mp3","asistente_virtual/Manguito Biche, Diomedes Díaz - Letra Oficial.mp3"]
             mixer.init()
             mixer.music.load(musica_lista[0])
             mixer.music.play()
             time.sleep(6)
             rec2 = listen2()
             if "termina" in rec2:
                 mixer.music.stop()
                 break
     elif "pon feliz noche buena" in rec:
             talk("reproduciendo feliz noche buena de rodolfo aicardi")
             musica_lista = ["asistente_virtual/Sabor Navideño  - Afrosound ( Video Oficial )  - Discos Fuentes.mp3","asistente_virtual/utomp3.com - Feliz NocheBuena  Rodolfo Aicardi  Discos Fuentes.mp3","asistente_virtual/Amaneciendo  - Adolfo Echeverria y Su Conjunto  ( Video Oficial ) - Discos Fuentes.mp3","asistente_virtual/Soundtrack (S3E5) #27 - Para la Luna - Narcos (2017).mp3","asistente_virtual/Manguito Biche, Diomedes Díaz - Letra Oficial.mp3"]
             mixer.init()
             mixer.music.load(musica_lista[1])
             mixer.music.play()
             time.sleep(6)
             rec2 = listen2()
             if "termina" in rec2:
                 mixer.music.stop()
     elif "pon amaneciendo" in rec:
             talk("reproduciendo amaneciendo de adolfo echeverria y su conjunto")
             musica_lista = ["asistente_virtual/Sabor Navideño  - Afrosound ( Video Oficial )  - Discos Fuentes.mp3","asistente_virtual/utomp3.com - Feliz NocheBuena  Rodolfo Aicardi  Discos Fuentes.mp3","asistente_virtual/Amaneciendo  - Adolfo Echeverria y Su Conjunto  ( Video Oficial ) - Discos Fuentes.mp3","asistente_virtual/Soundtrack (S3E5) #27 - Para la Luna - Narcos (2017).mp3","asistente_virtual/Manguito Biche, Diomedes Díaz - Letra Oficial.mp3"]
             mixer.init()
             mixer.music.load(musica_lista[2])
             mixer.music.play()
             time.sleep(6)
             rec2 = listen2()
             if "termina" in rec2:
                 mixer.music.stop()
     elif "pon para la luna" in rec:
             talk("reproduciendo para la luna de los nemus")
             musica_lista = ["asistente_virtual/Sabor Navideño  - Afrosound ( Video Oficial )  - Discos Fuentes.mp3","asistente_virtual/utomp3.com - Feliz NocheBuena  Rodolfo Aicardi  Discos Fuentes.mp3","asistente_virtual/Amaneciendo  - Adolfo Echeverria y Su Conjunto  ( Video Oficial ) - Discos Fuentes.mp3","asistente_virtual/Soundtrack (S3E5) #27 - Para la Luna - Narcos (2017).mp3","asistente_virtual/Manguito Biche, Diomedes Díaz - Letra Oficial.mp3"]
             mixer.init()
             mixer.music.load(musica_lista[3])
             mixer.music.play()
             time.sleep(6)
             rec2 = listen2()
             if "termina" in rec2:
                 mixer.music.stop()
     elif "pon manguito biche" in rec:
             talk("reproduciendo manguito biche de diomedes diaz ")
             musica_lista = ["asistente_virtual/Sabor Navideño  - Afrosound ( Video Oficial )  - Discos Fuentes.mp3","asistente_virtual/utomp3.com - Feliz NocheBuena  Rodolfo Aicardi  Discos Fuentes.mp3","asistente_virtual/Amaneciendo  - Adolfo Echeverria y Su Conjunto  ( Video Oficial ) - Discos Fuentes.mp3","asistente_virtual/Soundtrack (S3E5) #27 - Para la Luna - Narcos (2017).mp3","asistente_virtual/Manguito Biche, Diomedes Díaz - Letra Oficial.mp3"]
             mixer.init()
             mixer.music.load(musica_lista[4])
             mixer.music.play()
             time.sleep(6)
             rec2 = listen2()
             if "termina" in rec2:
                 mixer.music.stop()
     elif "pon la lista de musica" in rec:
         talk("reproduciendo la lista de musica")
         mixer.init()
         mixer.music.load(musica_lista)
         mixer.music.play()
         if "termina" in rec2:
             mixer.music.stop()
         elif "siguiente cancion" or "pasa cancion":
           mixer.init()
           mixer.music.load(musica_lista[1])
           mixer.music.play()
     elif "quién eres" in rec:
         talk("soy una inteligencia artificial , creado por  el señor santiago")
         
     elif "pon maligno" in rec:
         talk("reproduciendo maligno de aterciopelados")
         mixer.init()
         mixer.music.load("asistente_virtual/Aterciopelados - Maligno (Video).mp3")
         mixer.music.play()
         rec2 = listen2()
         if "termina" in rec:
             mixer.music.stop()
             
     else: 
         talk("lo siento, no lo se ")
             
             
         
botton_voices_mex = Button(main_window,text="Voz español", fg='black',bg='#237a57',font=("Arial",14,"bold"),command= mexican_voice)
botton_voices_mex.place(x=650,y=135, width=182,height=50)

botton_voices_usa = Button(main_window,text="Voz ingles ", fg='black',bg='#EB5757',font=("Arial",14,"bold"),command= english_voice)
botton_voices_usa.place(x=650,y=245, width=164,height=50)

botton_listen = Button(main_window,text="Escuhar", fg='black',bg='#f5af19',font=("Arial",15,"bold"),width= 10, height= 2 ,command= run_mia)
botton_listen.pack(pady=10)

botton_speak = Button(main_window,text="Hablar", fg='black',bg='#f5af19',font=("Arial",15,"bold"),width= 10, height= 2 ,command= read_and_talk)
botton_speak.place(x=650,y=380, width=164,height=50)


main_window.mainloop()