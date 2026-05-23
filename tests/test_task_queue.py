from src.models.task import Task
from src.services.task_queue import TaskQueue
from src.contracts.task_source import TaskSource
from src.sources.generate_source import GenerateSource
from src.sources.api_source import ApiMockTaskSource
from src.sources.file_source import FileSource

import pytest


class MockAsyncTaskSource:

    def __init__(self, tasks):
        self._tasks = tasks

    async def get_tasks(self):
        for task in self._tasks:
            yield task


class TestTaskQueueBasics:

    @pytest.mark.asyncio
    async def test_async_iteration(self):
        source = GenerateSource(3)
        queue = TaskQueue(source)

        tasks = []
        async for task in queue:
            tasks.append(task)

        assert len(tasks) == 3
        assert all(isinstance(t, Task) for t in tasks)

    @pytest.mark.asyncio
    async def test_repeatable_async_iteration(self):
        source = GenerateSource(3)
        queue = TaskQueue(source)

        first_tasks = []
        async for task in queue:
            first_tasks.append(task)

        second_tasks = []
        async for task in queue:
            second_tasks.append(task)

        assert len(first_tasks) == len(second_tasks) == 3
        assert all(f.id == s.id for f, s in zip(first_tasks, second_tasks))

    @pytest.mark.asyncio
    async def test_queue_with_api_source(self):
        source = ApiMockTaskSource()
        queue = TaskQueue(source)

        tasks = []
        async for task in queue:
            tasks.append(task)

        assert len(tasks) == 2
        assert tasks[0].id == 1

    @pytest.mark.asyncio
    async def test_queue_with_file_source(self):
        source = FileSource("friday.txt")
        queue = TaskQueue(source)

        tasks = []
        async for task in queue:
            tasks.append(task)

        assert len(tasks) == 4
        assert tasks[0].id == 1
        assert tasks[0].description == "Finish sprint presentation"

    @pytest.mark.asyncio
    async def test_lazy_evaluation_with_large_source(self):
        source = GenerateSource(10000)
        queue = TaskQueue(source)

        count = 0
        async for task in queue:
            count += 1
            if count == 5:
                break

        assert count == 5


class TestTaskQueueFiltering:

    @pytest.mark.asyncio
    async def test_filter_by_status_pending(self):
        source = GenerateSource(5)
        queue = TaskQueue(source)
        filtered = await queue.filter_by_status("pending")

        tasks = []
        async for task in filtered:
            tasks.append(task)

        assert len(tasks) == 5
        assert all(t.status == "pending" for t in tasks)

    @pytest.mark.asyncio
    async def test_filter_by_status_active(self):
        source = GenerateSource(5)
        queue = TaskQueue(source)
        filtered = await queue.filter_by_status("active")

        tasks = []
        async for task in filtered:
            tasks.append(task)

        assert len(tasks) == 0

    @pytest.mark.asyncio
    async def test_filter_by_priority_low(self):
        source = GenerateSource(5)
        queue = TaskQueue(source)
        filtered = await queue.filter_by_priority(2)

        tasks = []
        async for task in filtered:
            tasks.append(task)

        assert len(tasks) == 2
        assert all(t.priority <= 2 for t in tasks)

    @pytest.mark.asyncio
    async def test_filter_by_priority_high(self):
        source = GenerateSource(5)
        queue = TaskQueue(source)
        filtered = await queue.filter_by_priority(5)

        tasks = []
        async for task in filtered:
            tasks.append(task)

        assert len(tasks) == 5
        assert all(t.priority <= 5 for t in tasks)

    @pytest.mark.asyncio
    async def test_chained_filtering(self):
        tasks = [
            Task(input_id=1, input_description="Task 1", input_priority=1, input_status="pending",
                 input_create_time="2023-01-01 00:00:00", input_deadline_time="2026-01-02 14:14:14"),
            Task(input_id=2, input_description="Task 2", input_priority=3, input_status="active",
                 input_create_time="2023-01-01 00:00:00", input_deadline_time="2026-01-02 14:14:14"),
            Task(input_id=3, input_description="Task 3", input_priority=2, input_status="pending",
                 input_create_time="2023-01-01 00:00:00", input_deadline_time="2026-01-02 14:14:14"),
            Task(input_id=4, input_description="Task 4", input_priority=4, input_status="pending",
                 input_create_time="2023-01-01 00:00:00", input_deadline_time="2026-01-02 14:14:14"),
        ]

        source = MockAsyncTaskSource(tasks)
        queue = TaskQueue(source)

        filtered = await (await queue.filter_by_status("pending")).filter_by_priority(3)

        result = []
        async for task in filtered:
            result.append(task)

        assert len(result) == 2
        assert all(t.status == "pending" and t.priority <= 3 for t in result)

    @pytest.mark.asyncio
    async def test_filter_with_empty_result(self):
        source = GenerateSource(5)
        queue = TaskQueue(source)
        filtered = await queue.filter_by_status("nonexistent_status")

        tasks = []
        async for task in filtered:
            tasks.append(task)

        assert len(tasks) == 0

    @pytest.mark.asyncio
    async def test_filter_preserves_laziness(self):
        source = GenerateSource(1000)
        queue = TaskQueue(source)
        filtered = await queue.filter_by_priority(5)

        count = 0
        async for task in filtered:
            count += 1
            if count == 10:
                break

        assert count == 10


class TestTaskQueueWithRealSources:

    @pytest.mark.asyncio
    async def test_api_source_filtering(self):
        source = ApiMockTaskSource()
        queue = TaskQueue(source)
        filtered = await queue.filter_by_priority(2)

        tasks = []
        async for task in filtered:
            tasks.append(task)

        assert len(tasks) == 1
        assert tasks[0].id == 1

    @pytest.mark.asyncio
    async def test_file_source_filtering(self):
        source = FileSource("friday.txt")
        queue = TaskQueue(source)
        filtered = await queue.filter_by_status("finished")

        tasks = []
        async for task in filtered:
            tasks.append(task)

        assert len(tasks) == 2
        assert all(t.status == "finished" for t in tasks)

    @pytest.mark.asyncio
    async def test_large_queue_performance(self):
        source = GenerateSource(100000)
        queue = TaskQueue(source)

        count = 0
        async for task in queue:
            count += 1

        assert count == 100000


class TestTaskQueueErrorHandling:

    @pytest.mark.asyncio
    async def test_filter_by_status_logging(self):
        source = GenerateSource(3)
        queue = TaskQueue(source)

        filtered = await queue.filter_by_status("pending")
        assert filtered is not None

    @pytest.mark.asyncio
    async def test_filter_by_priority_logging(self):
        source = GenerateSource(3)
        queue = TaskQueue(source)

        filtered = await queue.filter_by_priority(5)
        assert filtered is not None

    def test_invalid_source_raises_type_error(self):
        with pytest.raises(TypeError):
            TaskQueue("not a source")
