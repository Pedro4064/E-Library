import os
import time
import getpass
import subprocess
import mysql.connector #Needs to be installed via pip
from random import randint
import time
from termcolor import colored #Needs to be installed via pip

#############################################################################################################
#  OBS->You need to close and reopen the program after you added a book to the database outside the program #
# (if it is via the program there is no problem whatsoever)                                                 #
#                                                                                                           #
#                                                                                                           #
#############################################################################################################


#mysql settings
eLib = mysql.connector.connect(host = 'localhost', user = 'root', password = 'P3dr0mysql', database = 'eLib', connect_timeout = 86400) #The time out is to ensure the connection will live for at least a day
myCursor = eLib.cursor(buffered=True)

#variables
password = "4064"
addFormula = "INSERT INTO Books (name,path,path_to_cover,driveLink,ebook,pdf,fiction,mystery,fantasy,science_fiction,non_fiction,genre_fiction,thriller,romance,young_adult_fiction,crime_fiction,literary_fiction,horror_fiction,history,fairy_tale,comic_book,manga,light_novel,classic) VALUES ('%s','%s','%s','%s',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
searchFormula = "SELECT name FROM Books WHERE name LIKE '%%%s%%' ORDER BY name"
pathFormula = "SELECT path FROM Books WHERE name = '%s'"

############################################################################################################

def zeroTwo():

    os.system('clear')
    print(':/oooooo++.`````````.................-...................-..//..-............-.``````````````````````````````````````````````````````````````.:+osoo/:\n-:+ooooo+-```````````..-.............-.............-.....:../:```-............````````````````````````````````````````````````````````````````/+++oo+/\n`.:+ooo:`````````````..:.............:.............-.....+../.````.-..........``````````````..````````````````````..:////..```````````````````.--:++/+\n``./++/`````````````...:.............:.............-.....+-.:``````.-..........````````````...````````````````````..-:///+/-``````````````````````:/++\n````::````````````.....--............:.............:-..../-.:```````.-..............````.......``````````..````````.....-:/+/-`````````````````````./+\n`````````````````.......-............:............./:..../:.:.````````--..........-......-.....`````````.....``````.......-/````````````````````````.:\n````````````````-.......:.........-..:......-......//....//.-.````.````.-..........-.....-......````````........``````......``````````````````````````\n``````````````..:.......--........-..:......-....--++....::---``````````.--........-:....--.....................```````....```````````````````````````\n`````````.....-.:......../........-..:-.....--...:-o/....::-.-````````````.-........-:-..--....................````````.....``````````````````````````\n`````````....-:.:........o-.......-..:/.....--.-.::/:-...:.:-:`````````````.--.......-:---:...................``````````........-::-.`````````````````\n`````````....-/-:........+/..-....--.-+.....././-:/..:...:`:-:--::::--...-...::.......-:--:....................``````````........://:`````````````````\n```````````..:/-:......../--.--....:.-+-...../-/--+``/...:/o:-+-...```````````:/-......-:-:-...................``````````..........--```````````````.+\n```````````..//-:-....-..:`:--:....:--//.....::/--+``/:.-//:/-:````````````````:o:-.....::-:..................``````````............```````````````./s\n.`````````.../----....:..:..:-:....-/-/:.....-+/--/:++/--:/++::````````````````./+:-....-::/..................`````````.-.........```````````````/+ssy\n/.```````....-.:-:....-----`.:--..../:/-:.-.../+/-+/-.+:-:++:::-```````.````````./:-:-....:+-..................``````...--......`````````.```...-ossyy\n+/:-.```.....-`:-/-...-:--:``--:-...-+/.:-:-..:os-/-./+o--+-`.::``......````..```.+-.:--..-/:....................--:-...-:.....`````````````````:++oyy\n/::////......-`--:/-...:-.:.``--:....:+::--/..-+//-/:++o/-:```-+:-....-:+osyyho/:-/s//++----/...................-++::----:-....`````````````````://+ss\n+++++o+.....--`.:-o-...-/---```:::...-/+./-/-..-/:-/:+++:-:..-....-/shdmNNNNNNmmmdddyysoo:--/...................-oso/:---:-....```````````````.:+//+ss\n++o++oo.....-.``-:/+-..-+:-/````:::...-+:-:-/-..:.//://.`-/-.``./ydNNNNNNmddhysooooosys/:::-:-.................--ssyo+:---:....``````````````:+oosssss\noooo+oo-....-.```::/:-..:s::+-``./:/-..-/.::+/--:.-/:..``.-/`.+hmNNNmdyo/:-..........:/.``.-::.................--ssssoo---:......``````````../ossssyss\noo+++oo--...-.````::o/---/o:+/:-.-//:--.-:`-:+:---`:/.`````-.smmmdy+:-..```````.``.``.:/.```.:.................-:sooo+/:--/--....``````````../osssyyys\n+++ooo+--...-.````-:/-:---++:ooo+/:/-----:-`.:::+/..::`````.smdy+-.``````.```..........-/-```:.................-/o+:.````...---..``````````../:+syyyys\n//++so+-:...--``````::..---::/o++o++/`.---/.`.-.-:-``.`````.yy:.```````...`.........```.-/-``:..................+:.````.-...-.--..`````````../.-ossso+\no+++sso-:...--```````-:``.-:::/:-//++.```.-:.```````````````-.```````````.```....````````-/:.--................./````.-.````.-.:.....````..../..///+oo\ns++ssso-:-.../``````````````..`.``..-.`````..`````````````````````````````````````````````-::::-................:```.-.````````:-............/``:+ssss\nyysssoo--:..-/-```````````..--------.``````````````````````````````````````````````````````-::/-................:``.:.--::-````.:............/..+syyyy\nssoosss--:-.-:/.`````````.....-----..```````````````````````````````````````````````````````.:/-...............-:``//+ooooo:```.:...........-+/syyyyyy\nssssyys---:---/-```````.-+syhddddhys+.```````````````````````````````````````````````````````./-...............-:`.oooooooso.```:...........-+osyyyyys\n+oossys:------/-.`````.odNNNNmho/:-..``..`````````````````````````````````````````````````````:--..............--`.+ooooooso.```-...........-+ssssyyyy\n/osssss:---:--/-:.```.-mNNNms:..```````..`````````````````````````````````````````````````````--..............---``.+oooooy+.``.-..........--/ssssyyyy\nsosooso/-.--:--/--``.:oNNms-.````````.````````````````````````````````````````````````````````.:-..............-.``.:ooooos/``.--........----/ssyyyyyy\nyyhyyyy+-...-:-/-:.`/osdh:.``````````.:.``````````````````````````````````````````````````````.:-..............:.`./oooooso-`./-.........----/ssyyyyhy\nhhhyyyy+-....-:::-:./++/.`````````````-/.``````````````````````````````````````````````````````:--............-:.:ooooooos/..+o-.........-:--:ssyyyhhh\nhhhhhyyo-.....-:/-:.``````````````````.:+.`````````````````````````````````````````````````````:..............-/+oooooooso-.+oo--........-/---syyyyyhh\nyyyyyyys-......-/+-:````````````````````-/.````````````````````````````````````````````````````-..............-/+ooooooo/--:oso-........../---sssyyyyh\nhyyyyyys--.-....---:-````````````````````..````````````````````````````````````````````````````--.............-/.://::-.`-:-oss:-........./---sssyyyyh\ndhhyysss---:-.......:``````````````````````````````````````````````````````````````````````````--............../````````-:.-+ss:..........:---oosyyyyh\ndhhyyyyy:--/-....--.:-`````````````````````````````````````````````````````````````````````````:.-..-.........-:```````--..-/ss:-.........:---o+syyyyy\nddhyyyyy/--/-....----:`````-.``````````````````````````````````````````````````````````````````:--............-:```..::-...-:ss:-.........-:--o++syyyy\nddhyyyss+--/-.......-:-```````````````````````````````````````````.-```````````````````````````:--.-.........-:yooosso-....-:ss/-.........-/--ssoosyyy\nhyyhyyyso--+-.......--/.``````````````````````````````````````..---.```````````````````````````:--.-........--/yssssso-.....-os/-..........:--oooosyyy\nsyyyyyyys--+-........-/-`````````````````````````````````...----..`````````````````````````````:--...........-+yssssso-.....-+y/-..........::-+oo+osyy\nsyyyyyyys--s-........-/+.``````````````````````````...---.....`````````````````````````````````:--.-.........-+sysssss-....../y+-..........-/-+oo+oosy\nyyyyyysss--o-........-/o/.``````````````````````.---..`````````````````````````````````````````::-.-.........-osyyssss----...:s+-.........../-/oo+/+os\nooossssss--o-.......--/oo-.````````````````.-..--..````````````````````````````````````````````-:-...........-soyyysso---:...-so-...........:::so+//+o\n+oosssssy--s:........-/ooo.````````````````.....````````````````````````````````````..`````````-:-.........---soysysso---/...-/s-...........-/-+++/:/+\nosssssyyh-:s:........-/sso/.````````````````.``````````````````````````````````````.-.`````````-:-.-.......---ssyyysso---/...--s-............/-//o+//+\nsssyssssy-/s/........-/ssso/.```````````````````````````````````````````````````````..`````````-:-..........-:soyyysso---/...--+:............::/+oo+++\nsyyyyyysy-+s/.........:sssss+.`````````````````````````````````````````````````````````````````--...........-/oosyssso---/-...-:/-...........-/:ooo+++\nsossssssy:+y+........-:sssssso-.``````````````````````````````````````````````````````````````./:-.........--+oosyysso---/-..---/-............:-o+oooo\no++++ooos:+s+.........:ssssssso+-``````````````````````````````````````````````````````````.-/+o:...........-+oosyysso---/-...--:-............-:o++ooo\nsoosssoos:oso-........:ssssssssys/-`````````````````````````````````````````````````````.-/+ooos-.........-.-ooossysss---+-.....-:............-/+o/+++\nsoossssos:oss-........-osssyyssyyso/-.```````````````````````````````````````````````.-/+oooooos-...........-soosshsss---o--....-:.............:+so+++\nsssssyyss:+ss-........-ossyyyyyhyyso++-.`````````````````````````````````````````..-/+ooooooooos-..........--sosssyyss---o:......:--...........-+ssso+\nyyyyyyysy/+ys:........-ossyyyyyhyhsooyoo/-.````````````````````````````````````.:/+ooooooooooooo-..........-:sossssyss---o/......-:-............:ysss+\ndddddhyyh//ys/........-+sssyyyyhhyo+oyssso+:.``````````````````````````````..:/+ooooooossssooooo-..........-/oossssyss---++-......:-............-+ooso\nddddddhhh//ys+-.......-/ssyyyyyhhyooshyssssss/-.````````````````````````.-:+ooooooosososssssooos-..........-+oosssssys---+o-......-:.............-+oss\nhhhhhhhhh+:sss-......../ssssyyydhs+syhyssssshsso/-.`````````````````.-:/+oooooosososssssssssoooo-..........-+oosssssys---+o/.......:-............./sss\nhhhhhhhhy+:ssy:........:ssssyyydyo+shdhysysshyssso+:.```````````.-:/+oooooooosssssssoososssooooo-..........-ooossssooy---:s+-......-:-............-oss\nhhhhhhhhy+:oos/........:sssyyyyds+oyhddyyyyyyhsssssso/-.``...-:+oooooooosssssssssssssssssssooooo-..........-soossooo+o----so:-......:-............-:oo\nhhhhhhhyy+-sss+-.......-sssyyyyhoosyhhdyyyyyyhyssssssso++++oossssysoooossssssssssssssssssssoooo+-.........--sooooo+:.-:---oo+-......-:-............-/o\nyhhhhhhhyo-syys-.......-ossyyyyhooshhhdyyyyyyhyyyssssssssssssssssyyssssssssssssssssssssssssoooo+-.........-:oooo+:.``.:---+so/--.....-:-............-+\nyyyhhhyyyo-syyy-.......-osssyyyyosyhhhdyyyyyyhyyyyysyssssssssyysssyhssssssssssssssssssssssssooo+-.........-/oo+/.````./---/sso:-......-:-...........-:\nyyyyhyyyys-syyy:.......-+sssyyyyosyhhhhhyyyyyyhyyyyyyysyysysyyysyyyyyssssssssssssssossssssssooo+-.........-/+/-``````./---:ssso-.......-:...........--\nyyyyyyyyys-oyss+........+sssyyyyossyyyyhyyyyyyhyyyyyyyyssssysysyyyyyhssssssssssssossssssssosoooo-.........-/:.````````/----ssss+--......::-..........-\nyyyyyyyyys-+oooo......../sssyysy+osyyysyssyyyyyyyyyyyyyssssyyysyyyyyyyssssssssssssssssssssssoooo-..........:``````````:----//+oo+:-....--::-......----\nyyyyyyyyyy:/ssoo-......./sssyysyooosyyo/yssyyyyhyyyyyyyyssysssyyyyyyyysssssossssssssssssssssoooo-..........:``````````.:----/..-:::-------::-----:::::\nyyysssyyyy/:ssos/.......:sssyyyhsoosyysoyssyyyyhyyyyyysssysssyysyyyyyyhssssssssssssssssssssooooo-.........-:```````````:----::...```..-----/+::::-----\nyyyyssyyyy+-sssoo.......-sssyyshsoosyyyyhyyyyyyyhyyyyyyyyyysyyyyyyyyyyyyssssossssssosssssssooooo-.........-:```````````.:----:+:---------::-------:---\nsyyyyyyyyyo-oysos-......-osssssho+osyyyyhyyyyyyyhyyyyyysyyyysysssssssssysoosssssssossssssssoooos-........--:````````````.-:----::------------:::--.---\nsyyyyyyyyys-+ysos:.......+sssyshsoosyyyyhyyyyyyyyhyysssyysssssssssso+/:-soossssssssosssssssosoos-........-:-``````````````.:-----::------::------..```\nsyyyyyyyyyy-+ysss+.......:sssyyhyssyyyyyyyyyysyyyhyysssssssssso+/:-.```.ooossssssssossssssssooos-.-.....--/.````````````````...---------..----.```````\nsyhhhyssyyy:/yysss-......-sssyshyyyyyyssyhsssssssyhsssssso+/-..```````./ososssssssssssssssssooos-.-.....--/.```````````````````````````.-..```````````\nshhhhhhyyyy+:yysss:......-osssshssyyysssshssssssssys+/:-.```````````.-+ooyssssssosssssssssooooos--......--/.``````````````````````````````````````````\nhhhddddhhyys-syysso-......+sssshsssssssssysssso+/:-.```````````````./ooosyssssssssssssssssoooo+o-.......--/```````````````````````````````````````````\nhhhhhhhhhyhy-oyyysy-....../ssssysosooo++//:-..```````````.````````-+oooosysssssssssoosssooooo/./-.......--/`````````````.-...`````````````````````````\n')

    input('')

############################################################################################################

def Tux():
    os.system('clear')
    print('\n                                                 ``````\n                                           `..............`\n                                        `....................`\n                                      `........................`\n                                     `..........................`\n                                    .............................`\n                                   `..............................\n                                   `..............................`\n                                   ..................-::-..........\n                                   ..-+ss+-.......-odmmmds:........\n                                   .-yNNNNh:.....:hNNddNNNd:.......\n                                   .:md/:+my.....yNh/--:hNNo.......\n                                   .-do...od.....dN:..../NNo.......\n                                   ..oy:.-/s+oso+yy:-..-yNy-.......\n                                   ...oo+shyhhhyyhhhys+ohs-........\n                                   `.:shhhhhhhhhhhhhhhhhyy+-.......\n                                   `-shhhhhhhhhhhhhhhhysoyy:.......`\n                                   ..:oyhhhhhhhhhhhysssyhyo-........\n                                  `...sssssssysssssyyhyyhdd:........`\n                                  ...-mNhyyyyyyhhhhyyydNNNNo.........`\n                                 `...+NNNmhyyyyyyyyhmNNNNNNd..........`\n                                `...-hNNNNNNNmmmNNNNNNNNNNNN/...........\n                               `..../NNNNNNNNNNNNNNNNNNNNNNNh-...........`\n                              `....-hNNNNNNNNNNNNNNNNNNNNNNNNo............`\n                            `......oNNNNNNNNNNNNNNNNNNNNNNNNNN/............`\n                           `......+NNNNNNNNNNNNNNNNNNNNNNNNNNNm/.............`\n                          .......+NNNNNNNNNNNNNNNNNNNNNNNNNNNNNd..............`\n                        `.......:NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNo-.............`\n                       `....-..+dNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNh:.-:-..........\n                      ....-/:-oNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNd:.-//-.........`\n                     ....-+-.oNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNh-../s-.........`\n                    ....-o-./NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNy.../y-.........`\n                  `.....o/.:dNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN+...ss..........\n                  .....:y-.yNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNd-../d-..........\n                 `.....os.:NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN+..:d/..........`\n                 ......yo.yNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNy..+d:..........`\n                 ......ys:dNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNd.-hy...........`\n                 ......+d+NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNd/yN+::---......`\n                 ......-dmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmy+++////::--....`\n               `.:+oo/-./mNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNmy-................\n              `-shhhhhy+-:yNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNdss/.............:ooo/-`\n             `:yhhhhhhhhs:-/hNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN+yho............/hhhhhy+`\n      ````.-/ohhhhhhhhhhhy/.-/smNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNm+hhy-.........-ohhhhhhhh-`\n   `.:+osyyhhhhhhhhhhhhhhhh+-..:+hmNNNNNNNNNNNNNNNNNNNNNNNNNNNNNd+hhho-.....-:oyhhhhhhhhh/`\n   .+hhhhhhhhhhhhhhhhhhhhhhhs:...-:odNNNNNNNNNNNNNNNNNNNNNNNNNNNd+hhhhyo+++syhhhhhhhhhhhhy/`\n  `-yhhhhhhhhhhhhhhhhhhhhhhhhy/.....:sNNNNNNNNNNNNNNNNNNNNNNNNNNhohhhhhhhhhhhhhhhhhhhhhhhhh+-`\n  `-yhhhhhhhhhhhhhhhhhhhhhhhhhh+-....:NNNNNNNNNNNNNNNNNNNNNNNNNNsohhhhhhhhhhhhhhhhhhhhhhhhhhyo:`\n   .shhhhhhhhhhhhhhhhhhhhhhhhhhhs:.-:yNNNNNNNNNNNNNNNNNNNNNNNNh/.ohhhhhhhhhhhhhhhhhhhhhhhhhhhhho-`\n   .shhhhhhhhhhhhhhhhhhhhhhhhhhhhy/+dNNNNNNNNNNNNNNNNNNNNNNmy/...shhhhhhhhhhhhhhhhhhhhhhhhhhhhhhs-\n   -yhhhhhhhhhhhhhhhhhhhhhhhhhhhhhho/+ydmNNNNNNNNNNNNNmmhs/-....-yhhhhhhhhhhhhhhhhhhhhhhhhhhhhhy+.\n  `/hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhy+-.-:/+oosssooo+/:-........+hhhhhhhhhhhhhhhhhhhhhhhhhhhhs/-`\n  -shhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhs-.......................-yhhhhhhhhhhhhhhhhhhhhhhhhhs/-`\n  -shhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh+.......................:hhhhhhhhhhhhhhhhhhhhhhhs+-`\n  `-+syhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhho.......................+hhhhhhhhhhhhhhhhhhhhy+-``\n    ``.-:/+osyyhhhhhhhhhhhhhhhhhhhhhhhh/.                ```.../hhhhhhhhhhhhhhhhhyo:.`\n           ```..-:/+oyhhhhhhhhhhhhhhhy:`                      `-shhhhhhhhhhhhhhy/-`\n                   ``..:/osyhhhhhhhs/.`                        `-ohhhhhhhhhhhs:.`\n                         ``..-:::-.``                            `.:+ossso+/.`\n                                                                     ``````                         \n')

    input()
############################################################################################################

def searchName(name): #Change in the future to be like the randomBook() -> no need to fetchall() multiple times....

    counter = 1

    os.system("clear")
    print("The name of the book you searched for is "+name+"\n")
    print("Results found: ")

    myCursor.execute(searchFormula %(name))

    #Print all the results so the user can chose which one is the right one ...
    for result in myCursor.fetchall():
        print(str(counter)+"• "+''.join(result))
        counter+=1

    #Gets the response and turns into string
    #name = ''.join(myCursor.fetchall()[0])
    #path = ''.join(myCursor.fetchall()[2])
    #path_to_cover = ''.join(myCursor.fetchall()[3])
    #print(name)
    print("\n")
    answer = input("Which one is the right one? ")

    #Send the command again to get the name again
    myCursor.execute(searchFormula %(name))

    try:
        os.system("clear")
        correct = ''.join(myCursor.fetchall()[int(answer) - 1]) #Computers count from 0, humans on the other hand count form 1...
        print(correct)

        #Get the path for the book by the name
        myCursor.execute(pathFormula %(correct))
        path = ''.join(myCursor.fetchall()[0])
        print(path)
        sendToDevice(path)

    except:
#print(str(int(answer)-1))
        print(colored("Not a valid option...",'yellow'))

    input("")

############################################################################################################

def sendToDevice(path):

    counter = 1

    os.system("clear")
    os.chdir("/Volumes/") #Change to /media/pi for the raspberry pi

    #Get the list of devices
    choices = subprocess.getoutput("ls").split("\n")

    for choice in choices:

        #Does not consider the hard drive and backup partition
        if choice != "Recovery" and choice!= "Macintosh HD": #Change this in the final code so the hd does not show up

            print("%d->%s" %(counter,choice))
            counter+=1



    print("\n")

    answer = input("Where to send the book to?")
    answer = int(answer) - 1  #humans count from 1, in the other hand machines count from 0...

    #move the file to the desired place
    inp = input("Is it a kindle device? [y/n]")
    if inp.casefold() == "y":
        #Change to /media/pi for the raspberry pi
        os.system("cp %s /Volumes/%s/documents" %(path,choices[answer]))#On kindle devices the book has to be on the documents folder

    else:
        os.system("cp %s /Volumes/%s" %(path,choices[answer]))

    eject = input('Eject device? [y/n]')

    if eject.casefold() == 'y':
        #change to umount /media/%s for the raspberry pi
        os.system("diskutil unmount /Volumes/%s" %(choices[answer])) #unmount the kindle/flash drive CHANGE TO unmount /Volumes/%s/ on linux
    elif eject.casefold() == 'n':
        print(colored('Make sure to eject device before removing it','yellow'))
    else:
        print(colored('Not a valid option', 'yellow'))

############################################################################################################

def newBook():

    pdf = 0
    ebook = 0

    fiction = 0
    mystery = 0
    fantasy = 0
    science_fiction = 0
    non_fiction = 0
    genre_fiction = 0
    thriller = 0
    romance = 0
    young_adult_fiction = 0
    crime_fiction = 0
    literary_fiction=0
    horror_fiction = 0
    history = 0
    fairy_tale = 0
    comic_book = 0
    manga = 0
    light_novel = 0
    classic = 0

    name = input("Please enter the name: ")
    path = input("Please enter the path: ")
    path_to_cover = input("Please insert path to cover: ")
    format = input("What is the format of the book?(pdf/mobi/both) ")
    driveLink = input("The Google Drive link : ")

    if format.casefold() == "pdf":
        pdf = 1
    if format.casefold() == "mobi":
        mobi = 1
    if format.casefold() == "both":
        mobi = 1
        pdf = 1

    #Read the multiple genres a single book can be
    type = input("Please insert the genres of the book (use , to separate multiple genres) ->")
    type.casefold()
    type.split(",")

    if "fiction" in type:
        fiction = 1
    if "mystery" in type:
        mystery = 1
    if "fantasy" in type:
        fantasy = 1
    if "science_fiction" in type:
        science_fiction = 1
    if "non_fiction" in type:
        non_fiction = 1
    if  "genre_fiction"in type:
        genre_fiction = 1
    if "thriller" in type:
        thriller = 1
    if "romance" in type:
        romance = 1
    if "young_adult_fiction" in type:
        young_adult_fiction = 1
    if "crime_fiction" in type:
        crime_fiction = 1
    if "literary_fiction" in type:
        literary_fiction = 1
    if "horror_fiction" in type:
        horror_fiction = 1
    if "history" in type:
        history = 1
    if "fairy_tale" in type:
        fairy_tale = 1
    if "comic_book" in type:
        comic_book = 1
    if "manga" in type:
        manga = 1
    if "light_novel" in type:
        light_novel = 1
    if "classic" in type:
        classic = 1
    #Now add all the Information above in the table on the database

    myCursor.execute(addFormula %(name,path,path_to_cover,driveLink,ebook,pdf,fiction,mystery,fantasy,science_fiction,non_fiction,genre_fiction,thriller,romance,young_adult_fiction,crime_fiction,literary_fiction,horror_fiction,history,fairy_tale,comic_book,manga,light_novel,classic))
    input("")
    eLib.commit()

############################################################################################################

def searcheById():
    os.system("clear")

    id = input("Book id:")

    try:
        myCursor.execute("SELECT name FROM Books WHERE id = %d" %(int(id)))
        for name in myCursor.fetchall():
            print("Book name:",''.join(name))

    except:
        print(colored("Not a valid id","yellow"))
    input()

############################################################################################################

def byGenre():
    counter = 0
    os.system("clear")
    genre = input("Please insert a genre: ")

    try:
        myCursor.execute("SELECT name FROM Books WHERE %s = 1" %(genre.casefold()))
        for book in myCursor.fetchall():
            counter+=1
            print("%d->%s" %(counter,''.join(book)))
    except:
        print(colored("Not a valid option, please check if the genre is correct (according to de file system)",'yellow'))

    input()
############################################################################################################

def randomBook():
    try:
        myCursor.execute("SELECT name FROM Books")
        books = myCursor.fetchall()

        number = randint(0,len(books) - 1)
        print("The book name is: ", ''.join(books[number]))
    except:
        print("A problem occurred, please contact technician")

    input()

############################################################################################################

def bookList():
    counter = 0

    os.system("clear")
    myCursor.execute("SELECT name FROM Books ORDER BY name")

    for book in myCursor.fetchall():
        counter+=1
        print("%d->%s" %(counter,''.join(book))) #''.join(myCursor.fetchall()[0] is to format the duple into a string)

    #So the user can read and go back to the main screen when he presses enter(otherwise the loop will continue and no one will be apble to read...)
    input()

############################################################################################################

def edit():
    print("1-> Edit Information")
    print("2-> Delete book info")

    inp = input("")

    if inp == "1":
        os.system("clear")
        name = input("Please insert the name of the book you wish to edit: ")
        info = input("which Information you wish to change?(only one thing at a time) ")
        new = input("Enter the new Information: ")

        try:
            myCursor.execute("UPDATE Books SET %s=%s WHERE name = '%s' " %(info,new,name)) #Tries to edit the info if it's an int
            eLib.commit()

        except:
            try:
                myCursor.execute("UPDATE Books SET %s='%s' WHERE name = '%s '" %(info,new,name)) #Tries to edit the info if it's a string(name,path,driverLink...)
                eLib.commit()
            except:
                print(colored('[ERROR] Please contact technician','red'))

    elif inp == "2":
        os.system("clear")
        name = input("What is the name of the book you want to delete? \n")
        #print(colored("Are you sure you want to delete?[y/n]","red"))
        answer = input(colored("Are you sure you want to delete?[y/n] ","red"))

        if answer == "y":
            myCursor.execute("DELETE FROM Books WHERE name = '%s'" %(name))
            eLib.commit()

        else:
            print(colored("Okay, operation terminated","green"))

    else:
        print(colored("Not a valid option","yellow"))

    input()

############################################################################################################

while True:

    authorization = False

    #Default value for which genre


    os.system("clear")

    #print(' -----------------------------------------------\n|                                               |\n|                                               |\n|                                               |\n -----------------------------------------------')



    #print(' ------------------------------------------------\n|    _____         __          _       _____     |\n|   |  ___|       |  |        | |     | |     \  |\n|   |  |__        |  |        | |     | |      | |\n|   |   __|  –––- |  |        | |     | |_____/  |\n|   |  |__        |  |____    | |     | |     \  |\n|   |_____|       |_______|   |_|     |_|_____/  |\n -----------------------------------------------\n')
    #print("_|_|_|_|            _|        _|  _|                                              \n_|                  _|            _|_|_|    _|  _|_|    _|_|_|  _|  _|_|  _|    _|\n_|_|_|  _|_|_|_|_|  _|        _|  _|    _|  _|_|      _|    _|  _|_|      _|    _|\n_|                  _|        _|  _|    _|  _|        _|    _|  _|        _|    _|\n_|_|_|_|            _|_|_|_|  _|  _|_|_|    _|          _|_|_|  _|          _|_|_|\n                                                                                _|\n  ")
    print(" _____           _     _ _                          \n| ____|         | |   (_) |__  _ __ __ _ _ __ _   _ \n|  _|    _____  | |   | | '_ \| '__/ _` | '__| | | |\n| |___  |_____| | |___| | |_) | | | (_| | |  | |_| |\n|_____|         |_____|_|_.__/|_|  \__,_|_|   \__, |\n                                              |___/ ")


    #Asks the user for an input
    print("Sociedade Recreativa Literaria CMB\n\n")
    print("Chose one of the options below:")
    print("\n")
    print("1.Search by name")
    print("2.Search by book genre")
    print("3.Random book recommendation")
    print("4.Print list of books")
    print("5.Add new book")
    print("6.Edit database")

    answer = input("->")


    if answer == '02' or answer == 'zeroTwo':
        zeroTwo()

    elif answer == 'tux' or answer == 'tux s2':
        Tux()

    if answer == "1":
        os.system("clear")
        name = input("Please insert the name of the book you wish to check out: ")
        searchName(name)

    # elif answer == "2":
    #     os.system("clear")
    #     searcheById()

    elif answer == "2":
        os.system("clear")
        byGenre()

    elif answer == "3":
        os.system("clear")
        randomBook()

    elif answer == "4":
        os.system("clear")
        bookList()

    elif answer == "5":
        os.system("clear")
        while authorization == False:
            inp = getpass.getpass()

            if inp == password:
                authorization = True
                print("Permission granted")
                newBook()
                #Function to add new book
            else:
                os.system("clear")
                print("Wrong password")

    elif answer == "6":
        os.system("clear")
        while authorization == False:
            inp = getpass.getpass()

            if inp == password:
                authorization = True
                print("Permission granted")
                edit()


    elif answer == "q" or answer == "Q" or answer == "quit":
        quit()
    else:
        print(colored("Not a valid option","yellow"))
