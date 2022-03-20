import library
from customer import Customer
from book import Book

if __name__ == '__main__':
    print('[v] Add new customer')
    customer = Customer('Jane', 'Tel Aviv', age=23)
    library.add_customer(customer)
    customers = library.get_all_customers()
    assert len(customers) == 1, 'Expected 1 customer but found %s' % len(customers)
    assert customers[0] == customer

    print('[v] Add new book')
    book = Book('Catch-22', 'Joseph Heller', 'November 10, 1961', book_type=1, copies=5)
    library.add_book(book)
    books = library.get_all_books()
    assert len(books) == 1, 'Expected 1 book but found %s' % len(books)
    assert books[0] == book

    print('[v] Create new loan')
    library.create_loan(customer, book)
    loans = library.get_all_loans()
    assert len(loans) == 1, 'Expected 1 loan but found %s' % len(loans)

    print('[v] Get loans by customer: %s' % customer.get_name())
    loans = library.get_loans_by_customer(customer)
    assert len(loans) == 1, 'Expected 1 loan but found %s' % len(loans)

    print('[v] Get loans by book: %s' % book.get_name())
    loans = library.get_loans_by_book(book)
    assert len(loans) == 1, 'Expected 1 loan but found %s' % len(loans)

    print('[v] Get late loans')
    loans = library.get_late_loans()
    assert not loans

    print('[v] Find customer by id: %s' % customer.get_id())
    customer1 = library.find_customer_by_id(customer.get_id())
    assert customer == customer1

    print('[v] Find book by name: %s' % book.get_name())
    book1 = library.find_book_by_name(book.get_name())
    assert book == book1

    print('[v] Fail to remove book: %s' % book.get_name())
    library.remove_book(book)
    books = library.get_all_books()
    assert len(books) == 1, 'Expected 1 book but found %s' % len(books)

    print('[v] Fail to remove customer: %s' % customer.get_name())
    library.remove_customer(customer)
    customers = library.get_all_customers()
    assert len(customers) == 1, 'Expected 1 customer but found %s' % len(customers)

    print('[v] Close existing loan: %s %s' % (customer.get_name(), book.get_name()))
    library.close_loan(customer, book)
    loans = library.get_all_loans()
    assert not loans, 'Expected 0 loan but found %s' % len(loans)

    print('[v] Remove book: %s' % book.get_name())
    library.remove_book(book)
    books = library.get_all_books()
    assert not books, 'Expected 0 book but found %s' % len(books)

    print('[v] Remove customer: %s' % customer.get_name())
    library.remove_customer(customer)
    customers = library.get_all_customers()
    assert not customers, 'Expected 0 customer but found %s' % len(customers)
