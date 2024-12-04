#importa los datos 
import tensorflow as tf
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

# Generar datos simulados
np.random.seed(0)

# Número de datos a generar
num_datos = 1000

# Área en metros cuadrados
area = np.random.randint(50, 300, num_datos)

# Número de habitaciones
num_habitaciones = np.random.randint(1, 6, num_datos)

# Número de baños
num_banos = np.random.randint(1, 4, num_datos)

# Ubicación geográfica (convertir a números)
ubicacion_dict = {'Bogotá': 0, 'Medellín': 1, 'Cali': 2, 'Barranquilla': 3}
ubicacion = np.random.choice(list(ubicacion_dict.values()), num_datos)

# Año de construcción
anio_construccion = np.random.randint(1970, 2022, num_datos)

# Estado de conservación (convertir a números)
estado_conservacion_dict = {'Nuevo': 0, 'Bueno': 1, 'Regular': 2, 'Para remodelar': 3}
estado_conservacion = np.random.choice(list(estado_conservacion_dict.values()), num_datos)

# Amenidades cercanas
amenidades = np.random.randint(0, 3, num_datos)

# Tamaño del terreno (en caso de casas)
tamano_terreno = np.random.randint(100, 1000, num_datos)

# Nivel de seguridad del área
nivel_seguridad = np.random.randint(1, 6, num_datos)

# Precio (variable dependiente)
precio = 1000 * area + 5000 * num_habitaciones + 3000 * num_banos + 15000 * amenidades + 2000 * tamano_terreno + 5000 * nivel_seguridad + np.random.normal(0, 100000, num_datos)

# Crear DataFrame
datos = pd.DataFrame({
    'Area': area,
    'Num_Habitaciones': num_habitaciones,
    'Num_Banos': num_banos,
    'Ubicacion': ubicacion,
    'Anio_Construccion': anio_construccion,
    'Estado_Conservacion': estado_conservacion,
    'Amenidades': amenidades,
    'Tamano_Terreno': tamano_terreno,
    'Nivel_Seguridad': nivel_seguridad,
    'Precio': precio
})

# Visualizar los primeros datos
print(datos.head())

# Gráfico de dispersión para algunas variables
plt.figure(figsize=(10, 6))
plt.scatter(datos['Area'], datos['Precio'], alpha=0.5)
plt.title('Precio vs Área del inmueble')
plt.xlabel('Área del inmueble (m²)')
plt.ylabel('Precio (COP)')
plt.show()
#correlaccion 
f,ax = plt.subplots(figsize =(20,20))
sns.heatmap(datos.corr(), annot=True)
plt.show()


#limpieza de los datos 
selected_features = ['Area','Num_Habitaciones','Num_Banos', 'Ubicacion','Anio_Construccion','Estado_Conservacion','Amenidades','Tamano_Terreno','Nivel_Seguridad','Precio']

X = datos[selected_features]
Y = datos['Precio']

scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(X)

#Normalizando output
Y = Y.values.reshape(-1,1)
Y_scaled = scaler.fit_transform(Y)


#entrenamiento
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x_scaled, Y_scaled, test_size = 0.25)


#definiedno modelo
modelo = tf.keras.applications()
modelo.add(tf.keras.layers.Dense(units=100, activation='relu', input_shape=(4, )))
modelo.add(tf.keras.layers.Dense(units=100, activation='relu'))
modelo.add(tf.keras.layers.Dense(units=100, activation='relu'))
modelo.add(tf.keras.layers.Dense(units=1, activation='linear'))

#compilar 
modelo.compile(optimizer='Adam', loss='mean_squared_error')
epochs_hist = modelo.fit(X_train, y_train, epochs = 100, batch_size = 50, validation_split = 0.2)

#evaluando modelo
epochs_hist.history.keys()

#Grafico
plt.plot(epochs_hist.history['loss'])
plt.plot(epochs_hist.history['val_loss'])
plt.title('Progreso del Modelo durante Entrenamiento')
plt.xlabel('Epoch')
plt.ylabel('Training and Validation Loss')
plt.legend(['Training Loss', 'Validation Loss'])

#prediccion
#Definir Hogarr por predecir con suuus respectivbas etnradas / inputs
#'Area','Num_Habitaciones','Num_Banos', 'Ubicacion','Anio_Construccion','Estado_Conservacion','Amenidades','Tamano_Terreno','Nivel_Seguridad','Precio'
X_test_1 = np.array([[ 1920, 7, 3, 2,2001,1,34,123,6]])

scaler_1 = MinMaxScaler()
X_test_scaled_1 = scaler_1.fit_transform(X_test_1)


#Haciendo prediccion
y_predict_1 = modelo.predict(X_test_scaled_1)


#Revirtiendo Escalado para apreciar el precio correctamente escalado
y_predict_1 = scaler.inverse_transform(y_predict_1)
print(f"el precio de la casa con estas caracteristicas es de {y_predict_1} de  pesos" )