class Book:

    def __init__(self, title, author, pages, price):
        self.title = title

        self.author = author
        self.pages = pages
        self.price = price

    def getprice(self):
        return self.price

b1 = Book("War and Peace","Leo Tolstoy", 1225, 39.95)
b2 = Book("The Cather in the Rye","JD Salinger", 234, 29.95)

print(b1.getprice())