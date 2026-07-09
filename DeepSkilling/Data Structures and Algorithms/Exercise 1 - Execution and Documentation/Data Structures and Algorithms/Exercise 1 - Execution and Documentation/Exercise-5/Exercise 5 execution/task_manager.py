from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    task_id: int
    title: str
    description: str
    completed: bool = False


class TaskNode:
    def __init__(self, task: Task, next_node: Optional["TaskNode"] = None):
        self.task = task
        self.next = next_node


class TaskLinkedList:
    def __init__(self):
        self.head: Optional[TaskNode] = None
        self.size = 0

    def add_task(self, task: Task) -> None:
        new_node = TaskNode(task)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.size += 1

    def delete_task(self, task_id: int) -> bool:
        if self.head is None:
            return False

        if self.head.task.task_id == task_id:
            self.head = self.head.next
            self.size -= 1
            return True

        current = self.head
        while current.next is not None:
            if current.next.task.task_id == task_id:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        return False

    def traverse_tasks(self) -> list[Task]:
        tasks = []
        current = self.head
        while current is not None:
            tasks.append(current.task)
            current = current.next
        return tasks

    def display_tasks(self) -> None:
        if self.head is None:
            print("No tasks available.")
            return

        current = self.head
        while current is not None:
            task = current.task
            status = "Done" if task.completed else "Pending"
            print(f"[{task.task_id}] {task.title} - {status} - {task.description}")
            current = current.next


def main() -> None:
    task_list = TaskLinkedList()

    # Demo data
    task_list.add_task(Task(1, "Research linked lists", "Understand the concept and use cases"))
    task_list.add_task(Task(2, "Write code", "Implement the task manager program"))
    task_list.add_task(Task(3, "Test the system", "Verify add/delete/traverse operations"))

    print("Initial task list:")
    task_list.display_tasks()

    print("\nDeleting task 2...")
    task_list.delete_task(2)

    print("\nUpdated task list:")
    task_list.display_tasks()


if __name__ == "__main__":
    main()
