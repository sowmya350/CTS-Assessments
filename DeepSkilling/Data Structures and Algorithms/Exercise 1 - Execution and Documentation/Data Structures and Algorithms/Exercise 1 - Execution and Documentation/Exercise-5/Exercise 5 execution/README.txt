Exercise 5: Task Management System

1. Understand Linked Lists:
- A linked list is a linear data structure where each node contains data and a reference to the next node.
- It is useful when elements need to be inserted or deleted frequently without shifting all elements.

2. Setup:
- Create a Task class to represent each task.
- Create a TaskNode class to hold a task and connect to the next node.
- Create a TaskLinkedList class to manage all tasks.

3. Implementation:
- add_task(task): adds a task to the end of the linked list.
- delete_task(task_id): removes a task by its ID.
- traverse_tasks(): visits every node and returns all tasks.
- display_tasks(): prints all tasks in the list.

4. Analysis:
- Adding a task at the end takes O(n) time because the list must be traversed to reach the last node.
- Deleting a task also takes O(n) in the worst case because the list may need to be searched.
- Traversing the entire list takes O(n) time.
- Linked lists are efficient for insertion and deletion when the position is known, but less efficient for random access than arrays.

How to run:
- Open the folder in VS Code.
- Run: python task_manager.py
