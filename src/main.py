import library
from customer import Customer
from book import Book

if __name__ == '__main__':
    print('Add new customer')
    customer = Customer('Jane', 'Tel Aviv', age=23)
    library.add_customer(customer)
    library.show_all_customers()

    print('\nAdd new book')
    book = Book('Catch-22', 'Joseph Heller', 'November 10, 1961', book_type=1, copies=5)
    library.add_book(book)
    library.show_all_books()

    print('\nCreate new loan')
    library.create_loan(customer, book)
    library.show_all_loans()

    print('\nShow loans by customer: %s' % customer.get_name())
    library.show_loans_by_customer(customer)

    print('\nShow loans by book: %s' % book.get_name())
    library.show_loans_by_book(book)

    print('\nFind book by name: %s' % book.get_name())
    book1 = library.find_book_by_name(book.get_name())
    print(book1)

    print('\nTry remove book: %s' % book.get_name())
    library.remove_book(book)
    library.show_all_books()

    print('\nTry remove customer: %s' % customer.get_name())
    library.remove_customer(customer)
    library.show_all_customers()

    print('\nClose existing loan: %s %s' % (customer.get_name(), book.get_name()))
    library.close_loan(customer, book)
    library.show_all_loans()

    print('\nTry remove book: %s' % book.get_name())
    library.remove_book(book)
    library.show_all_books()

    print('\nTry remove customer: %s' % customer.get_name())
    library.remove_customer(customer)
    library.show_all_customers()
