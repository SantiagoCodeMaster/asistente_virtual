import cv2
import os 
import threading as tr 
import subprocess as sub
import winsound
import imutils
from pygame import mixer


data_path = "C:\\Users\\USUARIO\\Desktop\\pyhton\\.vscode\\inteligencia artificial\\asistente_virtual\\Data_Face"
image_paths = os.listdir(data_path)

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('inteligencia artificial/asistente_virtual/LBHFaceModel.xml')

face_classif = cv2.CascadeClassifier("inteligencia artificial/asistente_virtual/haarcascade_frontalface_default.xml")

def face_rec(state):
    capture = cv2.VideoCapture(0)
    while True:
       comp,frame = capture.read()
       if comp == False: 
           break
       frame = imutils.resize(frame,width=640)
       #convertir el fotograma a escala de grises
       gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
       aux_frame = frame.copy()
    
       faces = face_classif.detectMultiScale(gray,1.3,5)
    
       for (x,y,w,h) in faces:
           face = aux_frame[y:y+h,x:x+w]
           face = cv2.resize(face,(150,150),interpolation=cv2.INTER_CUBIC)
           
           # Convertir la cara a escala de grises antes de la predicción
           face_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

           result = face_recognizer.predict(face_gray)
           
           cv2.putText(frame,f'{result}',(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
           
           if result[1] < 76:
               cv2.putText(frame,"Santi",(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
               cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
               
           else:
               #thread_alarma_song(0)
               cv2.putText(frame,f"desconocido",(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
               cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
               
       cv2.imshow('frame',frame)
       if cv2.waitKey(1) & 0xFF == ord('s'):
           break
           cap.release()
           cv2.destroyAllWindows()
           sub.call(f'taskkill / IM python.exe /F', shell = True)
           
def alarma_song(state):
    mixer.music.load("inteligencia artificial/asistente_virtual/utomp3.com - Alexa timer sound.mp3")
    if state == 0:
        winsound.PlaySound("alarmaa.wav",winsound.SND_FILENAME)

def thread_alarma_song(state):
    ta = tr.Thread(target=alarma_song,args=(state, ))
    ta.start()
    
face_rec(0)
       
               
               
    
