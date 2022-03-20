from loan import Loan

customers = []
books = []
loans = []


def add_book(book):
    books.append(book)


def add_customer(customer):
    customers.append(customer)


def create_loan(customer, book):
    customer_loans = []

    # Find all customer loans
    for loan in loans:
        if loan.get_customer() == customer:
            customer_loans.append(loan)

    if len(customer_loans) > 2:
        return

    for loan in customer_loans:
        if loan.is_overdue():
            return

    loan = Loan(customer, book)
    loans.append(loan)


def close_loan(customer, book):
    loans = get_all_loans()

    for loan in loans:
        if loan.get_customer() == customer and loan.get_book() == book:
            loans.remove(loan)
            return


def get_all_books():
    return books


def show_all_books():
    books = get_all_books()

    if len(books) == 0:
        print('No books')
        return

    for book in books:
        print(book)


def get_all_customers():
    return customers


def show_all_customers():
    customers = get_all_customers()

    if len(customers) == 0:
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


def show_late_loans():
    for loan in get_all_loans():
        if loan.is_late():
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


def find_book_by_name(book_name):
    for book in get_all_books():
        if book.get_name() == book_name:
            return book


def remove_book(book):
    for loan in get_all_loans():
        if loan.get_book() == book:
            return
    books.remove(book)


def remove_customer(customer):
    for loan in get_all_loans():
        if loan.get_customer() == customer:
            return
    customers.remove(customer)
