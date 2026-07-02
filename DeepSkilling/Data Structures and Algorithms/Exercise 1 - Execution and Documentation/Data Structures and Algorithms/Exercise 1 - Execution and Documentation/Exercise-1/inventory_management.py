import argparse
import sqlite3
from typing import List, Optional, Dict
from dataclasses import dataclass


class InventoryManager:
    def __init__(self, db_path: str = "inventory.db"):
        self.db_path = db_path
        self.init_db()

    def __del__(self) -> None:
        self.close()

    def close(self) -> None:
        if hasattr(self, "_connection") and self._connection is not None:
            self._connection.close()
            self._connection = None

    def init_db(self) -> None:
        conn = sqlite3.connect(self.db_path)
        try:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    quantity INTEGER NOT NULL CHECK (quantity >= 0),
                    price REAL NOT NULL CHECK (price >= 0)
                )
                """
            )
            conn.commit()
        finally:
            conn.close()

    def add_item(self, name: str, quantity: int, price: float, item_id: Optional[int] = None) -> int:
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if item_id is not None and item_id < 0:
            raise ValueError("Item ID cannot be negative")

        conn = sqlite3.connect(self.db_path)
        try:
            if item_id is None:
                cursor = conn.execute(
                    "INSERT INTO items (name, quantity, price) VALUES (?, ?, ?)",
                    (name, quantity, price),
                )
            else:
                cursor = conn.execute(
                    "INSERT INTO items (id, name, quantity, price) VALUES (?, ?, ?, ?)",
                    (item_id, name, quantity, price),
                )
            conn.commit()
            return cursor.lastrowid if item_id is None else item_id
        finally:
            conn.close()

    def get_item(self, item_id: int) -> Optional[dict]:
        conn = sqlite3.connect(self.db_path)
        try:
            row = conn.execute(
                "SELECT id, name, quantity, price FROM items WHERE id = ?",
                (item_id,),
            ).fetchone()
        finally:
            conn.close()

        if row is None:
            return None

        return {"id": row[0], "name": row[1], "quantity": row[2], "price": row[3]}

    def list_items(self) -> List[dict]:
        conn = sqlite3.connect(self.db_path)
        try:
            rows = conn.execute(
                "SELECT id, name, quantity, price FROM items ORDER BY id"
            ).fetchall()
        finally:
            conn.close()

        return [
            {"id": row[0], "name": row[1], "quantity": row[2], "price": row[3]}
            for row in rows
        ]

    def update_item(self, item_id: int, quantity: Optional[int] = None, price: Optional[float] = None) -> None:
        if quantity is not None and quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if price is not None and price < 0:
            raise ValueError("Price cannot be negative")

        updates = []
        values = []

        if quantity is not None:
            updates.append("quantity = ?")
            values.append(quantity)
        if price is not None:
            updates.append("price = ?")
            values.append(price)

        if not updates:
            return

        values.append(item_id)
        conn = sqlite3.connect(self.db_path)
        try:
            conn.execute(f"UPDATE items SET {', '.join(updates)} WHERE id = ?", values)
            conn.commit()
        finally:
            conn.close()

    def remove_item(self, item_id: int) -> bool:
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.execute("DELETE FROM items WHERE id = ?", (item_id,))
            conn.commit()
            return cursor.rowcount > 0
        finally:
            conn.close()

    def search_items(self, query: str) -> List[dict]:
        pattern = f"%{query.lower()}%"
        conn = sqlite3.connect(self.db_path)
        try:
            rows = conn.execute(
                "SELECT id, name, quantity, price FROM items WHERE lower(name) LIKE ? ORDER BY name",
                (pattern,),
            ).fetchall()
        finally:
            conn.close()

        return [
            {"id": row[0], "name": row[1], "quantity": row[2], "price": row[3]}
            for row in rows
        ]


@dataclass
class Product:
    productId: int
    productName: str
    quantity: int
    price: float


class InMemoryInventory:
    """Simple in-memory inventory using a dict (hash map) keyed by productId."""

    def __init__(self):
        self._items: Dict[int, Product] = {}

    def add_product(self, product: Product) -> None:
        if product.productId in self._items:
            raise KeyError(f"Product ID {product.productId} already exists")
        if product.quantity < 0 or product.price < 0:
            raise ValueError("Quantity and price must be non-negative")
        self._items[product.productId] = product

    def update_product(self, productId: int, *, quantity: Optional[int] = None, price: Optional[float] = None, productName: Optional[str] = None) -> None:
        if productId not in self._items:
            raise KeyError(f"Product ID {productId} not found")
        p = self._items[productId]
        if quantity is not None:
            if quantity < 0:
                raise ValueError("Quantity must be non-negative")
            p.quantity = quantity
        if price is not None:
            if price < 0:
                raise ValueError("Price must be non-negative")
            p.price = price
        if productName is not None:
            p.productName = productName

    def delete_product(self, productId: int) -> bool:
        return self._items.pop(productId, None) is not None

    def list_products(self) -> List[Product]:
        return sorted(self._items.values(), key=lambda x: x.productId)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Simple inventory management system")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new inventory item")
    add_parser.add_argument("values", nargs="*", help="Provide either [name quantity price] or [item_id name quantity price]")

    update_parser = subparsers.add_parser("update", help="Update an item")
    update_parser.add_argument("item_id", type=int)
    update_parser.add_argument("--quantity", type=int)
    update_parser.add_argument("--price", type=float)

    list_parser = subparsers.add_parser("list", help="List all items")
    list_parser.add_argument("--query", default=None)

    remove_parser = subparsers.add_parser("remove", help="Remove an item")
    remove_parser.add_argument("item_id", type=int)

    subparsers.add_parser("run-sequence", help="Run example add/update/delete sequence")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    manager = InventoryManager()

    if args.command == "add":
        values = args.values
        if len(values) == 3:
            name, quantity, price = values
            item_id = manager.add_item(name, int(quantity), float(price))
        elif len(values) == 4:
            item_id_raw, name, quantity, price = values
            item_id = manager.add_item(name, int(quantity), float(price), item_id=int(item_id_raw))
        else:
            raise SystemExit("Usage: add [item_id] name quantity price")
        print(f"Added item with id {item_id}")
    elif args.command == "update":
        manager.update_item(args.item_id, quantity=args.quantity, price=args.price)
        print(f"Updated item {args.item_id}")
    elif args.command == "list":
        items = manager.search_items(args.query) if args.query else manager.list_items()
        for item in items:
            print(f"{item['id']} {item['name']} {item['quantity']} {item['price']}")
    elif args.command == "remove":
        removed = manager.remove_item(args.item_id)
        print("Removed item" if removed else "Item not found")


if __name__ == "__main__":
    main()
