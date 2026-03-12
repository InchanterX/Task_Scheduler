from src.contracts.task_source import TaskSource


class TaskReceiver:
    '''Receive which way will be used to get tasks via duck typing'''

    def __init__(self, source: TaskSource):
        self.task_source = source

    def receive_task(self):
        '''Check if given option have a get_tasks() function to receive tasks from the source'''
        if isinstance(self.task_source, TaskSource):
            return list(self.task_source.get_tasks())
        raise TypeError("This source doesn't have get_tasks() function!")

    def display_tasks(self):
        '''Formalize received tasks'''
        tasks = self.receive_task()
        if not tasks:
            print("====================")
            print("No tasks found.")
            print("====================\n")
        else:
            print("====================")
            for task in tasks:
                print(f"Task ID: {task.id}, Payload: {task.payload}")
            print("====================\n")
