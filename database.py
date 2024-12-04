import sqlite3
import os

# Obtener la ruta completa al archivo de la base de datos
db_file_path = r"C:\Users\USUARIO\Desktop\pyhton\.vscode\inteligencia artificial\asistente_virtual\Brain.db"

#creamos conexion a la ruta de la base de datos 
def create_connection():
    connection = sqlite3.connect(db_file_path)
    return connection

#accedemos alas tablas si question no existe, (esto porque no reconoce el nombre de la tabla)
def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS question (
            id INTEGER PRIMARY KEY,
            pregunta TEXT,
            respuesta TEXT
        )
    ''')
    connection.commit()
    connection.close()

def get_table():
    create_table()  # Asegurar que la tabla existe
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM question')
    return cursor.fetchall()

bot_list = []
def get_question_answer():
    rows = get_table()
    for row in rows:
        print(row)
        bot_list.extend(list(row))  
    
    return bot_list
    

