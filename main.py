from PyQt5.QtGui import QPainter, QColor, QPen
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randrange
from UI import Ui_MainWindow


class Flag(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.p = False
        self.bu.clicked.connect(self.run)
        self.show()

    def paintEvent(self, event):
        if self.p:
            qp = QPainter()
            qp.begin(self)
            for i in range(randrange(1, 11)):
                x = randrange(1, self.width())
                y = randrange(1, self.height())
                d = randrange(1, min(self.height(), self.width()))
                qp.setPen(QPen(QColor(randrange(0, 255), randrange(0, 255), randrange(0, 255))))
                qp.drawEllipse(x, y, d, d)
            qp.end()
            self.p = False

    def run(self):
        self.p = True
        self.update()


app = QApplication(sys.argv)
ex = Flag()
ex.show()
sys.exit(app.exec_())