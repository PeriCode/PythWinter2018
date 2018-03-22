# Создается 9 лунок
# В одной из них с определенной частотой рандомно появляется крот
# Игрок за отведенное время должен попасть по максимальному
# количеству кротов
# За каждое попадание по кроту игроку начисляются очки

import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QGridLayout, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

class BeatTheSleeper(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.last = 0
		self.scores = 0

		grid = QGridLayout()
		grid.setSpacing(10)

		self.holes = []
		x, y = 0, 0
		for i in range(9):
			self.holes.append(QPushButton("Unactive", self))
			self.holes[i].setIcon(QIcon("hole.png"))
			self.holes[i].setIconSize(QSize(200, 200))

			self.holes[i].clicked.connect(self.doAction)

			grid.addWidget(self.holes[i], x, y)
			if y < 2:
				y += 1
			else:
				x += 1
				y = 0

		self.jumpSleeper()
		
		self.setLayout(grid)
		self.setGeometry(100, 100, 650, 650)
		self.setWindowTitle('Саид бьет кротов из открытого космоса')
		self.show()


	def jumpSleeper(self):
		number = randint(0, 8)
		self.holes[number].setIcon(QIcon("sleeper.png"))
		self.holes[number].setText("Active")
		self.last = number

	def hideSleeper(self):
		self.holes[self.last].setIcon(QIcon("hole.png"))
		self.holes[self.last].setText("Unactive")

	def doAction(self):
		sender = self.sender()
		if sender.text() == "Active":
			self.hideSleeper()
			self.scores += 1


app = QApplication(sys.argv)
my_window = BeatTheSleeper()
sys.exit(app.exec_())

