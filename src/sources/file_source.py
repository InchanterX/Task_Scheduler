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
                for i, line in enumerate(file):
                    yield Task(id=(i+1), payload=line.strip())
        except FileNotFoundError:
            return
