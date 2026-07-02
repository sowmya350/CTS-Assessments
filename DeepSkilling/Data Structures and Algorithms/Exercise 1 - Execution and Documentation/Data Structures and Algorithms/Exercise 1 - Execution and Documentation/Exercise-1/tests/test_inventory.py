import os
import shutil
import tempfile
import unittest

from inventory_management import InventoryManager


class InventoryManagerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.temp_dir, "inventory.db")
        self.manager = InventoryManager(self.db_path)

    def tearDown(self) -> None:
        self.manager.close()
        shutil.rmtree(self.temp_dir)

    def test_add_and_list_items(self) -> None:
        item_id = self.manager.add_item("Laptop", 10, 999.99)

        items = self.manager.list_items()

        self.assertEqual(item_id, 1)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["name"], "Laptop")
        self.assertEqual(items[0]["quantity"], 10)
        self.assertEqual(items[0]["price"], 999.99)

    def test_update_item(self) -> None:
        self.manager.add_item("Mouse", 5, 19.99)
        self.manager.update_item(1, quantity=8, price=24.99)

        item = self.manager.get_item(1)

        self.assertIsNotNone(item)
        self.assertEqual(item["quantity"], 8)
        self.assertEqual(item["price"], 24.99)

    def test_remove_item(self) -> None:
        self.manager.add_item("Keyboard", 3, 49.50)
        removed = self.manager.remove_item(1)

        self.assertTrue(removed)
        self.assertEqual(self.manager.list_items(), [])

    def test_search_items(self) -> None:
        self.manager.add_item("Keyboard", 3, 49.50)
        self.manager.add_item("Laptop", 2, 799.00)

        results = self.manager.search_items("key")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "Keyboard")

    def test_add_item_with_explicit_id(self) -> None:
        item_id = self.manager.add_item("Laptop", 10, 50000.0, 101)

        item = self.manager.get_item(101)

        self.assertEqual(item_id, 101)
        self.assertIsNotNone(item)
        self.assertEqual(item["name"], "Laptop")


if __name__ == "__main__":
    unittest.main()
