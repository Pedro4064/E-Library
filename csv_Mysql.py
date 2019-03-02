import csv
import mysql.connector


#############################################################################################################
#  OBS->You need to close and reopen the program after you added a book to the database outside the program #
# (if it is via the program there is no problem whatsoever)                                                 #
#                                                                                                           #
#                                                                                                           #
#############################################################################################################


eLib = mysql.connector.connect(host = 'localhost', user = 'root', password = 'xxxxxx', database = 'eLib')
myCursor = eLib.cursor(buffered=True)

file_name = input("Please inser the .csv file name(with extension) ->")
formula = "INSERT INTO Books (name,path,ebook,pdf,fiction,mystery,fantasy,science_fiction,non_fiction,genre_fiction,thriller,romance,young_adult_fiction,crime_fiction,literary_fiction,horror_fiction,history,fairy_tale,comic_book,manga,light_novel,classic) VALUES ('%s','%s',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

with open(file_name,'r') as file:
    fHand = csv.reader(file, delimiter = ',')

    for row in fHand:

        myCursor.execute(formula %(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21]))

        eLib.commit()
