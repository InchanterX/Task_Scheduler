from src.models.task import Task
from typing import Iterable


class ApiSources:
    '''Get tasks from imaginable API а'''

    def __init__(self):
        pass

    def get_tasks(self) -> Iterable[Task]:
        '''Simulate API response and split it into the tasks'''
        response: list[dict[str, int | str]] = [{"id": 1, "payload": "some content 1"},
                                                {"id": 2, "payload": "some content 2"}]
        for item in response:
            yield Task(id=int(item["id"]), payload=item["payload"])
