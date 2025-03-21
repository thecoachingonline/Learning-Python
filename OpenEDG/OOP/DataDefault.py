from dataclasses import dataclass, field
import random


def price_func():
    return float(random.randrange(20, 40))


@dataclass
class Book:
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0
    price: float = field(default_factory=price_func)


b1 = Book()
print(b1)

b1 = Book("War and Peace", "Leo Tolstoy", 1225)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234)
print(b1)
print(b2)