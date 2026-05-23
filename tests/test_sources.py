from src.models.task import Task
from src.sources.api_source import ApiMockTaskSource
from src.sources.file_source import FileSource
from src.sources.generate_source import GenerateSource
import pytest


class TestGenerateSource:

    @pytest.mark.asyncio
    async def test_generate_source_single_task(self):
        source = GenerateSource(1)
        tasks = []
        async for task in source.get_tasks():
            tasks.append(task)

        assert len(tasks) == 1
        assert tasks[0].id == 1
        assert tasks[0].description == "Task number 1"
        assert tasks[0].priority == 2
        assert tasks[0].status == "pending"

    @pytest.mark.asyncio
    async def test_generate_source_multiple_tasks(self):
        source = GenerateSource(5)
        tasks = []
        async for task in source.get_tasks():
            tasks.append(task)

        assert len(tasks) == 5
        assert tasks[0].id == 1
        assert tasks[4].id == 5
        assert all(t.status == "pending" for t in tasks)
        assert all(
            t.create_time.strftime(
                "%Y-%m-%d %H:%M:%S") == "2023-01-01 00:00:00"
            for t in tasks
        )

    @pytest.mark.asyncio
    async def test_generate_source_lazy_evaluation(self):
        source = GenerateSource(1000)

        gen = source.get_tasks()
        first_task = await gen.__anext__()

        assert first_task.id == 1

        second_task = await gen.__anext__()
        assert second_task.id == 2

    @pytest.mark.asyncio
    async def test_generate_source_priorities(self):
        source = GenerateSource(5)
        tasks = []
        async for task in source.get_tasks():
            tasks.append(task)

        expected_priorities = [2, 3, 4, 5, 1]
        actual_priorities = [t.priority for t in tasks]
        assert actual_priorities == expected_priorities


class TestApiMockTaskSource:

    @pytest.mark.asyncio
    async def test_api_source_returns_tasks(self):
        source = ApiMockTaskSource()
        tasks = []
        async for task in source.get_tasks():
            tasks.append(task)

        assert len(tasks) == 2
        assert tasks[0].id == 1
        assert tasks[0].description == "some content 1"
        assert tasks[0].priority == 1
        assert tasks[1].id == 2
        assert tasks[1].description == "some content 2"
        assert tasks[1].priority == 3

    @pytest.mark.asyncio
    async def test_api_source_is_async_iterable(self):
        source = ApiMockTaskSource()

        first_iteration = []
        async for task in source.get_tasks():
            first_iteration.append(task)

        second_iteration = []
        async for task in source.get_tasks():
            second_iteration.append(task)

        assert len(first_iteration) == len(second_iteration) == 2
        assert first_iteration[0].id == second_iteration[0].id

    @pytest.mark.asyncio
    async def test_api_source_tasks_have_correct_fields(self):
        source = ApiMockTaskSource()
        async for task in source.get_tasks():
            assert hasattr(task, 'id')
            assert hasattr(task, 'description')
            assert hasattr(task, 'priority')
            assert hasattr(task, 'status')
            assert hasattr(task, 'create_time')
            assert hasattr(task, 'deadline_time')
            break


class TestFileSource:

    @pytest.mark.asyncio
    async def test_file_source_friday_tasks(self):
        source = FileSource("friday.txt")
        tasks = []
        async for task in source.get_tasks():
            tasks.append(task)

        assert len(tasks) == 4
        assert tasks[0].id == 1
        assert tasks[0].description == "Finish sprint presentation"
        assert tasks[0].priority == 100
        assert tasks[0].status == "finished"
        assert tasks[3].id == 4
        assert tasks[3].description == "Prepare to Python context"

    @pytest.mark.asyncio
    async def test_file_source_saturday_tasks(self):
        source = FileSource("saturday.txt")
        tasks = []
        async for task in source.get_tasks():
            tasks.append(task)

        assert len(tasks) > 0
        assert all(hasattr(t, 'id') for t in tasks)
        assert all(hasattr(t, 'description') for t in tasks)

    @pytest.mark.asyncio
    async def test_file_source_nonexistent_file(self):
        source = FileSource("nonexistent_file.txt")
        tasks = []
        async for task in source.get_tasks():
            tasks.append(task)

        assert len(tasks) == 0

    @pytest.mark.asyncio
    async def test_file_source_lazy_evaluation(self):
        source = FileSource("friday.txt")
        gen = source.get_tasks()

        first_task = await gen.__anext__()
        assert first_task.id == 1

        second_task = await gen.__anext__()
        assert second_task.id == 2

    @pytest.mark.asyncio
    async def test_file_source_preserves_field_parsing(self):
        source = FileSource("friday.txt")
        tasks = []
        async for task in source.get_tasks():
            tasks.append(task)

        task = tasks[0]
        assert task.id == 1
        assert task.description == "Finish sprint presentation"
        assert task.priority == 100
        assert task.status == "finished"
        assert task.create_time.strftime(
            "%Y-%m-%d %H:%M:%S") == "2026-03-26 23:00:00"
        assert task.deadline_time.strftime(
            "%Y-%m-%d %H:%M:%S") == "2026-03-27 09:00:00"
