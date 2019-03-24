import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QPushButton, QToolBar, QTableWidget,QTableWidgetItem, QInputDialog, QLineEdit, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QImage

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


        ################################toolBar#################################
        usb = QAction(QIcon('Usb.png'),'Devices',self)
        usb.triggered.connect(self.USB)


        self.toolBar = self.addToolBar('MainToolBar')
        self.toolBar.addAction(usb)
        self.toolBar.addAction('Batata')




        #################################Table##################################


        self.table = QTableWidget(self)  # Create a self.table
        self.table.setColumnCount(3)     #Set three columns
        self.table.setRowCount(1)        # and one row
        # Set the self.table headers
        self.table.setHorizontalHeaderLabels(["Title", "Path", "Language"])

        #Set the tooltips to headings
        self.table.horizontalHeaderItem(0).setToolTip("Title")
        self.table.horizontalHeaderItem(1).setToolTip("Path")
        self.table.horizontalHeaderItem(2).setToolTip("Language")

        # Do the resize of the columns by content
        self.table.resizeColumnsToContents()
        self.table.move(150,50)
        self.table.resize(1100,675)

        self.initUI()

    def initUI(self):

        #Set the variables
        self.lastPath = ''
        self.imgPath = ''

        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()



        self.setGeometry(0, 0, 1400, 1050)
        self.setWindowTitle('E-Library')

        TitleBtn = QPushButton('Title',self)
        TitleBtn.move(0,50)
        TitleBtn.resize(150,50)
        TitleBtn.clicked.connect(self.Title)


        GenreBtn = QPushButton('Genre',self)
        GenreBtn.move(0,100)
        GenreBtn.resize(150,50)
        GenreBtn.clicked.connect(self.byGenre)

        BookList = QPushButton('Book List',self)
        BookList.move(0,150)
        BookList.resize(150,50)
        BookList.clicked.connect(self.All)

        EditBtn = QPushButton('Edit database',self)
        EditBtn.move(0,200)
        EditBtn.resize(150,50)
        EditBtn.clicked.connect(self.Edit)

        DeleteBtn = QPushButton('Delete Book',self)
        DeleteBtn.move(0,250)
        DeleteBtn.resize(150,50)
        DeleteBtn.clicked.connect(self.Delete)

        #Display all the book names
        self.All()

        self.show()

    def USB(self):
        print('Devices menu bar button was clicked')
        kindleChoises = ("Yes","No")
        counter = 1

        os.system("clear")
        os.chdir("/Volumes/") #Change to /media/pi for the raspberry pi

        #Get the list of devices
        choices = subprocess.getoutput("ls").split("\n")

        device, ok = QInputDialog.getItem(self, 'Device', 'Choose your device', choices,0,False)
        print(device)

        path, ok = QInputDialog.getText(self, 'Path to Book', 'Path', QLineEdit.Normal, '')
        print(path)

        kindle, ok = QInputDialog.getItem(self,'Kindle','Is it a kindle Device?',kindleChoises,0,False)
        print(kindle)

        if kindle == 'Yes':
            os.system("cp %s /Volumes/%s/documents" %(path,device)) #Change the Volume direcotry in ohter unix systems
        elif kindle == 'No':
            os.system('cp %s /Volumes/"%s"' %(path,device))

        eject, ok = QInputDialog.getItem(self,'Eject','Eject Device?',('Yes','No'), 0, False)

        if eject == 'Yes':
            os.system('diskutil unmount /Volumes/"%s"'%(device)) #Change to 'umount /media/pi/nameOfDevice' in the raspberry pi
        elif eject =='No':
            print('Okay')

    def All(self):
        print('potato')
        counter = 0

        myCursor.execute("SELECT name FROM Books ORDER BY name")

        response = myCursor.fetchall()

        self.table.setRowCount(0) #Clears the existing table
        self.table.setRowCount(len(response))

        for name in response:

            self.table.setItem(counter, 0, QTableWidgetItem(''.join(name)))
            counter+=1

        myCursor.execute("SELECT path FROM Books ORDER by name")

        self.response = myCursor.fetchall()
        counter = 0

        for path in self.response: #self.response so we can access it in the ShowImage function
            self.table.setItem(counter, 1, QTableWidgetItem(''.join(path)))
            counter +=1
        #Resize the columns width to hold the whole name
        self.table.resizeColumnToContents(0)
        self.table.resizeColumnToContents(1)

        #If cell is clicked
        self.table.cellClicked.connect(self.ShowImage)

    def Title(self):

        counter = 0

        title, ok= QInputDialog.getText(self,'Search Book','Book Title', QLineEdit.Normal, '')
        print(title)

        myCursor.execute("SELECT name FROM Books WHERE name LIKE '%%%s%%' " %(title))

        response = myCursor.fetchall()

        #Clear the table
        self.table.setRowCount(0)
        self.table.setRowCount(len(response))

        #Get the name
        for name in response:
            self.table.setItem(counter, 0, QTableWidgetItem(''.join(name)))
            counter+=1

        self.table.resizeColumnToContents(0)

        #Get the path
        myCursor.execute("SELECT path FROM Books WHERE name  LIKE '%%%s%%' " %(title))

        self.response = myCursor.fetchall()
        counter = 0

        for path in response:
            self.table.setItem(counter, 1, QTableWidgetItem(''.join(path)))
            counter+=1

        self.table.resizeColumnToContents(1)
        self.response
        self.table.cellClicked.connect(self.ShowImage)

    def ShowImage(self,row,col):

        self.imgPath = ''.join(self.response[row])


        #Only change the picture if you click another cell
        if self.imgPath != self.lastPath:
            print(self.imgPath)
            #Get the path_to_cover from the database
            myCursor.execute("SELECT path_to_cover FROM Books WHERE path = '%s' " %(self.imgPath))
            paths = myCursor.fetchall()
            path_to_cover = ''.join(paths[0])
            print(path_to_cover)

            #Create and move the image QLabel
            self.img = QImage("/Users/pedrocruz/Desktop/IMG_8205.JPG")

            self.label = QLabel(self)

            self.label.setPixmap(QPixmap(self.img))
            self.label.resize(1000,2000)
            self.label.move(0,100)
            #self.label.move(0,40)
            self.show()


        self.lastPath = self.imgPath


    def Edit(self):

        password, ok = QInputDialog.getText(self,'Password','Password',QLineEdit.Normal, '')
        print(password)
        if password == '4064':
            print('Permission granted')
            name, ok = QInputDialog.getText(self,'Name','Name of the book you whish to edit',QLineEdit.Normal,'')#Send 2 variables -> 1 to name and one to ok
            info, ok = QInputDialog.getText(self,'Info','What you want to edit',QLineEdit.Normal,'')#Send 2 variables -> 1 to info and one to ok
            newInfo, ok = QInputDialog.getText(self,'New Info', 'New Info ', QLineEdit.Normal, '') #Send 2 variables -> 1 to newInfo and one to ok

            try:
                myCursor.execute("UPDATE Books SET %s=%s WHERE name = '%s' " %(info,newInfo,name)) #Tries to edit the info if it's an int
                eLib.commit()

            except:

                try:
                    print("UPDATE Books SET %s='%s' WHERE name = '%s' " %(info,newInfo,name))
                    myCursor.execute("UPDATE Books SET %s='%s' WHERE name = '%s' " %(info,newInfo,name)) #Tries to edit the info if it's a string(name,path,driverLink...)
                    eLib.commit()
                except:
                    print(colored('[ERROR] Please contact technician','red'))

        else:
            print('Wrong password') #In the future make a popup warnging

    def byGenre(self):

        genres = ["fiction",	"mystery",	"fantasy",	"science_fiction"	,"non_fiction",	"genre_fiction",	"thriller",	"romance"	,"young_adult_fiction"	,"crime_fiction",	"literary_fiction",	"horror_fiction",	"history"	,"fairy_tale",	"comic_book",	"manga"	,"light_novel"]
        genre, ok = QInputDialog.getItem(self,'Genres','Choose a Genre',genres,0,False)

        myCursor.execute('SELECT name FROM Books WHERE %s = 1 ORDER BY name'%(genre))
        response = myCursor.fetchall()

        #Cleans the table
        self.table.setRowCount(0)
        #Show all Books with the genre
        self.table.setRowCount(len(response))
        counter = 0

        for book in response:
            self.table.setItem(counter, 0, QTableWidgetItem(''.join(book)))
            counter+=1

        myCursor.execute('SELECT path FROM Books WHERE %s = 1 ORDER BY name' %(genre))
        self.response = myCursor.fetchall()
        counter = 0

        for path in self.response:
            self.table.setItem(counter,1, QTableWidgetItem(''.join(path))) #The ''.join is to format the mysqk response
            counter +=1

        self.table.resizeColumnToContents(0)
        self.table.resizeColumnToContents(1)

        self.table.cellClicked.connect(self.ShowImage)

    def Delete(self):

        password, ok = QInputDialog.getText(self,'Password', 'Password',QLineEdit.Normal,'')
        if password == '4064':
            name, ok = QInputDialog.getText(self,'Delete','Name of the Book you whish to delete',QLineEdit.Normal,'')

            answer,ok = QInputDialog.getItem(self,'WARNING','ARE YOU SURE YOU WANT TO DELTE THE BOOK ?',('YES','NO'), 0,False)

            if answer == 'YES':

                myCursor.execute("DELETE FROM Books WHERE name = '%s'" %(name))
            else:
                print('okay')

        else:
            print('Wrong Password')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    # app.setStyle('Windows')
    ex = Example()
    sys.exit(app.exec_())
