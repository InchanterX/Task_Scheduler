from src.infrastructure.logger import logger
from src.contracts.task_source import TaskSource
from src.models.task import Task
from typing import Iterable


class TaskReceiver:
    '''Receive which way will be used to get tasks via duck typing'''

    def __init__(self, source: TaskSource):
        self.task_source = source

    def __iter__(self):
        return self.receive_tasks()

    def receive_tasks(self) -> Iterable[Task]:
        '''Check if given option have a get_tasks() function to receive tasks from the source'''
        if isinstance(self.task_source, TaskSource):
            logger.info(
                f"Receiving tasks from {self.task_source.__class__.__name__}")
            for task in self.task_source.get_tasks():
                logger.debug(f"Received task: {task}")
                yield task

            return

        logger.error(
            f"Given source {self.task_source.__class__.__name__} doesn't have get_tasks() function!")
        raise TypeError("This source doesn't have get_tasks() function!")
