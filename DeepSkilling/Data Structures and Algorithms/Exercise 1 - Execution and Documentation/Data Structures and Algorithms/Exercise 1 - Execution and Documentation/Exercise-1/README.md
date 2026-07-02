# Exercise 1: Inventory Management System

## 1. Understand the Problem
This project models a warehouse inventory system where items can be stored, updated, searched, and removed efficiently. The main goal is to support reliable data storage and quick retrieval using a lightweight database.

## 2. Setup
Run the following commands from the project folder:

```bash
python -m unittest discover -s tests -v
```

You can also run the CLI directly:

```bash
python inventory_management.py add "Laptop" 10 999.99
python inventory_management.py list
```

## 3. Implementation
The solution uses Python with SQLite for persistent storage.

### Features
- Add new inventory items
- Update stock quantity and price
- List all items
- Search items by name
- Remove items

### Design choice
SQLite was selected because it provides structured storage without needing a separate server, which keeps the system simple and reliable for an exercise-sized application.

## 4. Analysis
- Data is stored in a table with a primary key and indexed lookups for efficient retrieval.
- The implementation supports $O(1)$ average lookup for direct item access and fast list/search operations for a small-to-medium inventory.
- The design is easy to extend with features such as categories, supplier details, or low-stock alerts.
