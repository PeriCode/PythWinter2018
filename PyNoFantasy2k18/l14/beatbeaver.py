# Создать сетку, каждая клетка которой будет норой. 
# Клетки должны быть кликабельными.
# При нажатии на кнопку Начать запускается таймер.
# Каждый ход из одной норки выглядывает крот и ожидает заданное время.
# Игрок должен успеть "ударить" бобра. 
# В случае попадания по бобру игроку добавляются очки, а крот прячется.
# Когда выходит время, игра завершается.

import sys
import random

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

class Beat_the_beaver(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		grid = QGridLayout()
		grid.setSpacing(10)

		self.holes = []
		self.current = 0
		x, y = 0, 0
		for i in range(9):
			self.holes.append(QPushButton("0", self))
			self.holes[i].setIcon(QIcon("hole.png"))
			self.holes[i].setIconSize(QSize(200, 200))

			self.holes[i].clicked.connect(self.doAction)

			grid.addWidget(self.holes[i], x, y)
			if y < 2:
				y += 1
			else:
				x += 1
				y = 0

		self.count = 0


		self.showFace()
		self.setLayout(grid)

		self.setGeometry(50, 50, 650, 850)
		self.setWindowTitle('Бей бобра')
		self.show()

	def showFace(self):
		number = random.randint(0, 8)
		self.holes[number].setText("1")
		self.holes[number].setIcon(QIcon("beaver.png"))
		self.current = number

	def clearFace(self):
		self.holes[self.current].setText("0")
		self.holes[self.current].setIcon(QIcon("hole.png"))


	def doAction(self):
		sender = self.sender()
		if sender.text() == "1":
			self.count += 1
			self.clearFace()


app = QApplication(sys.argv)
my_window = Beat_the_beaver()
sys.exit(app.exec_())
