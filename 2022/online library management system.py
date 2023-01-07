
# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# HarryLibrary = Library(listofbooks, library_name)


#dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input

class Library :
    def __init__(self,list,name): #constructor
        self.booksList=list
        self.name=name
        self.lendDict={} # blank dictonary to add books

    def displayBooks(self):
        print(f"we have following books in library:{self.name}")
        for book in self.booksList:
            print(book)

    def lendbook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print(" Lender book has been updated.you can take the book now")
        else :
            print(f"book is already used by :{self.lendDict[book]}")
    
    def addbook(self,book):
        self.booksList.append(book)
        print("Book has been added to book list")

    def returnbook(self,book):
        self.lendDict.pop(book)


if __name__=='__main__':
    mylibrary=Library(['mylibrary Potter','Alice in Wonderland','Gulliver’s Travels','Alchemist','Middle March','The Lord of the Rings']," Great Kingdom!")
    
    while(True):
        print(f"welcome to the {mylibrary.name} library. \n Enter your choice to continue:")
        print("1.Display")
        print("2.Lend")   
        print("3.Add")
        print("4.Return")
        userchoice=input()
        if userchoice not in ['1','2','3','4'] :
            print("Please enter a valid option! ")
            continue
        else:
            userchoice=int(userchoice)
        
        if userchoice==1:
            mylibrary.displayBooks()

        elif userchoice==2:
            book=input("Enter the book u want to lend:")  
            user=input("Enter the name:")
            mylibrary.lendbook(user,book)

        elif userchoice==3:
            book=input("Enter the book u want to add:")
            mylibrary.addbook(book)

        elif userchoice==4:
            book=input("Enter name of book to return:")
            mylibrary.returnbook(book) 
        else :
            print("Not a valid option")    
            
        print("Press q to quit and c to continue:")
        userchoice2=""
        while(userchoice2!="c" and userchoice2!="q"):
            userchoice2=input()
        if userchoice2=="q" or "Q":
            exit()
        elif userchoice2=="c"  or "C":
            continue
