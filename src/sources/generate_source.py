from src.models.task import Task
from typing import Iterable


class GenerateSource:
    '''Generates source data for tasks'''

    def __init__(self, count: int):
        self._count = count

    def get_tasks(self) -> Iterable[Task]:
        '''Generate task data with generator'''
        for n in range(1, self._count + 1):
            yield Task(
                input_id=n,
                input_description=f"Task number {n}",
                input_priority=n % 5 + 1,
                input_status="pending",
                input_create_time="2023-01-01 00:00:00",
                input_deadline_time="2026-01-02 14:14:14"
            )
