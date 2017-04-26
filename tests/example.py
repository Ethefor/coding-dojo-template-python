import unittest

from classes.Basket import Basket
from classes.Book import Book


class ExampleTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual(1, 1)

    def test_empty_basket(self):
        basket = Basket()
        self.assertEqual(basket.get_quantity(), 0)

    def test_create_book(self):
        book = Book('HP1', 8)

    def test_add_to_basket(self):
        book = Book('HP1', 8)
        basket = Basket(book)
        self.assertEqual(basket.get_quantity(), 1)

    def test_price_for_one_book(self):
        price = 8
        book = Book('HP1', price)
        basket = Basket(book)
        self.assertEqual(basket.get_whole_price(), price)

    def test_add_book_to_basket(self):
        book = Book('HP2', 8)
        basket = Basket()
        basket.add_new_book(book)
        self.assertEqual(basket.get_quantity(), 1)

    def test_add_same_type_books(self):
        book = Book('HP3', 8)
        basket = Basket()

        for i in range(5):
            basket.add_new_book(book)

        self.assertEqual(basket.get_whole_price(), 40)

    def test_add_different_books(self):
        # book1 = Book('HP1', 8)
        # book2 = Book('HP2', 8)
        # book3 = Book('HP3', 8)
        # book4 = Book('HP4', 8)

        price = 8
        listBooks = [Book('HP1', price), Book('HP2', price), Book('HP3', price), Book('HP4', price)]
        basket = Basket()
        basket.set_list_books(listBooks)
        self.assertEqual(basket.get_quantity(), len(listBooks))
        self.assertEqual(basket.get_whole_price(), 0.8*(price*len(listBooks)))



if __name__ == '__main__':
    unittest.main()
