from os import path
from src.models.task import Task
from typing import Iterable


class FileSource:
    '''Receive tasks from a file line by line'''

    def __init__(self, file_name: str):
        self._file_path = path.abspath(path.join("tasks_source", file_name))

    def get_tasks(self) -> Iterable[Task]:
        '''Open file and yield tasks'''
        try:
            with open(self._file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    splitted_line = line.strip().split(" ")
                    yield Task(
                        input_id=int(splitted_line[0]),
                        input_description=(" ".join(splitted_line[1:(
                            len(splitted_line) - 6)])),
                        input_priority=int(splitted_line[-6]),
                        input_status=splitted_line[-5],
                        input_create_time=(
                            splitted_line[-4] + " " + splitted_line[-3]),
                        input_deadline_time=(
                            splitted_line[-2] + " " + splitted_line[-1]),
                    )
        except FileNotFoundError:
            return
