from datetime import datetime, timedelta

class Loan:
    def __init__(self, book, user, loan_days=14):
        self.book = book
        self.user = user
        self.loan_date = datetime.now()
        self.due_date = self.loan_date + timedelta(days=loan_days)
        self.returned = False

    def mark_returned(self):
        self.returned = True
        self.book.mark_returned()

    def is_overdue(self):
        return datetime.now() > self.due_date and not self.returned

    def __repr__(self):
        return f"Loan(book={self.book.title}, user={self.user.name})"