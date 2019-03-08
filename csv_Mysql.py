import os
import sys
import csv
import mysql.connector
from termcolor import colored


#############################################################################################################
#  OBS->You need to close and reopen the program after you added a book to the database outside the program #
# (if it is via the program there is no problem whatsoever)                                                 #
#                                                                                                           #
#                                                                                                           #
#############################################################################################################


eLib = mysql.connector.connect(host = 'localhost', user = 'root', password = 'P3dr0mysql', database = 'eLib')
myCursor = eLib.cursor(buffered=True)


os.system("clear")
#print("_|_|_|_|            _|        _|  _|                                              \n_|                  _|            _|_|_|    _|  _|_|    _|_|_|  _|  _|_|  _|    _|\n_|_|_|  _|_|_|_|_|  _|        _|  _|    _|  _|_|      _|    _|  _|_|      _|    _|\n_|                  _|        _|  _|    _|  _|        _|    _|  _|        _|    _|\n_|_|_|_|            _|_|_|_|  _|  _|_|_|    _|          _|_|_|  _|          _|_|_|\n                                                                                _|\n  ")
print(" _____           _     _ _                          \n| ____|         | |   (_) |__  _ __ __ _ _ __ _   _ \n|  _|    _____  | |   | | '_ \| '__/ _` | '__| | | |\n| |___  |_____| | |___| | |_) | | | (_| | |  | |_| |\n|_____|         |_____|_|_.__/|_|  \__,_|_|   \__, |\n                                              |___/ ")


#file_name = input("Please inser the .csv file name(with extension) ->")
file_name = sys.argv[1]
formula = "INSERT INTO Books (name,path,ebook,pdf,fiction,mystery,fantasy,science_fiction,non_fiction,genre_fiction,thriller,romance,young_adult_fiction,crime_fiction,literary_fiction,horror_fiction,history,fairy_tale,comic_book,manga,light_novel,classic) VALUES ('%s','%s',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

try:
    with open(file_name,'r') as file:
        fHand = csv.reader(file, delimiter = ',')

        print("These titles were added to the database: \n")
        for row in fHand:

            try:
                myCursor.execute(formula %(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21]))

                eLib.commit()
                print(row[0])

            except:
                print("An error occurred while submitting :",row[0])

    print("\n")
    print("After you finish the database's update please make sure to restart the main program\n")


except:
    print('\n')
    print(colored("[ERROR] Make sure you add the .csv file name as an argument in the command line",'red'))
    print('\n')
