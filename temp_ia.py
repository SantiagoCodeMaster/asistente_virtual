#regrersion lineal simple con tensorflow
#importamos las librerias
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import tensorflow as tf

def entrenamiento_red():
  # Lee el archivo CSV con el delimitador punto y coma
  dt_temperature = pd.read_csv("inteligencia artificial/ia/celsius_a_fahrenheit.csv", delimiter=";")

  # Convertir las columnas a listas
  celsius_values = dt_temperature['Celsius'].tolist()
  fahrenheit_values = dt_temperature['Fahrenheit'].tolist()


  #cargar un set de datos
  x_train = dt_temperature['Celsius']
  y_train = dt_temperature['Fahrenheit']

  #creando el modelo de inteligencia artificial
  model = tf.keras.Sequential()#tf.keras.Sequential lo utilizamos para crear nuestro modelo de manera secuencial capa a capa y se utiliza con keras
  model.add(tf.keras.layers.Dense(units=1,input_shape =[1]))#layers son capas y Dense son las capas mas simples que hay , de una sola neurona

  #compilado
  model.compile(optimizer = tf.keras.optimizers.Adam(1.3), loss = 'mean_squared_error')
  #entrenamiento
  epochs_hist = model.fit(x_train ,y_train,epochs=100 ) #un epochs significa que nuestra red a pasado por nuestro red de entrenamiento


  #vamos a evaluar nuestro modelo 
  epochs_hist.history.keys()
  #grafico
  plt.plot(epochs_hist.history['loss'])
  plt.title("progreso de perdida durante el modelo de entrenamiento")
  plt.xlabel("epoch")
  plt.ylabel("training loss")
  plt.legend("training loss")

  model.get_weights()
  
  return model 