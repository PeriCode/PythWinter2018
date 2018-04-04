import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QLineEdit, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

        # self.lbl = QLabel(self)
        self.qle = QLineEdit(self)

        self.qle.move(60, 60)
        runButton = QPushButton('Начать', self)
        runButton.move(100, 100)

        # self.lbl.move(60, 40)

        # qle.textChanged[str].connect(self.onChanged)
        runButton.clicked.connect(self.startGame)

        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('QLineEdit')
        self.show()


    # def onChanged(self, text):

        # self.lbl.setText(text)
        # self.lbl.adjustSize()

    def startGame(self):
        self.qle.setText('')
        f = open('text.txt', 'w')
        f.write(self.qle.text())
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())