from src.services.task_receiver import TaskReceiver
from src.sources.file_source import FileSource
from src.sources.generate_source import GenerateSource
from src.sources.api_source import ApiSources


def main():
    '''Main entry point for the task scheduler'''
    while (1):
        print("1. Generate Task")
        print("2. API Task")
        print("3. File Task")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()
        match choice:
            case "1":
                number = input("Enter the number of tasks to generate: ")
                if not (number.isdigit() and int(number) > 0):
                    print("Invalid input! Enter a positive integer!")
                    continue
                generate_option = GenerateSource(int(number))
                receiver1 = TaskReceiver(generate_option)
                receiver1.display_tasks()
            case "2":
                api_option = ApiSources()
                receiver2 = TaskReceiver(api_option)
                receiver2.display_tasks()
            case "3":
                file_name = input("Enter the file name: ")
                file_option = FileSource(file_name)
                receiver3 = TaskReceiver(file_option)
                if not file_option.get_tasks():
                    print("No tasks found in the file.")
                    continue
                receiver3.display_tasks()
            case "4":
                break
            case _:
                print("Invalid input! Input an integer from 1 to 4.")


if __name__ == "__main__":
    main()
