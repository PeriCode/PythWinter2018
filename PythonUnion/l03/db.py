import sqlite3

con = sqlite3.connect('test.db') # подключаемся к БД
cursor = con.cursor() # создаем бегунок
cursor.execute("""
	DROP TABLE Heroes
	""") # делаем запрос на удаление таблицы Heroes

cursor.execute("""
	CREATE TABLE Heroes (
	id INT,
	name TEXT,
	country TEXT,
	role TEXT)
""") # делаем запрос на создание таблицы Heroes

cursor.execute("""INSERT INTO Heroes VALUES (
	1,
	'Прометей',
	'Древняя Греция',
	'Принес огонь людям')
	""") # делаем запрос на добавление одной строки

data_list = [(2, 'Гарри Поттер', 'Англия', 'Убил Волан-Де-морта'),
(3, 'Фродо', 'Шир', 'Спас Средиземье'),
(4, 'Моисей', 'Египет', 'Спас евреев от рабства')
]

cursor.executemany("""INSERT INTO Heroes VALUES 
	(?, ?, ?, ?)""", data_list) # запрос на добавление нескольких строк

cursor.execute("SELECT * FROM Heroes") # делаем запрос на вывод всей таблицы 
print(cursor.fetchall()) # вывод на экран содержимого таблицы
con.commit() # сохраняем изменения
cursor.close() # завершаем работу курсора
con.close() # завершаем работу с БД