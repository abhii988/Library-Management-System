'''
This is the main module of the whole program.
It imports booklist.py, borrow.py and returnbook.py modules in order to access their main functions to display all of the books,
borrow a book and to return a book respectively.
'''
import booklist as l
import borrow as b
import returnbook as r
design='='*95 #declaring a variable to design the program whilst printing
name=input("Please enter your name: ") #taking the name of the user as input
#This function is the main function of the program that runs first and asks the user what he/she wants to do. It then calls the funcitons of different modules according to the user's choice.
def main(): 
     print(design)
     print("\t\t\tHello "+name+". Welcome to the Library!")
     print(design)
     choose=True #declaring the boolean value of choose as true to make the program run in loop
     while choose==True:
          print("""\t\t\t************Library Menu***********\n
          \t\t\ta.Display available books
          \t\t\tb.Borrow a book
          \t\t\tc.Return back a book
          \t\t\td.Exit
           """) #displaying the main menu of the library
          choice=input("What do you want to do? ") #asks for the user's choice
          if choice=='a':
               l.displaylistofbooks() #calls the function from booklist.py module to display the list of books present in the library
          elif choice=='b':
               b.askforbook()  #calls the function from borrow.py module to borrow a book
          elif choice=='c':
               r.return_book()  #calls the function from returnbook.py module to return a book
          elif choice=='d':
               print("Thankyou, come again.")
               exit() #exits out the user from the library
     
main()
