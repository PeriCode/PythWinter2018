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
from PyQt5.QtCore import QSize, QBasicTimer


class BeatTheSleeper(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.timer = QBasicTimer()
		self.steps = 0

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

		self.scores = QLabel("0")
		self.time = QLabel("20")
		self.startButton = QPushButton('Начать')

		grid.addWidget(self.scores, 3, 0)
		grid.addWidget(self.time, 3, 1)
		grid.addWidget(self.startButton, 3, 2)
		self.startButton.clicked.connect(self.startGame)
		
		self.setLayout(grid)
		self.setGeometry(100, 100, 850, 850)
		self.setWindowTitle('Саид бьет кротов из открытого космоса')
		self.show()


	def startGame(self):
		self.timer.start(500, self)
		self.scores.setText("0")
		self.startButton.setEnabled(False)

	def timerEvent(self, e):
		self.hideSleeper()
		self.jumpSleeper()

		if self.steps >= 40:
			self.timer.stop()
			self.startButton.setEnabled(True)
			self.time.setText("20")
			self.steps = 0
			self.hideSleeper()
			return

		self.steps += 1

		if self.steps % 2 == 0:
			temp_time = int(self.time.text()) - 1
			self.time.setText(str(temp_time))


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
			temp_scores = int(self.scores.text()) + 1
			self.scores.setText(str(temp_scores))


app = QApplication(sys.argv)
my_window = BeatTheSleeper()
sys.exit(app.exec_())

