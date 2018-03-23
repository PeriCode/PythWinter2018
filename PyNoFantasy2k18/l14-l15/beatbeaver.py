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
from PyQt5.QtCore import QSize, QBasicTimer

class Beat_the_beaver(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.timer = QBasicTimer()
		self.step = 0

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

		self.count = QLabel('0')
		self.time = QLabel('30')
		self.runButton = QPushButton('Начать')

		grid.addWidget(self.count, x + 1, 0)
		grid.addWidget(self.time, x + 1, 1)
		grid.addWidget(self.runButton, x + 1, 2)

		self.runButton.clicked.connect(self.startGame)

		self.setLayout(grid)

		self.setGeometry(50, 50, 650, 850)
		self.setWindowTitle('Бей бобра')
		self.show()


	def startGame(self):
		self.timer.start(500, self)
		self.count.setText("0")
		self.runButton.setEnabled(False)
		self.time.setText("30")

	def timerEvent(self, e):
		self.clearFace()
		self.showFace()

		if self.step >= 60:
			self.timer.stop()
			self.step = 0
			self.clearFace()
			return

		self.step += 1

		if self.step % 2:
			temp_time = int(self.time.text()) - 1
			self.time.setText(str(temp_time))

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
			# self.count += 1
			temp_count = int(self.count.text()) + 1
			self.count.setText(str(temp_count))
			self.clearFace()


app = QApplication(sys.argv)
my_window = Beat_the_beaver()
sys.exit(app.exec_())
