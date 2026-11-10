import data
import input_client
import val
def main():
    wont_exit = False
    while not wont_exit:
        client_choice =input("""
================================
        LIBRARY MANAGEMENT
================================

1. Display all books
2. Search book by name
3. Add new book
4. Borrow a book
5. Return a book
6. Display available books
7. Display books by author
8. Exit

Choose an option:

    """)
        if client_choice == "8":
            wont_exit = True
        elif client_choice == "1":
                input_client.display_books(data.books)
        elif client_choice == "2":
                name = input("enter the book name: ").lower()
                print(input_client.search_book(data.books, name))                
        elif client_choice == "3":
            input_client.add_book(data.books, input_client.new_id(), input_client.add_name(data.books), input_client.add_author(), val.add_int("enter the book year: ") )
            print("book save ")
        elif client_choice == "4":
            input_client.borrow_book(data.books,val.add_int("enter the book id: "))
        elif client_choice == "5":
            input_client.return_book(data.books,val.add_int("enter the book id: "))
        elif client_choice == "6":
            print(input_client.get_available_books(data.books))
        elif client_choice == "7":
            print (input_client.get_books_by_author(data.books,val.add_str("enter the auter name: ")))
        else:
            print("chose a legal coice ")





main()