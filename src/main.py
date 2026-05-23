from src.infrastructure.logger import logger
from src.infrastructure.display import display_tasks
from src.sources.file_source import FileSource
from src.sources.generate_source import GenerateSource
from src.sources.api_source import ApiMockTaskSource
from src.services.task_queue import TaskQueue


def get_queue_from_source(choice: str) -> TaskQueue | None:
    if choice == "1":
        number = input("Enter the number of tasks to generate: ")
        logger.info(f"User entered number of tasks to generate: {number}")
        if not (number.isdigit() and int(number) > 0):
            print("Invalid input! Enter a positive integer!\n")
            return None
        return TaskQueue(GenerateSource(int(number)))

    elif choice == "2":
        return TaskQueue(ApiMockTaskSource())

    elif choice == "3":
        file_name = input("Enter the file name: ")
        logger.info(f"User entered file name: {file_name}")
        return TaskQueue(FileSource(file_name))

    else:
        logger.warning(f"User entered invalid option: {choice}")
        print("Invalid input! Input an integer from 1 to 4.\n")
        return None


def apply_filters(queue: TaskQueue) -> TaskQueue:
    while True:
        print("Filters:")
        print("1. Filter by status")
        print("2. Filter by priority")
        print("3. Show current tasks (after filters)")
        print("4. Done")
        print("\n")

        choice = input("Choose: ").strip()

        if choice == "1":
            status = input(
                "Status (pending/active/finished/canceled): ").strip().lower()
            if status:
                queue = queue.filter_by_status(status)
                print(f"Filtered by status: {status}")
            else:
                print("Status cannot be empty.")

        elif choice == "2":
            priority = input("Max priority (number): ").strip()
            if priority.isdigit():
                queue = queue.filter_by_priority(int(priority))
                print(f"Filtered by priority <= {priority}")
            else:
                print("Invalid number.")

        elif choice == "3":
            tasks = list(queue)
            display_tasks(tasks)
            print(f"Total: {len(tasks)} tasks")

        elif choice == "4":
            return queue

        else:
            print("Invalid choice. Enter 1-4.")


def main():
    logger.info("Task Scheduler started.")

    while True:
        print("1. Generate Tasks")
        print("2. API Mock Tasks")
        print("3. File Tasks")
        print("4. Exit")
        print("\n")

        choice = input("Enter your choice: ").strip()
        logger.info(f"User selected option: {choice}")

        if choice == "4":
            break

        queue = get_queue_from_source(choice)
        if queue is None:
            continue

        all_tasks = list(queue)
        print(f"\nLoaded {len(all_tasks)} tasks:")
        display_tasks(all_tasks)

        if input("\nApply filters? (y/n): ").strip().lower() == 'y':
            filtered_queue = apply_filters(queue)
            final_tasks = list(filtered_queue)
            print("\nFILTERED TASKS:\n")
            display_tasks(final_tasks)

        input("\nPress Enter to continue...\n")

    logger.info("Task Scheduler stopped.")


if __name__ == "__main__":
    main()
