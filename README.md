# lab-02

In this project you will implement a simple system to manage books library.

1. Your system should be able to manage the following entities:
    - Books
        - Id (Unique)
        - Name
        - Author
        - Year Published
        - Type (1/2/3)
        - Number of copies in the library
    - Customers
        - Id (Unique)
        - Name
        - City
        - Age
        - Customer Loans
    - Loans
        - CustId
        - BookId
        - LoanDate
        - ReturnDate

2. The book type sets the maximum loan time for the book:
    - 1 - up to 10 days
    - 2 - up to 5 days
    - 3 - up to 2 days

3. Create the infrastructure for the library system:
    - Build a class for each entity
    - Create a separate module for each class
    - Make sure every time you start your program, it loads all the data from a file, and each time you exit your program, all the data is stored to a file and not lost.

4. Build a client application to use your library system. Add the following operations (display a simple menu).
    - Add a new customer
    - Add a new book
    - Loan a book - A customer may only take out up to 3 books at a time. If a customer already has a book that he has loaned and did not return it on time, do not allow them to loan a new one: at least 2 weeks should pass between the last time a customer returned a book late and when they can loan an new one (as punishment for not returning book on time).
    - Return a book - if a customer returns a book late, your should display a relevant message that states that he will not be able to loan a book in upcoming 2 weeks.
    - Display all books
    - Display all customers
    - Display all loans
    - Display late loans
    - Display loans by customer
    - Display loans by book
    - Find book by name
    - Display book details (for a specific book)
    - Find customer details (for a specific customer)
    - Remove book - a book can be removed only if all it's copies are now in a library (you might want to add a field to the Books/Book class to help with this)
    - Remove customer - a customer can be removed only if he has returned all the books to the library.
