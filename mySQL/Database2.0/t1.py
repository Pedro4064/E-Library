from termcolor import colored
import mysql.connector
import os

eLib = mysql.connector.connect(host = 'localhost', user = 'root', password = 'P3dr0mysql', database = 'elib2', connect_timeout = 86400) #The time out is to ensure the connection will live for at least a day
myCursor = eLib.cursor(buffered=True)



def mainFrame():

    authorization = False

    os.system('clear')

    print(" _____           _     _ _                          \n| ____|         | |   (_) |__  _ __ __ _ _ __ _   _ \n|  _|    _____  | |   | | '_ \| '__/ _` | '__| | | |\n| |___  |_____| | |___| | |_) | | | (_| | |  | |_| |\n|_____|         |_____|_|_.__/|_|  \__,_|_|   \__, |\n                                              |___/ ")


    #Asks the user for an input
    print("Sociedade Recreativa Literaria CMB\n\n")
    print("Chose one of the options below:")
    print("\n")
    print('1.Search Book')
    print("2.Random book recommendation")
    print("3.Print list of books")
    print("4.Add new book")
    print("5.Edit database")

    answer = input("->")

    if answer == '1':
        searchBook()
    if answer == '2':
        print(answer)
    elif answer == '3':
        print(answer)
    elif answer == '4':
        print(answer)
    elif answer == '5':

        os.system("clear")

        while authorization == False:

            inp = getpass.getpass()

            if inp == password:
                authorization = True
                print("Permission granted")
                Edit()
                #Function to add new book
            else:
                os.system("clear")
                print("Wrong password")


    else:
        quit()

def searchBook():

    os.system('clear')

    print('1.Search by book name')
    print('2.Search by genre')
    print('3.Search by series')
    print('4.Search by author')
    print('5.Searh by language')

    answer = input('->')

    if answer == '1':
        bookName()

    elif answer == '2':
        bookGenre()

    elif answer == '3':
        bookSeries()

    elif answer == '4':
        bookAuthor()

    elif answer == '5':
        bookLanguage()

    else:
        print(colored('Not a valid option','yellow'))

def bookName():

    os.system('clear')

    name = input('Book title ->')

def bookGenre():

    os.system('clear')

    genre = input('Book Genre ->')

def bookSeries():

    os.system('clear')

def bookAuthor():

    os.system('clear')

def bookLanguage():

    os.system('clear')

def Edit():
    

while True:

    mainFrame()
