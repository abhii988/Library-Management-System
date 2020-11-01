'''
This is the borrow book module for the user to borrow a book.
It imports booklist.py and datetime modules in order to access their main functions.
It imports the 2D list of books from booklist.py for the user to borrow a book and see if it is present in the library or not.
It then stores a record of the user in a text file 'borrow_details.txt'.
The module datetime is imported from the python library to save the date of borrow of the user to save their record.
'''
import booklist as b
import datetime
dash='-'*95 #declaring a variable to design the program whilst printing
global qnty #declaring a global variable qnty
today = datetime.date.today() #declaring a variable that stores today's date i.e. the day of borrow of book.
lst=b.listing2d() #saving the list of books in lst from booklist.py
global bookids #declaring a global variable bookids
#function that asks the user for the quantity of books. This function returns the quantity of books inputed by the user.
def askforbookquantity():
    global qty #declaring a global variable qty
    a=input("Please enter the quantity: ") #taking input of quantity
    qty=int(a) #saving the quantity as qty
    #comparing the inserted quantity of user to check if it is less than or equal to zero
    if(qty <= 0):
        print("Quantity cannot be less than or equal to 0. Try again.")
        askforbookquantity()
    return qty   
#function that asks the user for the bookID of book that the user wants to borrow. This function returns nothing.
def askforbook():
    global qnty #declaring a global variable qnty
    qnty=[] #declaring an empty list to save the quantities of book
    val=False #declaring the boolean value of val as false to make the user to borrow another book
    global bookname #declaring a global variable bookname
    bookname=[] #declaring an empty list
    global bookid #declaring a global variable bookid
    #global bookids #declaring a global variable bookids
    #bookids="nth"
    bookid=input("Enter the BookID of the book you want to borrow:") #takes bookID as input of the book
    #checks if the book is available or not
    for i in range (len(lst)):
        if bookid in lst[i][0]:
            print("The book that you want is available.")
            askforbookquantity()
            qnty.append(qty)
            
            val=True
            for j in range (len(lst)):
                if bookid in lst[j][0]:
                    bookname.append(lst[j][1])
    #calls the function if the user wants to borrow another book
    if val==True:
        anotherbook()
    else:
        print("Sorry,the book that you want is not availabe in our library.")
    #calls the function borrowedbooks()
    borrowedbooks()
    #calls the function totalprice()
    totalprice()
    #calls the function overwrite_txt()
    overwrite_txt()
    print(dash)
    print()
#function that asks the user for the bookID of book that the user wants to borrow again. This function returns nothing.
def anotherbook():
    global bookids #declaring a global variable bookids
    val=False #declaring the boolean value of val as false to make the user to borrow another book
    more=True #declaring the boolean value of more as as true to make the program run in loop
    while more==True:
        choose=input("Do you want another book?(Y/N)")
        if choose.upper()=="Y":
            bookids=input("Enter the BookID of the book:")
            if bookids!=bookid:
                for i in range(len(lst)):
                    if bookids in lst[i][0]:
                        print("The book that you want is available.")
                        askforbookquantity()
                        qnty.append(qty)
                        val=True
                        for j in range (len(lst)):
                            if bookids == lst[j][0]:
                                    bookname.append(lst[j][1])
                if val==True:
                    anotherbook()
                else:
                    print("Sorry,the book that you want is not availabe in our library.")
            else:
                print("Sorry,you cannot borrow the same book twice.")
        more=False
#function that saves the record of the user who borrows the book in a list. This function returns nothing.
def borrowedbooks():
    borrow=[]
    borrowername=input("Please enter your name again: ")
    for i in range (len(bookname)):
        details=borrowername+","+bookname[i]+","+str(qnty[i])+","+str(today)+"\n"
        borrow.append(details)
    print("The books that you borrowed are: ",bookname)
    print("And the corresponding quantity is: ",qnty)
    writeborrowfile(borrow)
    updatebooklist()
#function that saves the record in borrow_details.txt from the list created above. This function returns nothing.
def writeborrowfile(borrowlist):
    file=open("borrow_details.txt","w")
    for each in borrowlist:
        file.write(each)
    file.close()
#function that updates the list of books in stock in 'books.txt' file that decreases the quantity of the book that user borrowed. This function returns the new list with the updated quantity.
def updatebooklist():
    global updatedlist
    updatedlist=[]
    for j in range (len(bookname)):
        for k in range (len(lst)):
            if bookname[j] in lst[k][1]:
                newqty=int(lst[k][3])-qnty[j]
                lst[k][3]=str(newqty)                
    updatedlist=lst
    return updatedlist
#function that overwrites the list of books in 'books.txt' file with decreased the quantity of the book that user had borrowed. This function returns nothing.
def overwrite_txt():
    a=updatedlist
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
#function that calculates the total price of the books that the user has borrowed. This function returns nothing.
def totalprice():
    totalprice=0
    for j in range (len(bookname)):
        for k in range (len(lst)):
            if bookname[j] in lst[k][1]:
                price=float(lst[k][4].replace("$",""))
        totalprice+=price
        total = totalprice * qnty[j]
    print("The total price for the books you borrowed is: "+"$"+str(total))
