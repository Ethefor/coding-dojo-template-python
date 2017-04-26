from .Book import Book


class Basket:
    books = []

    def __init__(self, book=None):
        self.books = []
        if book is not None:
            self.books.append(book)

    def get_quantity(self):
        return len(self.books)

    def get_whole_price(self):
        price = 0

        for book in self.books:
            price += book.price

        return price

    def add_new_book(self, book):
        self.books.append(book)

    def set_list_books(self, books):
        self.books = books