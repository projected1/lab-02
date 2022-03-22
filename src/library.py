from uuid import UUID
from customer import Customer
from book import Book
from loan import Loan

customers = {}
books = {}
loans = []


def add_book(book):
    books[book.get_name()] = book


def add_customer(customer):
    customers[customer.get_id()] = customer


def create_loan(customer, book):
    if not isinstance(customer, Customer):
        raise TypeError('Invalid customer object')

    if not isinstance(book, Book):
        raise TypeError('Invalid book object')

    # Ensure we have enough copies to loan
    if book.get_copies() < 1:
        return 'There are no available copies of %s' % book.get_name()

    # Find all customer loans
    customer_loans = []
    for loan in loans:
        if loan.get_customer() == customer:
            customer_loans.append(loan)

    # Limit the amount of loans per-customer
    if len(customer_loans) > 2:
        return 'Customer reached max amount of loans: %s' % len(customer_loans)

    # No new loans if old loans are overdue
    for loan in customer_loans:
        if loan.is_overdue():
            return 'No new loans until overdue book is returned: %s' % loan.get_book().get_name()

    loan = Loan(customer, book)
    loans.append(loan)

    return loan


def close_loan(customer, book):
    loans = get_all_loans()

    for loan in loans:
        if loan.get_customer() == customer and loan.get_book() == book:
            loans.remove(loan)
            del loan
            return


def get_all_books():
    return list(books.values())


def show_all_books():
    books = get_all_books()

    if not books:
        print('No books')
        return

    for book in books:
        print(book)


def get_all_customers():
    return list(customers.values())


def show_all_customers():
    customers = get_all_customers()

    if not customers:
        print('No customers')
        return

    for customer in customers:
        print(customer)


def get_all_loans():
    return loans


def show_all_loans():
    loans = get_all_loans()

    if len(loans) == 0:
        print('No loans')
        return

    for loan in loans:
        print(loan)


def get_late_loans():
    loans = []

    for loan in get_all_loans():
        if loan.is_overdue():
            loans.append(loan)
    return loans


def show_late_loans():
    for loan in get_late_loans():
        print(loan)


def get_loans_by_customer(customer):
    loans = []

    for loan in get_all_loans():
        if loan.get_customer() == customer:
            loans.append(loan)
    return loans


def show_loans_by_customer(customer):
    for loan in get_loans_by_customer(customer):
        print(loan)


def get_loans_by_book(book):
    loans = []

    for loan in get_all_loans():
        if loan.get_book() == book:
            loans.append(loan)
    return loans


def show_loans_by_book(book):
    for loan in get_loans_by_book(book):
        print(loan)


def find_customer_by_id(customer_id):
    return customers[UUID(str(customer_id))]


def find_book_by_name(book_name):
    return books[book_name]


def remove_book(book):
    for loan in get_all_loans():
        if loan.get_book() == book:
            return
    books.pop(book.get_name())


def remove_customer(customer):
    for loan in get_all_loans():
        if loan.get_customer() == customer:
            return
    customers.pop(customer.get_id())
