import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QPushButton, QToolBar, QTableWidget,QTableWidgetItem, QInputDialog, QLineEdit, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QImage, QImageReader

import os
import time
import getpass
import subprocess
import mysql.connector #Needs to be installed via pip
from random import randint
from termcolor import colored


#mysql settings
eLib = mysql.connector.connect(host = 'localhost', user = 'root', password = 'P3dr0mysql', database = 'eLib', connect_timeout = 86400) #The time out is to ensure the connection will live for at least a day
myCursor = eLib.cursor(buffered=True)


class Example(QMainWindow,QPushButton, QToolBar, QIcon, QTableWidget, QTableWidgetItem, QLabel, QPixmap, QImage):
    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()



        self.setGeometry(0, 0, 1400, 1050)
        self.setWindowTitle('E-Library')

        #For some reason we need to create and display an image
        self.img = QImage("/Users/pedrocruz/Desktop/Quintessential_Quintuplest-_Cover.jpg")
        self.label = QLabel(self)


        self.label.setPixmap(QPixmap(self.img).scaledToWidth(1000))
        self.label.resize(1000,200)
        self.label.move(100,100)

        TitleBtn = QPushButton('Title',self)
        TitleBtn.move(0,50)
        TitleBtn.resize(150,50)
        TitleBtn.clicked.connect(self.potato)


        #self.label.move(0,100)

        self.show()

    def potato(self):

        print('potato')
        self.img = QImage("/Users/pedrocruz/Desktop/IMG_8205.JPG")

        # self.label = QLabel(self)

        self.label.setPixmap(QPixmap(self.img).scaledToWidth(1000))
        self.label.resize(1000,200)
        self.label.move(100,100)
        QApplication.processEvents()

        #Uses the setGeometry function as a means of updating the Window
        self.setGeometry(0, 0, 1400, 1050)








if __name__ == '__main__':

    app = QApplication(sys.argv)
    # app.setStyle('Windows')
    ex = Example()
    sys.exit(app.exec_())
