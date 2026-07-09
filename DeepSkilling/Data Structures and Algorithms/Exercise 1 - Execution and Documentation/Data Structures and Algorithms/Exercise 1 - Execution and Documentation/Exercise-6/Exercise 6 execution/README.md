# Exercise 6: Library Management System

## 1. Understand Search Algorithms
- Linear search checks each book one by one and is simple to implement.
- Binary search is faster, but the books must be sorted first.

## 2. Setup
- Run the program with:
  - `python library_management.py`
- Run the tests with:
  - `python -m unittest -v`

## 3. Implementation
- The program stores books in a `LibraryManagementSystem`.
- It supports searching by title and author using linear search.
- It also demonstrates binary search for exact title and author matches.

## 4. Analysis
- Linear search: $O(n)$ time in the worst case.
- Binary search: $O(log n)$ time after sorting.
- Binary search is more efficient for large datasets, while linear search is easier for small or unsorted data.
