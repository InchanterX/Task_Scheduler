from typing import AsyncIterable, Callable, Union
from src.infrastructure.logger import logger
from src.models.task import Task
from src.contracts.task_source import TaskSource


class TaskQueue:
    '''
    Lazy async iterable over tasks from a given source.
    Supports repeated iteration - each async for creates a new pass over the source.
    Filtering returns a new TaskQueue, preserving laziness and composability.
    '''

    def __init__(
        self,
        source: Union[TaskSource, Callable[[], AsyncIterable[Task]]]
    ):
        '''Initialize the TaskQueue with a task source'''
        if isinstance(source, TaskSource):
            self._factory = source.get_tasks
        elif callable(source):
            self._factory = source
        else:
            raise TypeError(
                "Source must be TaskSource or callable returning AsyncIterable[Task]"
            )

    def __aiter__(self):
        return self._iterate()

    async def _iterate(self):
        '''Delegate iteration to the factory's async generator'''
        async for task in self._factory():
            yield task

    async def filter_by_status(self, status: str) -> "TaskQueue":
        '''Filter tasks by status. Returns a new TaskQueue'''
        async def factory() -> AsyncIterable[Task]:
            async for task in self:
                if task.status == status:
                    yield task

        logger.info(f"Creating a filtered TaskQueue by status: {status}")
        return TaskQueue(factory)

    async def filter_by_priority(self, priority: int) -> "TaskQueue":
        '''Filter tasks by priority (<=). Returns a new TaskQueue'''
        async def factory() -> AsyncIterable[Task]:
            async for task in self:
                if task.priority <= priority:
                    yield task

        logger.info(f"Creating a filtered TaskQueue by priority: {priority}")
        return TaskQueue(factory)
