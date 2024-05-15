import os
from Users_class import User
from Authors_class import Author
from Books_class import Book

#                    --------------------------------------User Functions-------------------------------------


def add_user(users):
    name = input('Name: ').title()
    address = input('Address: ').title()
    phone = input('Phone: ')
    new_user = User(name, address, phone)
    users.append(new_user)
    print('User Created')
    new_user.user_info()
    return new_user

def search_users(users):
    if not users:
        print("There are no users in the list.")
    else:
        name = input('Search Name: ').title()
        user_found = False  # Flag to track whether the user is found
        for user in users:
            if user.name == name:
                user.user_info()
                user_found = True

        if not user_found:
            print("User not found")

def display_users(users):
    if not users:
        print("There are no users in the list.")
    else:
        for user in users:
            user.user_info()


def login(users, current_user):
    print('lets log in to Coding Temple Library Management System')
    try:
        option = int(input('''
            Login options
        --------------------
        1. Existing User
        2. New User
        > '''))
    except ValueError:
        print('Please respond only with numbers!')
    else:
        if option == 1:
            username = input("User Name: ")
            if not users:
                print("There are no users in the list.")
            else:
                for user in users:
                    if user.name == username:
                        current_user = user       
                        print("Login successful.") 
                        return current_user 

                else:
                    print("Invalid Username,Try agan")
        elif option == 2:
            current_user = add_user(users)
            return current_user
        else:
            print(f'Sorry {option} is not a valid option')
#             print(f'Let try that again and please respond with only 1 or 2')

            


#                      ---------------------------------Author Functions------------------------------


def add_author(authors):
    name = input('Author Name: ').title()
    new_author = Author(name)
    authors.append(new_author)
    new_author.author_info()
    return new_author

def search_authors(authors):
    if not authors:
        print("There are no authors in the list.")
    else:
        name = input('Search Author: ').title()
        author_found = False  # Flag to track whether the user is found
        for author in authors:
            if author.name == name:
                author.author_info()
                author_found = True
        if not author_found:
            print("No author found")

def display_authors(authors):
    if not authors:
        print("There are no authors in the list.")
    for author in authors:
        author.author_info()


#                       -------------------------------------------Book Functions---------------------------------------

def add_book(books):
    title = input('title: ').title()
    author = input('Author: ').title()
    genre = input('Genre: ').title()
    new_book = Book(title, author,genre)
    books.append(new_book)
    new_book.book_info()

def display_books(books):
    if not books:
        print("Sorry, There are no currently no books in our library.")
    for book in books:
        book.book_info()

def search_books(books):
    if not books:
        print("Sorry, There are no currently no books in our library.")
    else:
        name = input('Search Book: ').title()
        book_found = False  # Flag to track whether the user is found
        for book in books:
            if book.title == name:
                book.book_info()
                book_found = True
        if not book_found:
            print("No book found")

def checkout_book(books, current_user):
    for book in books:
        if book.available is True:
            book.book_info()
    title = input("Enter the title of the book you want to borrow: ").title()
    for book in books:
        if book.title == title:
            if book.available:
                current_user.borrowed_books.append(book)
                book.available = False
                print(f"{current_user.name} has borrowed '{book.title}'.")
                return current_user
            else:
                print(f"Sorry, '{book.title}' is not available for borrowing.")


def return_book(books, current_user):
    if not current_user.borrowed_books:
        print("You haven't borrowed any books.")
        return
    for index, book in enumerate(current_user.borrowed_books, start=1):
        print(f"{index}. {book.title}")
    title = input("Enter the title of the book you want to return: ").title()
    found = False
    for book in books:
        if book.title == title and book in current_user.borrowed_books:
            found = True
        current_user.borrowed_books.remove(book)
        book.available = True
        print(f"Book '{title}' returned successfully.")
        break

    if not found:
        print(f"Sorry, book '{title}' not found in your borrowed books.")

    # for book in books:
    #     if book.available is False:
    #         book.book_info()
    #     title = input("Enter the title of the book you want to return: ").title()
    #     for book in books:
    #         if book.title == title and book in current_user.borrowed_books
                



#                         -------------------------------Command line Interface(Menu Options)-------------------------


def author_options(authors):
    while True:
        try:
            option = int(input(''' 
                Author Options:
            -----------------------
                1. Add a new author
                2. View author details
                3. Display all authors
                4. Main Menu
                > '''))
        except ValueError:
            print('Please respond only with numbers!')

        else:
            if option == 1:
                os.system('cls')
                add_author(authors)
            elif option == 2:
                os.system('cls')
                search_authors(authors)
            elif option == 3:
                os.system('cls')
                display_authors(authors)
            elif option == 4:
                os.system('cls')
                print('Returning to main menu')
                break
            else:
                os.system('cls')
                print(f'Sorry {option} is not a valid option')
                print(f'Let try that again and please respond with only 1,2, 3 or 4')



def user_options(users):
    while True:
        try:
            option = int(input(''' 
                User Options:
            -----------------------
                1. Add a new user
                2. View user details
                3. Display all users
                4. Main Menu
                > '''))
        except ValueError:
            print('Please respond only with numbers!')
        else:
            if option == 1:
                os.system('cls')
                current_user = add_user(users)
                return current_user
            elif option == 2:
                os.system('cls')
                search_users(users)
            elif option == 3:
                os.system('cls')
                display_users(users)
            elif option == 4:
                os.system('cls')
                print('returning to main menu')
                break
            else:
                os.system('cls')
                print(f'Sorry {option} is not a valid option')
                print(f'Let try that again and please respond with only 1,2, 3 or 4')





def book_options(books, current_user):
    while True:
        try:
            option = int(input(''' 
                book Options:
            -----------------------
                1. Add a new book
                2. Borrow a book
                3. Return a book
                4. Search for a book
                5. Display all books
                6. Main Menu
                > '''))
        except ValueError:
            print('Please respond only with numbers!')

        else:
            if option == 1:
                os.system('cls')
                add_book(books)
            elif option == 2:
                os.system('cls')
                checkout_book(books, current_user)
            elif option == 3:
               return_book(books, current_user)
            elif option == 4:
                os.system('cls')
                search_books(books)
            elif option == 5:
                os.system('cls')
                display_books(books)
            elif option == 6:
                os.system('cls')
                print('returning to main menu')
                break
            else:
                os.system('cls')
                print(f'Sorry {option} is not a valid option')
                print(f'Let try that again and please respond with only 1, 2, 3, 4, 5 or 6')







def library_menu():

    users = []
    authors = []
    books = []
    current_user = None
    #login(users, current_user)
    print( "Welcome to the Coding Temple Library Management System!")
    while True:
        try:
            option = int(input(''' 
                Main Menu:
            ------------------
            1. Book Options
            2. User Options
            3. Author Options
            4. Exit Library
            > '''))

        except ValueError:
            print('Please respond only with numbers!')
        else:
            if option == 1:
                os.system('cls')
                book_options(books,current_user)
                pass
            elif option == 2:
                os.system('cls')
                current_user = user_options(users)
            elif option == 3:
                os.system('cls')
                author_options(authors)
                pass
            elif option == 4:
                os.system('cls')
                print('Exiting library')
                print('Thank you have a nice day')
                break
            else:
                print(f'Sorry {option} is not a valid option')
                print(f'Let try that again and please respond with only 1,2,3 or 4')

library_menu()


