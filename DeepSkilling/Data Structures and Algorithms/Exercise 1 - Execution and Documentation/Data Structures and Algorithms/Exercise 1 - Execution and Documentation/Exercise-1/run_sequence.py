from inventory_management import InventoryManager


def fmt_price(p):
    try:
        if float(p).is_integer():
            return str(int(p))
    except Exception:
        pass
    return str(p)


def display(manager):
    items = manager.list_items()
    for it in items:
        print(f"{it['id']} {it['name']} {it['quantity']} {fmt_price(it['price'])}")


def main():
    db = "sequence.db"
    manager = InventoryManager(db)

    # Add Product:
    manager.add_item("Laptop", 10, 50000.0, item_id=101)
    manager.add_item("Mouse", 50, 500.0, item_id=102)
    manager.add_item("Keyboard", 20, 1500.0, item_id=103)

    # Display Products:
    display(manager)
    print()

    # Update Product 101 quantity to 15
    manager.update_item(101, quantity=15)

    # Display Products:
    display(manager)
    print()

    # Delete Product 102
    manager.remove_item(102)

    # Final Inventory:
    display(manager)

    manager.close()


if __name__ == '__main__':
    main()
