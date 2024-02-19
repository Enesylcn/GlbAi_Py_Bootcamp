from colorama import Fore, Style

class Library:
    def __init__(self):
        self.file = open("books_List.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.read().splitlines()
        if books:
            print("List of Books:")
            for book in books:
                title, author, year, pages = book.split(",")
                print(f"{Fore.BLUE}Title: {title}, {Fore.GREEN}Author: {author}, {Fore.YELLOW}Year: {year}, {Fore.RED}Pages: {pages}{Style.RESET_ALL}")
        else:
            print("No books available.")

    def add_book(self):
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        year = input("Enter the first release year of the book: ")
        pages = input("Enter the number of pages of the book: ")
        book_info = f"{title},{author},{year},{pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        books = self.file.read().splitlines()
        found = False
        for book in books:
            if title in book:
                books.remove(book)
                found = True
                break
        if found:
            self.file.seek(0)
            self.file.truncate()
            for book in books:
                self.file.write(book + "\n")
            print("Book removed successfully.")
        else:
            print("Book not found.")

lib = Library()
while True:
    print(f"\n{Fore.CYAN}___---***  MENU  ***---___{Style.RESET_ALL}")
    print(f"{Fore.CYAN}1) {Style.RESET_ALL}List Books")
    print(f"{Fore.CYAN}2) {Style.RESET_ALL}Add Book")
    print(f"{Fore.CYAN}3) {Style.RESET_ALL}Remove Book")
    print(f"{Fore.CYAN}4) {Style.RESET_ALL}Exit")

    choice = input(f"{Fore.CYAN}Enter your choice (1, 2, 3 or 4): {Style.RESET_ALL}")


    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
