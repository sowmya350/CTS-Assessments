import unittest

from library_management import Book, LibraryManagementSystem


class LibrarySearchTests(unittest.TestCase):
    def setUp(self) -> None:
        self.library = LibraryManagementSystem(
            [
                Book("The Hobbit", "J.R.R. Tolkien", "9780547928227", 1937),
                Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "9780747532699", 1997),
                Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 1925),
                Book("Pride and Prejudice", "Jane Austen", "9780141439518", 1813),
            ]
        )

    def test_linear_search_by_title(self) -> None:
        results = self.library.search_by_title("harry")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Harry Potter and the Philosopher's Stone")

    def test_linear_search_by_author(self) -> None:
        results = self.library.search_by_author("rowling")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].author, "J.K. Rowling")

    def test_binary_search_by_title(self) -> None:
        result = self.library.search_by_title_binary("The Hobbit")
        self.assertIsNotNone(result)
        self.assertEqual(result.title, "The Hobbit")

    def test_binary_search_missing_title(self) -> None:
        result = self.library.search_by_title_binary("Unknown")
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
