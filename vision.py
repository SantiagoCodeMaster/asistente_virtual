#importamos la librerias
import cv2
import numpy as np

#modos de ejecuccion
#0 = 48 #captura de video
#1 = 49 # filtro desenfoque
#2 = 50 # filtro detector de esquina
#3 = 51 # filtro de bordes

#parametros para detectar esquinas
esquinas_para = dict(maxCorners = 500,
                     qualityLevel = 0.2,
                     minDistance = 15,
                     blockSize = 9)


def vision():
  #modo
  modo = 48

  cap = cv2.VideoCapture(0)

  while True:
      ret,frame = cap.read()
      #captura de video normal tecla 0
      if modo == 48:
          resultado = frame
      #se ejecuta el desenfoque tecla 1
      elif modo == 49:
          resultado = cv2.blur(frame,(13,13))
      #bordes tecla 3
      elif modo == 51:
          resultado = cv2.Canny(frame,135,150)

      #esquinas tecla 2
      elif modo == 50:
          resultado = frame
          gray = cv2.cvtColor(frame,cv2.COLOR_BGRA2GRAY)
          esquinas = cv2.goodFeaturesToTrack(gray,**esquinas_para)
          #preguntamos si detectamos esquinas con esas caracteristicas
          if esquinas is not None:
              for x,y in np.float32(esquinas).reshape(-1,2):
                  #convertir en enteros
                  x,y = int(x),int(y)
                  cv2.circle(resultado,(x,y),10,(0,0,225),1)

      elif modo != 48 and modo != 49 and modo != 50 and modo != 51 and modo != -1:
          #no se hace nada
          resultado = frame
          print("Tecla incorrecta")

      #mostramos los framse
      cv2.imshow("VIDEOCAPTURA" , resultado)
      t = cv2.waitKey(1)
      if t == 27:
         break

      elif  t  != -1:
         modo = t

  cap.release()
  cv2.destroyAllWindows()
