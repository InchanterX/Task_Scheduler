from src.models.task import Task
from typing import Iterable


class GenerateSource:
    '''Generates source data for tasks'''

    def __init__(self, count: int):
        self._count = count

    def get_tasks(self) -> Iterable[Task]:
        '''Generate task data with generator'''
        for n in range(1, self._count + 1):
            yield Task(id=n, payload=f"Task number {n}")
