from typing import Iterable, Iterator, Callable, Union
from src.infrastructure.logger import logger
from src.models.task import Task
from src.contracts.task_source import TaskSource
from src.sources.generate_source import GenerateSource


class TaskQueue:
    '''
    Provide a lazy iterator over tasks and ability to sort through them with some parameters.
    '''

    def __init__(self, source: Union[TaskSource, Callable[[], Iterable[Task]]]):
        if isinstance(source, TaskSource):
            self._factory = source.get_tasks
        elif callable(source):
            self._factory = source
        else:
            raise TypeError(
                "Source must be TaskSource or callable returning Iterable[Task]")

    def __iter__(self):
        '''Return an iterator over the tasks.'''
        return iter(self._factory())

    def filter_by_status(self, status: str) -> "TaskQueue":
        '''Filter tasks by their status. Return a new TaskQueue with the filtered tasks iterator.'''
        def factory():
            for task in self:
                if task.status == status:
                    yield task
        logger.info(
            f"Creating a filtered TaskQueue by status: {status} TaskQueue")
        return TaskQueue(factory)

    def filter_by_priority(self, priority: int) -> "TaskQueue":
        '''Filter tasks by their priority. Return a new TaskQueue with the filtered tasks iterator.'''
        def factory():
            for task in self:
                if task.priority <= priority:
                    yield task
        logger.info(
            f"Creating a filtered TaskQueue by priority: {priority} TaskQueue")
        return TaskQueue(factory)
