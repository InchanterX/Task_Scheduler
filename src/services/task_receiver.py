from src.infrastructure.logger import logger
from src.contracts.task_source import TaskSource


class TaskReceiver:
    '''Receive which way will be used to get tasks via duck typing'''

    def __init__(self, source: TaskSource):
        self.task_source = source

    def receive_tasks(self):
        '''Check if given option have a get_tasks() function to receive tasks from the source'''
        if isinstance(self.task_source, TaskSource):
            logger.info(
                f"Receiving tasks from {self.task_source.__class__.__name__}")
            logger.debug(
                f"Received tasks: {list(self.task_source.get_tasks())}")
            return list(self.task_source.get_tasks())

        logger.error(
            f"Given source {self.task_source.__class__.__name__} doesn't have get_tasks() function!")
        raise TypeError("This source doesn't have get_tasks() function!")

    def display_tasks(self):
        '''Formalize received tasks'''
        tasks = self.receive_tasks()
        if not tasks:
            print("====================")
            logger.info("No tasks found in the source.")
            print("No tasks found.")
            print("====================\n")

        else:
            print("====================")
            for task in tasks:
                print(
                    f"Task ID: {task.id}, "
                    f"Description: {task.description}, "
                    f"Priority: {task.priority}, "
                    f"Status: {task.status}, "
                    f"Create Time: {task.create_time}, "
                    f"Deadline Time: {task.deadline_time}, "
                    f"Duration: {task.duration}"
                )
            logger.info("Displayed all received tasks.")
            logger.debug(f"Displayed tasks: {tasks}")
            print("====================\n")
