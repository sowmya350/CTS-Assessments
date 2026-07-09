import unittest

from search_engine import ProductSearchEngine


class ProductSearchEngineTests(unittest.TestCase):
    def setUp(self):
        products = [
            {"id": 1, "name": "Wireless Mouse", "category": "Electronics"},
            {"id": 2, "name": "Gaming Keyboard", "category": "Electronics"},
            {"id": 3, "name": "Running Shoes", "category": "Sports"},
            {"id": 4, "name": "Yoga Mat", "category": "Sports"},
            {"id": 5, "name": "Bluetooth Speaker", "category": "Electronics"},
        ]
        self.engine = ProductSearchEngine(products)

    def test_search_returns_matching_products(self):
        results = self.engine.search("mouse")
        self.assertEqual([1], [product["id"] for product in results])

    def test_search_is_case_insensitive(self):
        results = self.engine.search("KEYBOARD")
        self.assertEqual([2], [product["id"] for product in results])

    def test_search_matches_category(self):
        results = self.engine.search("sports")
        self.assertEqual([3, 4], [product["id"] for product in results])

    def test_empty_query_returns_all_products(self):
        results = self.engine.search("")
        self.assertEqual(5, len(results))


if __name__ == "__main__":
    unittest.main()
