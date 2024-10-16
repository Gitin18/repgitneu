

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        return f"Task: {self.description}, Deadline: {self.deadline}, Completed: {'Yes' if self.completed else 'No'}"


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

##



    def show_pending_tasks(self):
        print("Pending tasks:")
        for task in self.tasks:
            if not task.completed:
                print(task)


# Example usage
task_manager = TaskManager()

# Adding tasks
task_manager.add_task("Finish project report", "2024-10-20")
task_manager.add_task("Buy groceries", "2024-10-14")
task_manager.add_task("Book flight tickets", "2024-10-")


task_manager.mark_task_completed("Buy groceries")


task_manager.show_pending_tasks()
