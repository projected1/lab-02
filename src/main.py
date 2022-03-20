import library
from customer import Customer
from book import Book

if __name__ == '__main__':
    while True:

        print('''
        **** Hello Librarian, Please enter your choice ****
        1.  Add a new customer
        2.  Add a new book
        3.  Loan a book
        4.  Return a book
        5.  Display all books
        6.  Display all customers
        7.  Display all loans
        8.  Display late loans
        9.  Display loans by customer
        10. Display loans by book
        11. Display book details
        12. Display customer details
        13. Remove book
        14. Remove customer
        15. Exit the program
        ''')

        try:
            choice = int(input('Enter your choice: '))
        except ValueError:
            print('Please enter a valid number')
            continue

        if choice < 1 or choice > 15:
            print('Please enter a valid number between 1 and 14')
            continue

        if choice == 1:
            name = input('Enter customer name - ')
            city = input('Enter a customer city of residence - ')
            age = int(input('Enter customers age - '))
            customer = Customer(name, city, age)
            library.add_customer(customer)
            print(customer)
            continue

        elif choice == 2:
            name = input('Enter book name - ')
            author = input('Enter author name - ')
            publish_date = input('Enter publish date - ')
            book_type = int(input('Enter type (1/2/3) - '))
            copies = int(input('Enter a number of copies - '))
            book = Book(name, author, publish_date, book_type, copies)
            library.add_book(book)
            print(book)
            continue

        elif choice == 3:
            customer_id = input('Enter customer id - ')
            book_name = input('Enter book name - ')
            customer = library.find_customer_by_id(customer_id)
            book = library.find_book_by_name(book_name)
            loan = library.create_loan(customer, book)
            print(loan)
            continue

        elif choice == 4:
            customer_id = input('Enter a customer id - ')
            book_name = input('Enter book name - ')
            customer = library.find_customer_by_id(customer_id)
            book = library.find_book_by_name(book_name)
            library.close_loan(customer, book)
            continue

        elif choice == 5:
            library.show_all_books()
            continue

        elif choice == 6:
            library.show_all_customers()
            continue

        elif choice == 7:
            library.show_all_loans()
            continue

        elif choice == 8:
            library.show_late_loans()
            continue

        elif choice == 9:
            customer_id = input('Enter customer id - ')
            customer = library.find_customer_by_id(customer_id)
            library.show_loans_by_customer(customer)
            continue

        elif choice == 10:
            book_name = input('Enter book name - ')
            book = library.find_book_by_name(book_name)
            library.show_loans_by_book(book)
            continue

        elif choice == 11:
            book_name = input('Enter book name - ')
            book = library.find_book_by_name(book_name)
            print(book)
            continue

        elif choice == 12:
            customer_id = input('Enter customer id - ')
            customer = library.find_customer_by_id(customer_id)
            print(customer)
            continue

        elif choice == 13:
            book_name = input('Enter book name - ')
            book = library.find_book_by_name(book_name)
            library.remove_book(book)
            continue

        elif choice == 14:
            customer_id = input('Enter customer id - ')
            customer = library.find_customer_by_id(customer_id)
            library.remove_customer(customer)
            continue

        elif choice == 15:
            print('Thank you for using our awesome library!')
            break
