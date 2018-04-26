from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit
import sys
import sqlite3
from random import randint

class User(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		nameText = QLabel('Введите логин', self)
		nameText.move(50, 50)
		self.log = QLineEdit(self)
		self.log.move(50, 70)
		surnameText = QLabel('Введите пароль', self)
		surnameText.move(50, 90)
		self.password = QLineEdit(self)
		self.password.move(50, 110)

		self.button = QPushButton('Зарегистрироваться',self)
		self.button.move(50, 135)
		self.button.clicked.connect(self.setForm)
		
		self.button_1 = QPushButton('Авторизоваться',self)
		self.button_1.move(50, 165)
		self.button_1.clicked.connect(self.checkForm)

		self.bet = QLineEdit(self)
		self.bet.move(50, 195)
		self.numb = QLineEdit(self)
		self.numb.move(200, 195)

		self.button_2 = QPushButton('Сделать ставку', self)
		self.button_2.move(50, 225)
		self.button_2.clicked.connect(self.makeBet)

		self.setGeometry(100, 100, 550, 550)
		self.setWindowTitle('Добро пожаловать!')
		self.show()

	def makeBet(self):
		conn = sqlite3.connect('test.db')
		cursor = conn.cursor()



	def setForm(self):
		conn = sqlite3.connect('test.db')
		cursor = conn.cursor()

		cursor.execute("DROP TABLE users")

		cursor.execute("""CREATE TABLE IF NOT EXISTS users
			(
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				login VARCHAR(30),
				password VARCHAR(30),
				score INTEGER
			)
			""")

		query = """INSERT INTO users (login, password)
		VALUES (?, ?)"""

		cursor.execute(query, (self.log.text(), self.password.text()))
		conn.commit()
		self.log.setText('')
		self.password.setText('')

		cursor.close()
		conn.close()

	def checkForm(self):
		try:
			conn = sqlite3.connect('test.db')
			cursor = conn.cursor()
		
			query = "SELECT * FROM users WHERE login='" + str(self.log.text()) + "' AND password ='" + str(self.password.text()) + "'"

			# print(query)
			cursor.execute(query)
			# print(cursor.fetchall())
			if len(cursor.fetchall()) == 0:
				print('Грустно, но вас нет в нашем списке!')
			else:
				print('Проходите милорд!')
			self.log.setText('')
			self.password.setText('')
			cursor.close()
			conn.close()
		except Exception as e:
			print('Произошла ошибка: ' + str(e))

app = QApplication(sys.argv)
my_window = User()
sys.exit(app.exec_())