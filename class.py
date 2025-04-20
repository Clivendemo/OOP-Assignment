# Base class
class Book:
    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self._genre = genre  # Encapsulated attribute

    def describe(self):
        print(f"'{self.title}' is a {self._genre} book written by {self.author} with {self.pages} pages.")

    def read(self):
        print(f"Reading '{self.title}'...")

# Subclass with polymorphism applied
class Textbook(Book):
    def read(self):
        print(f"Studying from the textbook '{self.title}' by {self.author}...")

class Novel(Book):
    def read(self):
        print(f"Reading the story Book '{self.title}' by {self.author}...")
 
# Testing
book1 = Textbook("The river and the Source", "Magret Ogola", 350, "Educational")
book2 = Novel("Siku Njema", "Ken Walibora", 280, "Adventure")

book1.describe()
book1.read()

book2.describe()
book2.read()