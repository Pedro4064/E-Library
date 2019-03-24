from PyQt5.QtWidgets import * #QMainWindow, QAction, qApp, QApplication, QPushButton, QToolBar, QTableWidget,QTableWidgetItem, QInputDialog, QLineEdit,QLabel
from PyQt5.QtGui import *
import sys


class Example(QMainWindow,QPushButton, QToolBar, QIcon, QTableWidget, QTableWidgetItem,QLabel):

    def __init__(self):

        super().__init__()

        self.setGeometry(0, 0, 50, 100)
        self.setWindowTitle('brary')

        self.img = QImage("/Users/pedrocruz/Desktop/IMG_8205.JPG")

        self.label = QLabel(self)

        self.label.setPixmap(QPixmap(self.img))
        self.label.resize(100,200)
        self.show()




if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
