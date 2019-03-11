import os
import sys
import csv
import mysql.connector
from termcolor import colored
from progress.bar import IncrementalBar


#############################################################################################################
#  OBS->You need to close and reopen the program after you added a book to the database outside the program #
# (if it is via the program there is no problem whatsoever)                                                 #
#                                                                                                           #
#                                                                                                           #
#############################################################################################################


#Creats a connection between python and mysql database
eLib = mysql.connector.connect(host = 'localhost', user = 'root', password = 'P3dr0mysql', database = 'eLib')
myCursor = eLib.cursor(buffered=True)

#Prints the banner
os.system("clear")
print(" _____           _ _ _                          \n| ____|         | (_) |__         ___ _____   __\n|  _|    _____  | | | '_ \\       / __/ __\ \ / /\n| |___  |_____| | | | |_) |  _  | (__\\__ \\\ V / \n|_____|         |_|_|_.__/  (_)  \\___|___/ \\_/   \n")

#Reads the argument(name of the file) passed in the terminal
file_name = sys.argv[1]

#mysql command to add data into the table Books
formula = "INSERT INTO Books (name,path,ebook,pdf,fiction,mystery,fantasy,science_fiction,non_fiction,genre_fiction,thriller,romance,young_adult_fiction,crime_fiction,literary_fiction,horror_fiction,history,fairy_tale,comic_book,manga,light_novel,classic) VALUES ('%s','%s',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

books = []
error = []

try:

    #count the number of rows in the file
    with open(file_name,'r') as file:

        counter = 0
        fHand = csv.reader(file, delimiter = ',')

        # get how many lines in the /csv file
        for row in fHand:
            counter+=1

    #Open the file and read line by line and formating the formual string to then commit to the database
    with open(file_name,'r') as file:
        fHand = csv.reader(file, delimiter = ',')

        #Creats a progress bar so the user can check the progress
        bar = IncrementalBar('Adding Books to the database', max = counter)

        for row in fHand:

            try:
                myCursor.execute(formula %(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21]))

                eLib.commit()
                books.append(row[0])

            #Add the name of the book it failed to add to the database to the error list
            except:
                error.append(row[0])

            #updates the progress bar
            bar.next()


    #If there are error messages
    if len(error) != 0:
        print(colored('[ERROR] failed to add these titles to the database','red'))

        for message in error:
            print(colored(message,'red'))


    print("\n")
    print("The folowing books were added to the database: \n")

    for book in books:
        print('•',book)

    print('\n')
    print(colored("After you finish the database's update please make sure to restart the main program\n",'yellow'))


except:
    print('\n')
    print(colored("[ERROR] Make sure you add the .csv file name as an argument in the command line",'red'))
    print('\n')
