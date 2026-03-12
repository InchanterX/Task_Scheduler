from typing import Protocol
from typing import Iterable, runtime_checkable
from src.models.task import Task


@runtime_checkable
class TaskSource(Protocol):
    '''Contract for the function that return tasks'''

    def get_tasks(self) -> Iterable[Task]:
        ...
