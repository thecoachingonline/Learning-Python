class Book:

    def __init__(self, title, author, pages, price):
        self.title = title

        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret attribute"

    def getprice(self):
        if hasattr(self,"_discount"):
            return self.price - (self.price * self._discount)
        elif:
            return self.price
        
    def setdiscount(self, amount):
        self._discount = amount


b1 = Book("War and Peace","Leo Tolstoy", 1225, 39.95)
b2 = Book("The Cather in the Rye","JD Salinger", 234, 29.95)

print(b1.getprice())

#print(b2.getprice())
#b2.setdiscount(0.25)
#print(b2.getprice())

print(b2.__Book__secret)


#๘