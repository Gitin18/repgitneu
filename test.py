from datetime import datetime

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = datetime.strptime(deadline, '%Y-%m-%d')
        self.completed = False
        self.failed = False

    def mark_completed(self):
        self.completed = True

    def mark_failed(self):
        self.failed = True

    def __str__(self):
        status = "Completed" if self.completed else "Failed" if self.failed else "Pending"
        return f"Task: {self.description}, Deadline: {self.deadline.date()}, Status: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    def mark_task_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_completed()
                print(f"Task '{description}' marked as completed.")
                return
        print(f"Task '{description}' not found.")

    def mark_task_failed(self):
        current_date = datetime.now().date()
        for task in self.tasks:
            if task.deadline.date() < current_date and not task.completed:
                task.mark_failed()
                print(f"Task '{task.description}' is marked as failed.")

    def show_pending_tasks(self):
        print("Pending tasks:")
        for task in self.tasks:
            if not task.completed and not task.failed:
                print(task)


# Example usage
task_manager = TaskManager()

# Adding tasks
task_manager.add_task("Finish project report", "2024-10-20")
task_manager.add_task("Buy groceries", "2024-10-14")
task_manager.add_task("Book flight tickets", "2024-10-22")

# Marking a task as completed
task_manager.mark_task_completed("Buy groceries")

# Mark overdue tasks as failed
task_manager.mark_task_failed()

# Showing pending tasks
task_manager.show_pending_tasks()

