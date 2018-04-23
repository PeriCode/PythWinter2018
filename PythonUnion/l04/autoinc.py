import sqlite3

conn = sqlite3.connect('New_2.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE python_group")

cursor.execute("""CREATE TABLE IF NOT EXISTS python_group (
	id INTEGER PRIMARY KEY AUTOINCREMENT, 
	name VARCHAR(255),
	surname VARCHAR(255)
)
 """)

list_of_pupils = [('Ибрагим', 'Ибрагимов'), ('Даниял', 'Магомедов'), ('Мурад', 'Мурадов')]
# query = """INSERT INTO python_group (name) VALUES (?)"""
# cursor.execute("""INSERT INTO python_group (name, surname) VALUES ('Амир')""")
# cursor.execute("""INSERT INTO python_group (name, surname) VALUES ('Исамутдин')""")
# cursor.execute("""INSERT INTO python_group (name, surname) VALUES ('Марат')""")
cursor.executemany("""INSERT INTO python_group (name, surname) VALUES (?, ?)""", list_of_pupils)



conn.commit()
cursor.close()
conn.close()