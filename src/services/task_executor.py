from src.contracts.task_handler import TaskHandler
from src.infrastructure.logger import logger
from src.services.task_queue import TaskQueue


class TaskExecutor:
    '''
    Async executor that pulls tasks from a TaskQueue and dispatches
    each one to a TaskHandler.
    '''

    def __init__(self, queue: TaskQueue, handler: TaskHandler) -> None:
        '''Initialize the TaskExecutor with a TaskQueue and a TaskHandler'''
        if not isinstance(handler, TaskHandler):
            raise TypeError(
                f"Handler must implement TaskHandler protocol, "
                f"got {type(handler).__name__}"
            )
        self._queue = queue
        self._handler = handler
        self._processed = 0
        self._failed = 0

    async def __aenter__(self) -> "TaskExecutor":
        '''Start the TaskExecutor and log the handler being used'''
        logger.info(
            f"TaskExecutor started with handler: "
            f"{self._handler.__class__.__name__}"
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> bool:
        '''Stop the TaskExecutor and log the final statistics'''
        logger.info(
            f"TaskExecutor finished — "
            f"processed: {self._processed}, failed: {self._failed}"
        )
        if exc_type is not None:
            logger.error(f"TaskExecutor exited with error: {exc_val}")
        return False

    async def run(self) -> None:
        '''Pull every task from the queue and pass it to the handler'''
        async for task in self._queue:
            try:
                await self._handler.handle(task)
                self._processed += 1
            except Exception as e:
                self._failed += 1
                logger.error(
                    f"Handler failed on task id={task.id}: {e}"
                )
