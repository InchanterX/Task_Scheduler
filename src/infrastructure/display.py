from src.models.task import Task
from src.infrastructure.logger import logger


def display_tasks(tasks: list[Task]) -> None:
    '''Formalize received tasks'''
    if not tasks:
        print("====================")
        logger.info("No tasks found in the source.")
        print("No tasks found.")
        print("====================\n")

    else:
        print("====================")
        for task in tasks:
            print(
                f"Task ID: {task.id}, "
                f"Description: {task.description}, "
                f"Priority: {task.priority}, "
                f"Status: {task.status}, "
                f"Create Time: {task.create_time}, "
                f"Deadline Time: {task.deadline_time}, "
                f"Duration: {task.duration}"
            )
        logger.info("Displayed all received tasks.")
        logger.debug(f"Displayed tasks: {tasks}")
        print("====================\n")
