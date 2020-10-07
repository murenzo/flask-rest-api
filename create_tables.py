import sqlite3

connection = sqlite3.connect('database.db')

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id integer primary key, username text, password text)"

cursor.execute(create_table)

connection.commit()

connection.close()
