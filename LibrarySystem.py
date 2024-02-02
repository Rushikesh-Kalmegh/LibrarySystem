class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print("Books Available in Library:")
        for book in self.books:
            print(book)

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            self.borrowed_books.append(book)
            book.available = False
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"Sorry, {book.title} is not available for borrowing.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True
            print(f"{self.name} returned {book.title}")
        else:
            print(f"You didn't borrow {book.title} from the library.")


# Example:
# library = Library()

# book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")
# book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0061120084")

# library.add_book(book1)
# library.add_book(book2)

# library.display_books()

# member1 = Member("Alice")
# member2 = Member("Bob")

# book_to_borrow = library.search_book("The Great Gatsby")
# member1.borrow_book(book_to_borrow)

# book_to_return = library.search_book("The Great Gatsby")
# member1.return_book(book_to_return)

# library.display_books()
