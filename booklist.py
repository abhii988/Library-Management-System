'''
This module reads the list of books from the file 'books.txt' to show the stock of  books present in the library and converts it into a 2D list in order to make the list of books print in a readable format for the user.
'''
design='='*95 #declaring a variable to design the program whilst printing
dash='-'*95 #declaring a variable to design the program whilst printing
l=[] #declaring an empty list
#function that reads the stock of books from books.txt file. This function returns content of books.txt.
def readlistofbooks():
    file=open("books.txt","r")
    content=file.readlines()
    file.close()
    return content

books=readlistofbooks()
#function that splits and replace's the values to keep in 2D list. This function returns nothing.
for i in range(len(books)):
    l.append(books[i].replace("\n","").split(","))
#function to save the value of list 'l' to 'listofbooks'. This function returns nothing.
def listing2d():
     listofbooks=l
     return listofbooks
#function to show the list of books and prints them in a readable format using formatters and designs. This function returns nothing.
def displaylistofbooks():
    print(design)
    print("\t"*3+"The books available in our library are:")
    print(design)
    print("Book ID\t\tName\t\t\tAuthor\t\t\tQuantity\tPrice")
    print(dash)
    for j in range(len(l)):
        print()
        for k in range(len(l[i])):
            print(l[j][k],end="\t\t")
    print()
    print(dash)
    print()
