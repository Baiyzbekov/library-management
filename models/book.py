from utils.enums import BookStatus

class Book:
    def __init__(self, title, isbn, authors, publication_year, publisher):
        self.title = title
        self.isbn = isbn
        self.authors = authors  # list of Author objects
        self.publication_year = publication_year
        self.publisher = publisher
        self.status = BookStatus.AVAILABLE

    def is_available(self):
        return self.status == BookStatus.AVAILABLE

    def mark_borrowed(self):
        self.status = BookStatus.BORROWED

    def mark_returned(self):
        self.status = BookStatus.AVAILABLE

    def __repr__(self):
        return f"Book(title={self.title}, isbn={self.isbn})"