import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon

class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(30, 50, 400, 400)
		self.setWindowTitle('USSR')
		self.setWindowIcon(QIcon('ussr_640.png'))
		my_but = QPushButton('Нажми на меня', self)
		my_but.move(100,100) 
		self.show()

app = QApplication(sys.argv)
my_window = Example()
sys.exit(app.exec_())
