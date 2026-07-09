from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Book:
    title: str
    author: str
    isbn: str
    year: int


class LibraryManagementSystem:
    def __init__(self, books: Optional[List[Book]] = None):
        self.books = books or []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def search_by_title(self, keyword: str) -> List[Book]:
        keyword = keyword.lower().strip()
        return [book for book in self.books if keyword in book.title.lower()]

    def search_by_author(self, keyword: str) -> List[Book]:
        keyword = keyword.lower().strip()
        return [book for book in self.books if keyword in book.author.lower()]

    def search_by_title_binary(self, title: str) -> Optional[Book]:
        sorted_books = sorted(self.books, key=lambda book: book.title.lower())
        left = 0
        right = len(sorted_books) - 1
        target = title.lower().strip()

        while left <= right:
            mid = (left + right) // 2
            current_title = sorted_books[mid].title.lower()

            if current_title == target:
                return sorted_books[mid]
            if current_title < target:
                left = mid + 1
            else:
                right = mid - 1

        return None

    def search_by_author_binary(self, author: str) -> Optional[Book]:
        sorted_books = sorted(self.books, key=lambda book: book.author.lower())
        left = 0
        right = len(sorted_books) - 1
        target = author.lower().strip()

        while left <= right:
            mid = (left + right) // 2
            current_author = sorted_books[mid].author.lower()

            if current_author == target:
                return sorted_books[mid]
            if current_author < target:
                left = mid + 1
            else:
                right = mid - 1

        return None


def main() -> None:
    library = LibraryManagementSystem()
    library.add_book(Book("The Hobbit", "J.R.R. Tolkien", "9780547928227", 1937))
    library.add_book(Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "9780747532699", 1997))
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 1925))
    library.add_book(Book("Pride and Prejudice", "Jane Austen", "9780141439518", 1813))

    print("Books matching 'the':")
    for book in library.search_by_title("the"):
        print(f"- {book.title} by {book.author}")

    print("\nBooks by 'rowling':")
    for book in library.search_by_author("rowling"):
        print(f"- {book.title} by {book.author}")

    print("\nBinary search for 'The Hobbit':")
    found = library.search_by_title_binary("The Hobbit")
    if found:
        print(f"Found: {found.title} by {found.author}")
    else:
        print("No matching book found.")


if __name__ == "__main__":
    main()
