import sqlite3

conn = sqlite3.connect('New.db')
cursor = conn.cursor()

cursor.execute("""DROP TABLE books""")

cursor.execute(""" CREATE TABLE IF NOT EXISTS books (
	id INTEGER, 
	title VARCHAR(255), 
	author VARCHAR(50),
	year INTEGER(4)
)
 """)
cursor.execute("""
INSERT INTO books VALUES (
1, 'Оно', 'Стивен Кинг', 1986)
	""")

list_of_books = [(2, 'Идиот', 'Достоевский', 1868),
(3, 'Бойцовский клуб', 'Чак Паланик', 1985)]
cursor.executemany("""INSERT INTO books VALUES
	(?, ?, ?, ?)""", list_of_books)

query = """INSERT INTO books VALUES (?, ?, ?, ?)"""
query_info = (4, "Книжный вор", "Маркус Зузак", 2005)
cursor.execute(query, query_info)

cursor.execute("""SELECT * FROM books""")
cursor.execute("""SELECT title  FROM books""")
cursor.execute("""SELECT title, year FROM books WHERE year = 2005""")
cursor.execute("""SELECT  title, author FROM books 
	WHERE year<2000 AND year>1900 ORDER BY year DESC LIMIT 1""")

print(cursor.fetchall())

cursor.execute("""UPDATE books 
	SET year = 1996 
	WHERE title = 'Бойцовский клуб'
""")

cursor.execute("DELETE FROM books WHERE author = 'Достоевский'")

conn.commit()
cursor.close()
conn.close()