from typing import Protocol, runtime_checkable
from src.models.task import Task


@runtime_checkable
class TaskHandler(Protocol):
    '''Contract for task handlers'''

    async def handle(self, task: Task) -> None:
        '''Process a single task'''
        ...
