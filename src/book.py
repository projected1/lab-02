from datetime import datetime

book_type_to_loan_days = (10, 5, 2)


class Book:
    def __init__(self, name, author, publish_date, book_type, copies):
        self.name = name
        self.author = author
        self.publish_date = datetime.strptime(publish_date, '%B %d, %Y')
        self.loan_days = book_type_to_loan_days[book_type]
        self.existing_copies = copies
        self.remaining_copies = copies

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return 'Book name: %s, author: %s, publish_date: %s, loan_days: %s, copies: %d' % \
            (self.name, self.author, self.publish_date, self.loan_days, self.remaining_copies)

    def get_name(self):
        return self.name

    def get_loan_days(self):
        return self.loan_days

    def get_copies(self):
        return self.remaining_copies

    def get_copy(self):
        if self.remaining_copies > 0:
            self.remaining_copies -= 1
            return self

    def add_copy(self):
        if self.remaining_copies < self.existing_copies:
            self.remaining_copies += 1
