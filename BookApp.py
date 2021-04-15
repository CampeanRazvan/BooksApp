
def add_Book():
    book_name = input("Insert a book title->")
    author_name = input("Insert the author name->")
    # Importing csv libraries
    import csv
    #  deschidem .csv in write mode
    with open('booksDB.csv',"w") as file:
        # fieldnames ---- cap de tabel din dictionarul nostru , am creat capurile de tabel
        writer = csv.DictWriter(file,fieldnames=[
            "BookName" , "AuthorName" , "SharedWith" , "IsRead"
                                                 ])
        #  Introducem date in dictionarul nostru
        writer.writerow({"BookName": book_name ,
                         "AuthorName": author_name,
                         })
    print("Book was added successfully")




def list_Books():
    print("Here we list the books")

def update_Book():
    print("Here we update a book")

def share_Book():
    print("Here we share a book")



#  Main menu for user
print("Menu : ")
print("""1 : Add a book 
2 : List the books
3 : Update a book
4 : Share a book
""")
option = int(input("Select one optin -> "))
if option == 1:
    add_Book()
elif option == 2:
    list_Books()
elif option == 3:
    update_Book()
elif option == 4:
    share_Book()
else:
    print("Not a valid option  ")

