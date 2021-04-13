
def add_Book():
    print("Here we add a book")

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

