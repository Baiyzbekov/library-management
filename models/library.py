from models.loan import Loan

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.users = []
        self.employees = []
        self.loans = []

    def add_book(self, book):
        self.books.append(book)

    def register_user(self, user):
        self.users.append(user)

    def hire_employee(self, employee):
        self.employees.append(employee)

    def lend_book(self, book, user):
        if book.is_available():
            loan = Loan(book, user)
            self.loans.append(loan)
            book.mark_borrowed()
            user.borrow_book(book)
            return loan
        else:
            raise Exception("Book is not available")

    def return_book(self, book, user):
        for loan in self.loans:
            if loan.book == book and loan.user == user and not loan.returned:
                loan.mark_returned()
                user.return_book(book)
                return loan
        raise Exception("Loan not found")

    def list_available_books(self):
        return [book for book in self.books if book.is_available()]

    def __repr__(self):
        return f"Library(name={self.name})"