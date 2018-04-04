import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtWidgets import QLineEdit

class User(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		nameText = QLabel('Введите имя', self)
		nameText.move(50, 50)
		self.nameInput = QLineEdit(self)
		self.nameInput.move(50, 70)

		self.button = QPushButton('Отправить', self)
		self.button.move(50, 100)

		self.button.clicked.connect(self.sendForm)

		self.setGeometry(50, 50, 500, 500)
		self.setWindowTitle('Добро пожаловать!')
		self.show()

	def sendForm(self):
		f = open('Список пользователей.txt', 'a')
		f.write(self.nameInput.text() + '\n')
		f.close()
		self.nameInput.setText('')


app = QApplication(sys.argv)
my_window = User()
sys.exit(app.exec_())
