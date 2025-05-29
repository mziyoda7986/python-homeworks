class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book: Book):
        if len(self.borrowed_books) > 2:
            raise MemberLimitExceededException("Cannot borrow more than 3 books!")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"{book.title} already borrowed!")
        
        book.is_borrowed = True
        self.borrowed_books.append(book)
        print(f"{self.name} borrowed {book.title}.")
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}.")
        else:
            print(f"{self.name} does not have {book.title}.")

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book: Book):
        self.books.append(book)
        print(f"Added book: {book.title}")

    def add_member(self, member:Member):
        self.members.append(member)
        print(f"Added member: {member.name}")
    
    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"{title} not found in the library!")
    def find_member(self, name):
        for mem in self.members:
            if mem.name == name:
                return mem
        print(f"{name} not found!")
        return None
    
    def borrow_book(self, name, title):
        member = self.find_member(name)
        if not member:
            return
        try:
            book = self.find_book(title)
            member.borrow_book(book)
        except (BookAlreadyBorrowedException, BookNotFoundException, MemberLimitExceededException) as ex:
            print("Error:", ex)
        
    def return_book(self, name, title):
        member = self.find_member(name)
        if not member:
            return
        try:
            book = self.find_book(title)
            member.return_book(book)
        except (BookAlreadyBorrowedException, BookNotFoundException, MemberLimitExceededException) as ex:
            print("Error:", ex)

lib = Library()

# Add books
lib.add_book(Book("1984", "George Orwell"))
lib.add_book(Book("The Hobbit", "J.R.R. Tolkien"))
lib.add_book(Book("Dune", "Frank Herbert"))

# Add members
lib.add_member(Member("Alice"))
lib.add_member(Member("Bob"))

# Borrow books
lib.borrow_book("Alice", "1984")
lib.borrow_book("Alice", "The Hobbit")
lib.borrow_book("Alice", "Dune")

# Try to exceed book limit
lib.add_book(Book("Brave New World", "Aldous Huxley"))
lib.borrow_book("Alice", "Brave New World")  # Should raise MemberLimitExceededException

# Try to borrow a book already borrowed
lib.borrow_book("Bob", "1984")  # Should raise BookAlreadyBorrowedException

# Try to borrow a non-existent book
lib.borrow_book("Bob", "Invisible Man")  # Should raise BookNotFoundException

# Return a book and borrow again
lib.return_book("Alice", "1984")
lib.borrow_book("Bob", "1984")  # Should now be successful