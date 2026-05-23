from src.infrastructure.display import display_tasks
from src.models.task import Task
from src.services.task_queue import TaskQueue
from src.sources.generate_source import GenerateSource
import pytest


@pytest.mark.asyncio
async def test_display_tasks_with_tasks(capsys):
    queue = TaskQueue(GenerateSource(2))
    await display_tasks(queue)

    captured = capsys.readouterr()
    assert "Task ID:" in captured.out
    assert "Description:" in captured.out
    assert "Priority:" in captured.out


@pytest.mark.asyncio
async def test_display_empty_tasks(capsys):
    async def empty_source():
        return
        yield

    queue = TaskQueue(empty_source)
    await display_tasks(queue)

    captured = capsys.readouterr()
    assert "No tasks found" in captured.out


@pytest.mark.asyncio
async def test_display_tasks_formatting(capsys):
    queue = TaskQueue(GenerateSource(1))
    await display_tasks(queue)

    captured = capsys.readouterr()
    assert "====================" in captured.out
    assert "Task ID:" in captured.out
    assert "Description:" in captured.out
    assert "Priority:" in captured.out
    assert "Status:" in captured.out
    assert "Create Time:" in captured.out
    assert "Deadline Time:" in captured.out
    assert "Duration:" in captured.out


@pytest.mark.asyncio
async def test_display_tasks_shows_count(capsys):
    queue = TaskQueue(GenerateSource(3))
    await display_tasks(queue)

    captured = capsys.readouterr()
    assert "3" in captured.out
