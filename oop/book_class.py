class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        print(f"Deleting {self.title}")

b = Book("1984", "George Orwell", 1949)

# Import the Book class from book.py
#from book import Book

#def main():
    # Create an instance of the Book class
 #   my_book = Book("1984", "George Orwell", 1949)

    # Test the __str__ method
  #  print("Testing __str__ method:")
   # print(my_book)

    # Test the __repr__ method
    #print("\nTesting __repr__ method:")
   # print(repr(my_book))

#if __name__ == "__main__":
 #   main()


