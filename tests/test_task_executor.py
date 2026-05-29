from src.models.task import Task
from src.services.task_queue import TaskQueue
from src.sources.generate_source import GenerateSource
from src.sources.api_source import ApiMockTaskSource
from src.services.task_executor import TaskExecutor
from src.handlers.handlers import LoggingHandler, PrintHandler, StatusFilterHandler
from src.contracts.task_handler import TaskHandler
import pytest


class CapturingHandler:

    def __init__(self):
        self.handled: list[Task] = []

    async def handle(self, task: Task) -> None:
        self.handled.append(task)


class FailingHandler:

    async def handle(self, task: Task) -> None:
        raise RuntimeError(f"Intentional failure on task {task.id}")


class TestTaskExecutorBasics:

    @pytest.mark.asyncio
    async def test_executor_processes_all_tasks(self):
        handler = CapturingHandler()
        queue = TaskQueue(GenerateSource(5))

        async with TaskExecutor(queue, handler) as executor:
            await executor.run()

        assert len(handler.handled) == 5
        assert all(isinstance(t, Task) for t in handler.handled)

    @pytest.mark.asyncio
    async def test_executor_counts_processed(self):
        handler = CapturingHandler()
        queue = TaskQueue(GenerateSource(3))

        async with TaskExecutor(queue, handler) as executor:
            await executor.run()
            assert executor._processed == 3
            assert executor._failed == 0

    @pytest.mark.asyncio
    async def test_executor_counts_failures(self):
        handler = FailingHandler()
        queue = TaskQueue(GenerateSource(3))

        async with TaskExecutor(queue, handler) as executor:
            await executor.run()
            assert executor._failed == 3
            assert executor._processed == 0

    @pytest.mark.asyncio
    async def test_executor_continues_after_failure(self):
        fail_ids = {2}

        class PartialFailHandler:
            def __init__(self):
                self.handled = []

            async def handle(self, task: Task) -> None:
                if task.id in fail_ids:
                    raise RuntimeError("fail")
                self.handled.append(task)

        handler = PartialFailHandler()
        queue = TaskQueue(GenerateSource(3))

        async with TaskExecutor(queue, handler) as executor:
            await executor.run()

        assert len(handler.handled) == 2
        assert all(t.id not in fail_ids for t in handler.handled)

    @pytest.mark.asyncio
    async def test_executor_with_api_source(self):
        handler = CapturingHandler()
        queue = TaskQueue(ApiMockTaskSource())

        async with TaskExecutor(queue, handler) as executor:
            await executor.run()

        assert len(handler.handled) == 2

    def test_executor_rejects_invalid_handler(self):
        queue = TaskQueue(GenerateSource(1))

        with pytest.raises(TypeError):
            TaskExecutor(queue, "not a handler")


class TestTaskHandlerProtocol:

    def test_capturing_handler_satisfies_protocol(self):
        assert isinstance(CapturingHandler(), TaskHandler)

    def test_logging_handler_satisfies_protocol(self):
        assert isinstance(LoggingHandler(), TaskHandler)

    def test_print_handler_satisfies_protocol(self):
        assert isinstance(PrintHandler(), TaskHandler)

    def test_status_filter_handler_satisfies_protocol(self):
        inner = LoggingHandler()
        handler = StatusFilterHandler("pending", inner)
        assert isinstance(handler, TaskHandler)

    def test_plain_object_does_not_satisfy_protocol(self):
        assert not isinstance(object(), TaskHandler)


class TestStatusFilterHandler:

    @pytest.mark.asyncio
    async def test_passes_matching_status(self):
        inner = CapturingHandler()
        handler = StatusFilterHandler("pending", inner)

        task = Task(
            input_id=1, input_description="t", input_priority=1,
            input_status="pending", input_create_time="2026-01-01 00:00:00",
            input_deadline_time="2026-01-01 00:00:00"
        )
        await handler.handle(task)
        assert len(inner.handled) == 1

    @pytest.mark.asyncio
    async def test_blocks_non_matching_status(self):
        inner = CapturingHandler()
        handler = StatusFilterHandler("pending", inner)

        task = Task(
            input_id=2, input_description="t", input_priority=1,
            input_status="active", input_create_time="2026-01-01 00:00:00",
            input_deadline_time="2026-01-01 00:00:00"
        )
        await handler.handle(task)
        assert len(inner.handled) == 0

    @pytest.mark.asyncio
    async def test_filter_handler_in_executor(self):
        inner = CapturingHandler()
        handler = StatusFilterHandler("pending", inner)
        queue = TaskQueue(GenerateSource(5))

        async with TaskExecutor(queue, handler) as executor:
            await executor.run()

        assert len(inner.handled) == 5
