class TaskNotFoundException(Exception):
    def __init__(self, task_id: int):
        self.message = f"Task with ID {task_id} not found"
        super().__init__(self.message)
        
class TaskCreationFailedException(Exception):
    def __init__(self, reason: str = "Unkown reason"):
        self.message = f"Failed to create task due to: {reason}"
        super().__init__(self.message)
        
class TaskUpdateFailedException(Exception):
    def __init__(self, task_id: int, reason: str = "Unknown reason"):
        self.message = f"Failed to update task with ID {task_id} due to: {reason}"
        super().__init__(self.message)

class TaskDeletionFailedException(Exception):
    def __init__(self, task_id: int, reason: str = "Unknown reason"):
        self.message = f"Failed to delete task with ID {task_id} due to: {reason}"
        super().__init__(self.message)

class GetAllTasksException(Exception):
    def __init__(self, reason: str = "Unknown error"):
        self.message = f"Failed to retrieve tasks due to: {reason}"
        super().__init__(self.message)