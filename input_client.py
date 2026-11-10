import val
import data
def display_books(books):
        for book in books:
                print(book)


def search_book(books, name):
    maches=[]
    for book in books:
        if name in book["name"].lower():
            maches.append(book)
    if maches == []:
        maches = "not found "        
    return maches
        
def add_name(books):
    l_name=False
    while not l_name: 
        name =input("add book name: ")
        if name not in data.books:
            l_name =True
        else:
            raise ("this name ollrady exist ")
    return name

def add_author():
    l_author = False
    while not l_author:
        author = input("enter the author name: ")
        if author != "":
            l_author = True
    return author

def new_id():
    new_id = 1
    for b in data.books:
        if b["id"]>= new_id:
            new_id = new_id+1
    return new_id

def add_book(books, book_id, name, author, year):
    books.append({"id":book_id, "name": name, "author":author, "year": year, "avalable":True})
    

def borrow_book(books, book_id):
    if_w=False
    for book in books:
        if book["id"] == book_id:
            if book["available"] == True:
                book["available"] = False
                if_w = print("borrow sexses")
            else:
                if_w = print("this book olredy borrow")
    if if_w==False:
        if_w =print("this book is not found ")
    return if_w


def return_book(books, book_id):   
    if_b=False
    for book in books:
        if book["id"] == book_id:
            if book["available"] == False:
                book["available"] = True
                if_b = print("return sexses")
            else:
                if_b = print("this book is not borrow")
    if if_b==False:
        if_b =print("this book not found ")
    return if_b       

def get_available_books(books):
    a_books = []
    for book in books:
        if book["available"] == True:
            a_books.append(book)
    return a_books

def get_books_by_author(books, author):
    a_books = []
    for book in books:
        if book["author"] == author:
            a_books.append(book)
    if a_books ==[]:
        a_books = "this outer is not find"
    return a_books