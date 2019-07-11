from PyQt5.QtWidgets import * #QMainWindow, QAction, qApp, QApplication, QPushButton, QToolBar, QTableWidget,QTableWidgetItem, QInputDialog, QLineEdit,QLabel
from PyQt5.QtGui import *
import sys


class Example(QMainWindow,QPushButton, QToolBar, QIcon, QTableWidget, QTableWidgetItem,QLabel):

    def __init__(self):

        super().__init__()

        self.setGeometry(0, 0, 1400, 1050)
        self.setWindowTitle('E-Library')

        label = QLabel(self)
        pixmap = QPixmap('IMG_8205.JPG')
        label.setPixmap(pixmap)
        #label.move(100,100)
        label.resize(pixmap.width(),pixmap.height())

        # Optional, resize window to image size
        #self.resize(pixmap.width(),pixmap.height())
        self.show()
        # ################################toolBar#################################
        # usb = QAction(QIcon('Usb.png'),'Devices',self)
        # usb.triggered.connect(self.USB)
        #
        #
        # self.toolBar = self.addToolBar('MainToolBar')
        # self.toolBar.addAction(usb)
        # self.toolBar.addAction('Batata')
        #
        #
        #
        #
        # #################################Table##################################
        #
        #
        # self.table = QTableWidget(self)  # Create a self.table
        # self.table.setColumnCount(3)     #Set three columns
        # self.table.setRowCount(1)        # and one row
        # # Set the self.table headers
        # self.table.setHorizontalHeaderLabels(["Title", "Path", "Language"])
        #
        # #Set the tooltips to headings
        # self.table.horizontalHeaderItem(0).setToolTip("Title")
        # self.table.horizontalHeaderItem(1).setToolTip("Path")
        # self.table.horizontalHeaderItem(2).setToolTip("Language")
        #
        # # Do the resize of the columns by content
        # self.table.resizeColumnsToContents()
        # self.table.move(150,50)
        # self.table.resize(1100,675)




if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
