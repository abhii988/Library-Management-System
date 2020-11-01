'''
This is the return book module for the user to return a book.
It imports booklist.py and datetime modules in order to access their main functions.
It imports the 2D list of books from booklist.py for the user to return a book and see if it is present in the library or not.
It then stores a record of the user in a text file 'returned_details.txt'.
The module datetime is imported from the python library to save the date of borrow of the user to save their record.
'''
import datetime
import booklist as b
booklst=b.listing2d() #saving the list of books in booklst from booklist.py
dash='-'*95 #declaring a variable to design the program whilst printing
today = datetime.date.today() #declaring a variable that stores today's date i.e. the day of borrow of book.
'''
This function takes the user's name as input from the user and checks if the name exists in the record of borrow in 'borrow_details.txt'. 
If the name exists, it returns all of the borrowed books and prints a message else it returns the user back to the menu
This function returns nothing.     
'''
def return_book():
    norecord=True
    global returned
    returned = []
    readborrowfile()
    returner=input("Please enter your name again: ")
    for i in range(len(lst2)):
        if returner==lst2[i][0]:
            returned.append(lst2[i])
            #print(returned)
            returneddetails()
            norecord=False
            lst.remove(lst2[i])
            print("ThankYou for returning the book.")
    if norecord==True:           
        print("Sorry, your name doesn't exist in our database.")
    updatebooklist()
    overwrite_txt()
    #print(returned)
    #print(ret)
    print(dash)
    print()
    #print(lst2)
    #print(returned)
#function reads the record of borrow in 'borrow_details.txt' and saves it in a 2D list. This function returns nothing.
def readborrowfile():
    file=open("borrow_details.txt","r")
    content=file.readlines()
    file.close()
    global lst
    global lst2
    lst=[]
    lst2=[]
    for i in range(len(content)):
        lst.append(content[i].replace("\n","").split(","))
        lst2.append(content[i].replace("\n","").split(",")) 
#function stores a record of the user to return a book in a 2D list'. This function returns nothing.
def returneddetails():
    global ret
    ret=[]
    for i in range (len(returned)):
        details=returned[i][0]+","+returned[i][1]+","+returned[i][2]+","+str(today)+"\n"
        ret.append(details)
    writereturnfile(ret)
#function writes the record of the user in a text file 'returns_details.txt'. This function returns nothing.
def writereturnfile(returnedlist):
    file=open("returned_details.txt","a")
    for each in returnedlist:
        file.write(each)
    file.close()
#function that updates the list of books in stock in 'books.txt' file that increases the quantity of the book that user returned. This function returns the new list with the updated quantity.
def updatebooklist():
    global updatelist
    updatelist=[]
    for j in range (len(returned)):
        for k in range (len(booklst)):
            if returned[j][1]==booklst[k][1]:
                newqty=int(booklst[k][3])+int(returned[j][2])
                booklst[k][3]=str(newqty)                
    updatelist=booklst
    return updatelist
#function that overwrites the list of books in 'books.txt' file with increases the quantity of the book that user had returned. This function returns nothing.
def overwrite_txt():
    a=updatelist
    file=open("books.txt","w")
    for i in range(len(a)):
        counter=1
        for j in range(len(a[i])):
            file.write(a[i][j])
            if counter <=4:
                file.write(",")
            counter+=1
        file.write("\n")
    file.close()
