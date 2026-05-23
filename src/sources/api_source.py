import asyncio
from src.models.task import Task
from typing import AsyncIterable


class ApiMockTaskSource:
    '''Get tasks from imaginable API'''

    def __init__(self):
        pass

    async def get_tasks(self) -> AsyncIterable[Task]:
        '''Simulate API response and split it into the tasks'''
        # If it was real API and not just a mock, this response would be replaced with aiohttp session.
        # But, alas, there is just a mocked response.
        response: list[dict[str, int | str]] = [{
            "id": 1,
            "description": "some content 1",
            "priority": 1,
            "status": "pending",
            "create_time": "2023-01-01 00:00:00",
            "deadline_time": "2026-01-02 14:14:14",
        },
            {
                "id": 2,
                "description": "some content 2",
                "priority": 3,
                "status": "active",
                "create_time": "2026-03-01 10:40:00",
                "deadline_time": "2026-04-29 14:14:14"
        }]
        for i, item in enumerate(response):
            yield Task(
                input_id=int(item["id"]),
                input_description=str(item["description"]),
                input_priority=int(item["priority"]),
                input_status=str(item["status"]),
                input_create_time=str(item["create_time"]),
                input_deadline_time=str(item["deadline_time"])
            )

            if i % 1000 == 0:
                await asyncio.sleep(0)
