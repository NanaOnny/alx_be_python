# library_system.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            if isinstance(book, Book):
                book_type = "Book"
            elif isinstance(book, EBook):
                book_type = "EBook"
            elif isinstance(book, PrintBook):
                book_type = "PrintBook"
            else:
                book_type = "Unknown"

            if isinstance(book, EBook):
                print(f"{book_type}: {book.title} by {book.author}, File Size: {book.file_size} KB")
            elif isinstance(book, PrintBook):
                print(f"{book_type}: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"{book_type}: {book.title} by {book.author}")