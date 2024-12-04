#importamos las librerias
import speech_recognition as sr
import pyttsx3,pywhatkit,wikipedia,datetime,keyboard,colors,os,vision,temp_ia
from pygame import mixer
import time 
import subprocess as sub 
from tkinter import * 
from PIL import Image,ImageTk
import threading as tr
import whatsapp as whap
import database
from chatterbot import ChatBot
from chatterbot import preprocessors
from chatterbot.trainers import ListTrainer 
import cv2
from datetime import datetime
import pytz
import locale
import serial

#ser = serial.Serial('COM3',9600)
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
         -conversar...(charla con ella)
"""

label_title= Label(main_window,text="Mia IA",bg='#DBE6F6',fg='#000428', font=('Arial',30,'bold'))
label_title.pack(pady=10)

canvas_comandos = Canvas(bg='#C5796D',height= 320,width=300)
canvas_comandos.place(x=0,y=0)

canvas_comandos.create_text(115,135, text = comandos,fill = 'black',font ='Arial 10')

Texto_info = Text(main_window,bg='#ff9068',fg = "black")
Texto_info.place(x=0,y=320,height=280,width=300)



Mia_photo = ImageTk.PhotoImage(Image.open("foto robot.png"))
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

programs = {
     "datos": "C:\\Users\\USUARIO\\Desktop\\SPVENTA.lnk",
     "google": "",
     "pychram": "C:\\Users\\Public\\Desktop\\PyCharm Community Edition 2023.2.4.lnk"

}

#creamos variables de nombres y las demas para inciar la paqueteria y la funcion de reconocer voz
name = "mia"
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
    

#la funcion listen permite abrir el microfono y con la variable listener para que pueda reconocer el texto
def listen(prhase = None):
    listener = sr.Recognizer()
    rec = ""
    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source)
        talk(prhase)
        pc = listener.listen(source)
    try:
        rec = listener.recognize_google(pc,language="es")
        rec = rec.lower()
        print(rec)
    except sr.UnknownValueError:
        print(rec)
        talk("Tengo problemas para entenderte en este momento. Vuelve a intentarlo más tarde. puedes cerrar la pagina y volverlo abrir.")
    except sr.RequestError as e:
        print(f"could not request results from Google spechh Recognition servicie; {0}".formart(e))
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
        talk("Tengo problemas para entenderte en este momento. Vuelve a intentarlo más tarde.")
    return rec
# funciones asociadas a las palabras claves 

def reproduce(rec):
    print(rec)
    music = rec.replace("reproduce",'')
    print("reproduciendo " + music)
    talk("reproduciendo" + music)
    pywhatkit.playonyt(music)
def busca(rec):
    print(rec)
    search = rec.replace('busca','')   
    wikipedia.set_lang('esp')
    wiki = wikipedia.summary(search,1)
    write_text(search +":"+ wiki)
    talk(wiki)
    
def alarma(rec):
    print(rec)
    t = tr.Thread(target=clock,args=(rec,))
    t.start()
    
def colores(rec):
    talk('enseguida')
    colors.capture()
   

def camara(rec):
   talk("muy bien")
   vision.vision()
    
def abre(rec):
    print(rec)
    for site in sites:
        if site in rec:
            sub.call(f'start chrome.exe {sites[site]}',shell=True)
            talk(f'abriendo {site}')
    
        
def pon_sabor_navideño(rec):
    talk("reproduciendo sabor navideño de afrosound")
    musica_lista = ["asistente_virtual/Sabor Navideño  - Afrosound ( Video Oficial )  - Discos Fuentes.mp3","asistente_virtual/utomp3.com - Feliz NocheBuena  Rodolfo Aicardi  Discos Fuentes.mp3","asistente_virtual/Amaneciendo  - Adolfo Echeverria y Su Conjunto  ( Video Oficial ) - Discos Fuentes.mp3","asistente_virtual/Soundtrack (S3E5) #27 - Para la Luna - Narcos (2017).mp3","asistente_virtual/Manguito Biche, Diomedes Díaz - Letra Oficial.mp3"]
    mixer.init()
    mixer.music.load(musica_lista[0])
    mixer.music.play()
    time.sleep(6)
    
   
    
def pon_feliz_noche_buena(rec):
    talk("reproduciendo feliz noche buena de rodolfo aicardi")
    mixer.init()
    mixer.music.load("inteligencia artificial/asistente_virtual/utomp3.com - Feliz NocheBuena  Rodolfo Aicardi  Discos Fuentes.mp3")
    mixer.music.play()
    time.sleep(313)
    
    
    
def pon_amaneciendo(rec):
    talk("reproduciendo amaneciendo de adolfo echeverria y su conjunto")
    mixer.init()
    mixer.music.load("inteligencia artificial/asistente_virtual/Amaneciendo  - Adolfo Echeverria y Su Conjunto  ( Video Oficial ) - Discos Fuentes.mp3")
    mixer.music.play()
    time.sleep(330)
    
    
    
def pon_para_laluna(rec):
     talk("reproduciendo para la luna de los nemus")
     mixer.init()
     mixer.music.load("Soundtrack (S3E5) #27 - Para la Luna - Narcos (2017).mp3")
     mixer.music.play()
     time.sleep(340)
         
    
def pon_manguito_biche(rec):
    talk("reproduciendo manguito biche de diomedes diaz ")
    mixer.init()
    mixer.music.load("Manguito Biche, Diomedes Díaz - Letra Oficial.mp3")
    mixer.music.play()
    time.sleep(441)
           
    
    
def  quien_eres(rec):
    talk("soy una inteligencia artificial , creado por  el señor santiago")
      
      
def clock(rec):
    num = rec.replace('alarma','')
    num = num.strip()
    talk("alarma , configurada para las" + num + "horas")
    if num[0] != '0' and len(num) < 5:
        num = '0' + num
    print(num)
    while True:
           if datetime.datetime.now().strftime('%H:%M') == num:
             print("DESPIERTAAA")
             mixer.init()
             mixer.music.load("asistente_virtual/utomp3.com - Alexa timer sound.mp3")
             mixer.music.play()
           else:
               continue
           if keyboard.read_key() == "s":
               mixer.music.stop()
               break
def saludo(rec):
    talk("como te encuentras el dia de hoy, espero tengas un bonito dia")
            

def cierra(rec):
    for taks in programs:
        kill_task = programs[taks].split('\\')
        kill_task = kill_task[-1]
        if taks in rec:
            sub.call(f'TASKKILL /IM {kill_task} /F',shell = True)
            talk(f"cerrando{taks}")
        
        if 'todo' in rec:
            sub.call(f'TASKKILL /IM {kill_task} /F',shell = True)
            talk(f"cerrando{taks}")
            
    if 'ciérrate' in rec:
        sub.call(f'TASKKILL /IM  inteligencia artificial/asistente_virtual/mia_gui.py.exe  /F',shell = True)
        talk('adios')
        
def serenata_amor(rec):
    talk("reproduciendo,serenata de amor de jaime Echeverria")
    mixer.init()
    mixer.music.load("y2mate.com - Jaime R  Echavarria    Serenata de amor.mp3")
    time.sleep(409)
    
def conversar(rec):
    chat = ChatBot("mia",database_uri = None)
    trainer = ListTrainer(chat)
    trainer.train(database.get_question_answer())
    talk('¡Hola! ¿En qué puedo ayudarte hoy?')
    while True:
        try:
            request = listen("")
        except UnboundLocalError:
            talk("lo siento,no te entendi ")
            continue
        print('tu' + request)
        answer = chat.get_response(request)
        print("mia: " ,answer)
        talk(answer)
        if "chao" in request:
            break
        

    
def pico_placa(rec):
   fecha_actual = datetime.now()
   dia_actual = fecha_actual.day
   talk("dime,el ultimo digito, de tu placa")
   placa = int(input("dime el ultimo digito de tu placa: "))
   if placa >= 10 or placa < 0:
        talk("error , pusiste el numero mal")
   elif placa == 6 or  placa == 7 or placa == 8 or placa == 9 or placa == 0 : 
        if dia_actual % 2 == 0:
          talk("hoy puedes sacar el carro , no tienes pico y placa")
        else:
          talk("no saques el carro , hoy tienes pico y placa")
   elif placa == 1 or placa == 2 or placa == 3 or placa == 4 or placa == 5:
        if dia_actual % 2 != 0:
           talk("hoy puedes sacar el carro , no tienes pico y placa")
        else:
           talk("no saques el carro , hoy tienes pico y placa")
   else:
      talk("error, pusiste el numero mal")
      
def dia(rec):
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    fecha = datetime.now().strftime("%d de %B de %Y").lstrip('0')
    talk(f"hoy es {fecha}")
    


def hora(rec):
    zona_horaria_bogota = pytz.timezone('America/Bogota')
    hora_actual = datetime.now(zona_horaria_bogota).strftime("%H:%M")
    talk(f"son las {hora_actual}")
    
def serial_leds(val):
    try:
      data = str(val).encode()
      ser.write(data)
    except NameError:
        talk("luces led, no responden, verifica la fuente de , energia del dispositivo")
    

def leds(rec):
    if 'prende' in rec:
        talk('muy bien...')
        serial_leds(1)
    elif 'apaga' in rec:
        talk('muy bien...')
        serial_leds(0)
    
def buenos_dias(rec):
    talk("buenos dias, señor santiago")
    serial_leds(1)
    zona_horaria_bogota = pytz.timezone('America/Bogota')
    hora_actual = datetime.now(zona_horaria_bogota).strftime("%H:%M")
    talk(f"son las {hora_actual}")

def temp_unid(rec):
    talk("pasar los grados Fahrenheit. a grados centígrados. dime los grados en Fahrenheit")
    try:
     Temp_c = int(input(" dime los grados en Fahrenheit: "))
     model = temp_ia.entrenamiento_red()
     Temp_F = model.predict([Temp_c])
     talk(f"{Temp_c} grados Fahrenheit, a grados centígrados es {Temp_F} grados centígrados")
    except ValueError:
        talk("Error, el numero ingresado. no es valido")


    

  
    
#diccionario de palabras claves para su funcion              
key_words = {
    'reproduce' : reproduce, 
    'busca' : busca,# X
    'alarma' : alarma, # X
    'colores' : colores, 
    'abre' : abre, 
    'pon sabor navideño': pon_sabor_navideño, 
    'pon feliz noche buena' : pon_feliz_noche_buena,
    'pon amaneciendo' : pon_amaneciendo,  
    'pon para la luna' : pon_para_laluna,
    'pon manguito biche' : pon_manguito_biche, 
    'quién eres' : quien_eres,
    'hola' : saludo,
    'cerrar' : cierra, #X
    'serenata de amor' : serenata_amor,
    'abre cámara' : camara, 
    'conversar' :conversar, 
    'pico y placa' : pico_placa,
    'qué día es hoy': dia,
    'qué hora es' : hora,
    'qué horas son' : hora,
    'prende' : leds,
    'apaga' : leds ,
    'buenos días': buenos_dias,
    'temperatura': temp_unid,
}


#la funcion run_mia permite que ella tome accion dependiendo de lo que escucho   
def run_mia():
    while True:
        rec = listen("hola, soy mia , en que puedo ayudarte")
        if 'busca' in rec:
            key_words['busca'](rec)
            break
        else: 
            for word in key_words:
                if word in rec:
                    key_words[word](rec)
        if 'para' in rec:
            talk("hasta, la vista!")
            break
        
              
    main_window.update()
     

     
botton_voices_contacts= Button(main_window,text="agregar contacto", fg='black',bg='#237a57',font=("Arial",14,"bold"),command= mexican_voice)
botton_voices_contacts.place(x=650,y=135, width=182,height=50)

botton_voices_usa = Button(main_window,text="Voz ingles ", fg='black',bg='#EB5757',font=("Arial",14,"bold"),command= english_voice)
botton_voices_usa.place(x=650,y=245, width=164,height=50)

botton_listen = Button(main_window,text="Escuhar", fg='black',bg='#f5af19',font=("Arial",15,"bold"),width= 10, height= 2 ,command= run_mia)
botton_listen.pack(pady=10)

botton_speak = Button(main_window,text="Hablar", fg='black',bg='#f5af19',font=("Arial",15,"bold"),width= 10, height= 2 ,command= read_and_talk)
botton_speak.place(x=650,y=380, width=164,height=50)



main_window.mainloop()