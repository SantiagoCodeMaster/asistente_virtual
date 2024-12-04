import sqlite3


def create_connection():
    connection = sqlite3.connect("Brain")
    return connection

def get_table():
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
        
get_question_answer() 