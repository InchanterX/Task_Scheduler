from os import path
from src.models.task import Task
from typing import AsyncIterable
from src.sources.async_file_reader import AsyncFileReader


class FileSource:
    '''Receive tasks from a file line by line'''

    def __init__(self, file_name: str, dir_name: str = "tasks_source"):
        self._file_path = path.abspath(path.join(dir_name, file_name))

    async def get_tasks(self) -> AsyncIterable[Task]:
        '''Open file and yield tasks'''
        try:
            async with AsyncFileReader(self._file_path) as reader:
                async for line in reader:
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
