import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon 

class My_GUI(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(100, 100, 500, 500)
		self.setWindowTitle('Peri')
		self.setWindowIcon(QIcon('589accad1a7ea.png'))
		button_1 = QPushButton('ЖМИ!!!!', self)
		button_1.setGeometry(50, 50, 300, 300)
		self.show()

app = QApplication(sys.argv)
my_window = My_GUI()
sys.exit(app.exec_())

