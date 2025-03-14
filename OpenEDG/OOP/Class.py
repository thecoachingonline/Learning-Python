class Book:
    BOOK_TYPES = ("HERDCOVER","PAPERBACK","EBOOK")

    __booklist = None

    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES
    
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist


    def set_title(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype


print("Book types: ", Book.get_book_types())

b1 = Book("Titlel", "HARDCOVER")
b2 = Book("Titlel", "COMIC")

thebook = Book.getbooklist()
thebook.append(b1)

print(thebook)