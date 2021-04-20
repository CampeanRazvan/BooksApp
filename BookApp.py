
def add_Book():
    book_name = input("Insert a book title->")
    author_name = input("Insert the author name->")
    # Importing csv libraries
    import csv
    #  deschidem .csv in write mode

    with open('booksDB.csv',mode = "w") as file:
        # fieldnames ---- cap de tabel din dictionarul nostru , am creat capurile de t
        # abel
        writer = csv.DictWriter(file,fieldnames=[
            "BookName" , "AuthorName" , "SharedWith" , "IsRead"
                                                 ])
        #  Introducem date in dictionarul nostru
        writer.writerow({"BookName": book_name,
                         "AuthorName": author_name,
                         "SharedWith": "None",
                         "IsRead": False,
                         })



    print("Book was added successfully")




def list_Books():
    import csv
    with open("booksDB.csv",mode = "r") as file:
        # pasul 1 sa luam toate datele din baza de date
        rows = csv.DictReader(file,fieldnames=("BookName", "AuthorName" , "SharedWith" ,"IsRead" ))

        #  parcurgem rand cu rand
        for row in rows:
            # print(f"Book name is: {row.get('BookName')}")
            # print(f"Author name is: {row.get('AuthorName')}")
            # print(f"The book is shared with: {row.get('SharedWith')}")
            # print(f"Book name is: {row.get('IsRead')},")
                print(
                    f"Book name is: {row.get('BookName')} auth name {row.get('AuthorName')} is shared"
                    f" {row.get('ShareWith')} is read  {row.get('IsRead', False)}")


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

