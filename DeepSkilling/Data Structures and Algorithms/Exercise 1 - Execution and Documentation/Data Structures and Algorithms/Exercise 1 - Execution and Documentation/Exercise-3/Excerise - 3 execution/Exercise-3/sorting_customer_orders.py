def sort_orders_by_total_price(orders):
    """Return orders sorted by total price from highest to lowest."""
    return sorted(orders, key=lambda order: order["total_price"], reverse=True)


if __name__ == "__main__":
    sample_orders = [
        {"order_id": 101, "customer": "Alice", "total_price": 42.50},
        {"order_id": 102, "customer": "Bob", "total_price": 120.00},
        {"order_id": 103, "customer": "Charlie", "total_price": 79.99},
        {"order_id": 104, "customer": "Diana", "total_price": 15.75},
    ]

    sorted_orders = sort_orders_by_total_price(sample_orders)
    for order in sorted_orders:
        print(f"{order['order_id']}: {order['customer']} - ${order['total_price']:.2f}")
