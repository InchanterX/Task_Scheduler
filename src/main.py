from src.infrastructure.logger import logger
from src.infrastructure.display import display_tasks
from src.services.task_receiver import TaskReceiver
from src.sources.file_source import FileSource
from src.sources.generate_source import GenerateSource
from src.sources.api_source import ApiMockTaskSource


def main():
    '''Main entry point for the task scheduler'''
    logger.info("Task Scheduler started.")
    while (1):
        print("1. Generate Task")
        print("2. API Task")
        print("3. File Task")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()
        logger.info(f"User selected option: {choice}")
        match choice:
            case "1":
                number = input("Enter the number of tasks to generate: ")
                logger.info(
                    f"User entered number of tasks to generate: {number}")
                if not (number.isdigit() and int(number) > 0):
                    print("Invalid input! Enter a positive integer!\n")
                    continue
                generate_option = GenerateSource(int(number))
                receiver1 = list(TaskReceiver(generate_option).receive_tasks())
                display_tasks(receiver1)
            case "2":
                api_option = ApiMockTaskSource()
                receiver2 = list(TaskReceiver(api_option).receive_tasks())
                display_tasks(receiver2)
            case "3":
                file_name = input("Enter the file name: ")
                logger.info(f"User entered file name: {file_name}")
                file_option = FileSource(file_name)
                receiver3 = list(TaskReceiver(file_option).receive_tasks())
                display_tasks(receiver3)
            case "4":
                break
            case _:
                logger.warning(f"User entered invalid option: {choice}")
                print("Invalid input! Input an integer from 1 to 4.\n")
    logger.info("Task Scheduler stopped.")


if __name__ == "__main__":
    main()
