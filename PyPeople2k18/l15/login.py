from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit
import sys

class User(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		nameText = QLabel('Введите имя', self)
		nameText.move(50, 50)
		self.nameInput = QLineEdit(self)
		self.nameInput.move(50, 70)
		surnameText = QLabel('Введите фамилию', self)
		surnameText.move(50, 90)
		self.surnameInput = QLineEdit(self)
		self.surnameInput.move(50, 110)

		self.button = QPushButton('Войти',self)
		self.button.move(50, 135)
		self.button.clicked.connect(self.setForm)


		self.setGeometry(100, 100, 550, 550)
		self.setWindowTitle('Добро пожаловать!')
		self.show()

	def setForm(self):
		f = open('User list.txt')
		user_info = self.nameInput.text() + ' ' + self.surnameInput.text() + ';'
		text = f.read()
		if user_info in text:
			print('Добро пожаловать')
		else:
			print('Вас нет в списке')
		f.close()
		self.nameInput.setText('')
		self.surnameInput.setText('') 

app = QApplication(sys.argv)
my_window = User()
sys.exit(app.exec_())