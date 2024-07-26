class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, authclass Book:
    def __init__(self, title : str, author : str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"
    
class EBook(Book):
    def __init__(self, title: str, author: str, file_size : int):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count : int):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self, books = None):
        if books is None:
            self.books = []
        else:
            self.books = books
    
    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)or, file_size):
        self.file_sie = file_size
            return int"{self.file_size}"

class PrintBook(Book):
    def__init__(self, title, author, page_count):
        self.page_count = page_count
            return int"{self.page_count}"
