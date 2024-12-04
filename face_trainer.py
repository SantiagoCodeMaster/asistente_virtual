import cv2 
import os
import numpy as np 

data_path = 'inteligencia artificial/Data_Face'
people =os.listdir(data_path)
print(people)
labels = []
faces_data = []
label = 0

for person in people:
    person_path = data_path + "/" + person
    print("leyendo imagenes")
    for file_name in os.listdir(person_path):
        print('Faces: ' ,person + '/' + file_name)
        labels.append(label)
        faces_data.append(cv2.imread(person_path+ '/' + file_name,0))
    
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
print("Entrenando....")
face_recognizer.train(faces_data,np.array(labels))

#almacenado el modelo
face_recognizer.write('inteligencia artificial/asistente_virtual/LBHFaceModel.xml')
print('modelo almacenado')


         