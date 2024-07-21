class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        print(f"Deleting {self.title}")

    def __str__(self):
        return f"Title = {self.title} by Author = {self.author},published in Year = {self.year}."

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

#    def __del__(self):
#        print(f"Deleting {self.title}.")

b = Book("1984", "George Orwell", 1949)

# Import the Book class from book.py
from book import Book

def main():
    # Create an instance of the Book class
    my_book = Book("1984", "George Orwell", 1949)

    # Test the __str__ method
    print("Testing __str__ method:")
    print(my_book)

    # Test the __repr__ method
    print("\nTesting __repr__ method:")
    print(repr(my_book))

if __name__ == "__main__":
    main()


