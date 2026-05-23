from src.contracts.task_handler import TaskHandler
from src.infrastructure.logger import logger
from src.models.task import Task


class LoggingHandler:
    '''Logs each task that passes through'''

    async def handle(self, task: Task) -> None:
        logger.info(
            f"Processing task id={task.id} "
            f"priority={task.priority} "
            f"status={task.status}"
        )


class PrintHandler:
    '''Prints each task to stdout'''

    async def handle(self, task: Task) -> None:
        print(
            f"[Handler] Task ID: {task.id} | "
            f"Description: {task.description} | "
            f"Priority: {task.priority} | "
            f"Status: {task.status}"
        )


class StatusFilterHandler:
    '''Passes task to inner handler only if status matches'''

    def __init__(self, target_status: str, inner: TaskHandler) -> None:
        self._status = target_status
        self._inner = inner

    async def handle(self, task: Task) -> None:
        if task.status == self._status:
            await self._inner.handle(task)
