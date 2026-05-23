from src.models.task import Task
from src.infrastructure.logger import logger


async def display_tasks(tasks: list[Task]) -> None:
    '''Formalize received tasks'''
    has_tasks = False
    print("====================")
    async for task in tasks:
        has_tasks = True
        print(
            f"Task ID: {task.id}, "
            f"Description: {task.description}, "
            f"Priority: {task.priority}, "
            f"Status: {task.status}, "
            f"Create Time: {task.create_time}, "
            f"Deadline Time: {task.deadline_time}, "
            f"Duration: {task.duration}"
        )

    if not has_tasks:
        logger.info("No tasks found in the source.")
        print("No tasks found.")
    else:
        logger.info("Displayed all received tasks.")

    print("====================\n")
