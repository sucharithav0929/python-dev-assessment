class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def get_age(self):
        current_year = 2025
        return current_year - self.publication_year

    def get_summary(self):
        return f' Title: {self.title} Author: {self.author} Published: {self.publication_year}'


book1 = Book("To kill a Mockingbird", "Harper Lee", "58945892306", 1960)
book2 = Book("Pride and Prejudice", "Jane Austen", "68688258626", 1813)
book3 = Book("Little Women", "Louisa", "6653044930665", 1869)

print("Book 1")
print("Title:", book1.title)
print("Author:", book1.author)
print("Age:", book1.get_age(), "years")
print("Summary:", book1.get_summary(), "\n")


print("Book 2")
print("Title:", book2.title)
print("Author:", book2.author)
print("Age:", book2.get_age(), "years")
print("Summary:", book2.get_summary())
