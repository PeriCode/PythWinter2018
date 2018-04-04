import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtWidgets import QLineEdit, QVBoxLayout
from PyQt5.QtCore import QSize

class User(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		layout = QVBoxLayout(self)
		nameText = QLabel('Введите имя', self)
		# nameText.move(50, 50)
		self.nameInput = QLineEdit(self)
		# self.nameInput.move(50, 70)

		self.button = QPushButton('Отправить', self)
		# self.button.move(50, 100)
		
		self.loginText = QLabel('', self)
		# self.loginText.move(50, 150)

		self.button.clicked.connect(self.sendForm)


		layout.addWidget(nameText)
		layout.addWidget(self.nameInput)
		layout.addWidget(self.button)
		layout.addWidget(self.loginText)
		self.setGeometry(50, 50, 500, 500)
		self.setWindowTitle('Добро пожаловать!')
		self.show()

	def sendForm(self):
		f = open('Список пользователей.txt', 'r')
		list_of_names = f.read()
		if self.nameInput.text() in list_of_names:
			self.loginText.setText('Добро пожаловать')
		else:
			self.loginText.setText('Вас нет в списке')
		f.close()
		self.nameInput.setText('')


app = QApplication(sys.argv)
my_window = User()
sys.exit(app.exec_())