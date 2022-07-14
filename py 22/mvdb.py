
from multiprocessing.dummy import connection
import sqlite3
# from tkinter import _Cursor

connection = sqlite3.connect('movies.db')

cursor = connection.cursor()

cursor.execute ('''CREATE TABLE IF NOT EXISTS Movies(Title TEXT, Director TEXT, Year INT'''))

connection.commit()
connection.close()





