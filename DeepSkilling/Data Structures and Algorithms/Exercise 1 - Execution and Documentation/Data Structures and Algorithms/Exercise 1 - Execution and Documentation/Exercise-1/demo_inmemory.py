from inventory_management import Product, InMemoryInventory


def fmt_price(p):
    try:
        if float(p).is_integer():
            return str(int(p))
    except Exception:
        pass
    return str(p)


def display(inv: InMemoryInventory):
    for p in inv.list_products():
        print(f"{p.productId} {p.productName} {p.quantity} {fmt_price(p.price)}")


def main():
    inv = InMemoryInventory()

    # Add Product:
    inv.add_product(Product(101, "Laptop", 10, 50000.0))
    inv.add_product(Product(102, "Mouse", 50, 500.0))
    inv.add_product(Product(103, "Keyboard", 20, 1500.0))

    # Display Products:
    display(inv)
    print()

    # Update Product 101 quantity to 15
    inv.update_product(101, quantity=15)

    # Display Products:
    display(inv)
    print()

    # Delete Product 102
    inv.delete_product(102)

    # Final Inventory:
    display(inv)


if __name__ == '__main__':
    main()
