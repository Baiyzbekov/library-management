from models.library import Library
from models.book import Book
from models.author import Author
from models.user import User

def main():
    library = Library("Biblioteka Uniwersytecka")

    author = Author("George Orwell", 1903, "British")
    book = Book("1984", "123456789", [author], 1949, "Secker & Warburg")

    user = User(1, "Alice", "alice@example.com")

    library.add_book(book)
    library.register_user(user)

    # Borrow book
    loan = library.lend_book(book, user)
    print("Loan created:", loan)

    # Return book
    library.return_book(book, user)
    print("Book returned")

if __name__ == "__main__":
    main()