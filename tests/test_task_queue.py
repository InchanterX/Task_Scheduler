from src.models.task import Task
from src.services.task_queue import TaskQueue
from src.contracts.task_source import TaskSource
from src.sources.generate_source import GenerateSource
from src.sources.api_source import ApiMockTaskSource
from src.sources.file_source import FileSource


import pytest

from src.services.task_queue import TaskQueue
from src.sources.generate_source import GenerateSource
from src.sources.api_source import ApiMockTaskSource
from src.sources.file_source import FileSource


def extract_ids(tasks):
    return [t.id for t in tasks]


class MockFileSource:
    def __init__(self):
        self._tasks = [
            Task(
                input_id=1,
                input_description="Finish sprint presentation",
                input_priority=100,
                input_status="finished",
                input_create_time="2026-03-26 23:00:00",
                input_deadline_time="2026-03-27 09:00:00"
            ),
            Task(
                input_id=2,
                input_description="Presentation protection",
                input_priority=1000,
                input_status="finished",
                input_create_time="2026-03-06 23:00:00",
                input_deadline_time="2026-03-27 09:15:00"
            ),
            Task(
                input_id=3,
                input_description="Python laboratory work",
                input_priority=10,
                input_status="active",
                input_create_time="2026-03-14 12:00:00",
                input_deadline_time="2026-03-28 23:59:59"
            ),
            Task(
                input_id=4,
                input_description="Prepare to Python context",
                input_priority=90,
                input_status="active",
                input_create_time="2026-03-21 12:00:00",
                input_deadline_time="2026-03-28 13:00:00"
            ),
        ]

    def get_tasks(self):
        yield from self._tasks


@pytest.fixture(params=[
    GenerateSource(10),
    ApiMockTaskSource(),
    MockFileSource(),
])
def queue(request):
    return TaskQueue(request.param)


def test_iteration(queue):
    tasks = list(queue)
    assert isinstance(tasks, list)
    assert len(tasks) > 0


def test_repeatable_iteration(queue):
    first = list(queue)
    second = list(queue)

    assert first == second


def test_iter_and_next():
    source = MockFileSource()
    queue = TaskQueue(source)
    it = iter(queue)

    first = next(it)
    assert first is not None

    second = next(it)
    assert second is not None
    assert second is not first

    third = next(it)
    assert third is not None
    fourth = next(it)
    assert fourth is not None

    with pytest.raises(StopIteration):
        next(it)


@pytest.mark.parametrize("status", ["pending", "active", "completed", "expired"])
def test_filter_by_status(queue, status):
    filtered = queue.filter_by_status(status)

    for task in filtered:
        assert task.status == status


@pytest.mark.parametrize("priority_limit", [1, 2, 3, 4, 5])
def test_filter_by_priority(queue, priority_limit):
    filtered = queue.filter_by_priority(priority_limit)

    for task in filtered:
        assert task.priority <= priority_limit


def test_filter_chain(queue):
    filtered = (
        queue
        .filter_by_priority(5)
        .filter_by_status("pending")
    )

    for task in filtered:
        assert task.priority <= 5
        assert task.status == "pending"


def test_empty_filter_result(queue):
    filtered = queue.filter_by_status("NON-EXISTENT_STATUS")

    assert list(filtered) == []


def test_next_on_empty_filtered(queue):
    filtered = queue.filter_by_status("NON-EXISTENT_STATUS")
    it = iter(filtered)

    assert next(it, None) is None


def test_large_source_behavior():
    queue = TaskQueue(GenerateSource(100000))

    count = sum(1 for _ in queue)
    assert count == 100000


def test_file_source():
    queue = TaskQueue(FileSource("friday.txt"))

    tasks = list(queue)

    assert len(tasks) > 0
    assert all(hasattr(t, "id") for t in tasks)
