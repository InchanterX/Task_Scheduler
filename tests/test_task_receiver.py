from src.models.task import Task
from src.sources.generate_source import GenerateSource
from src.sources.api_source import ApiSources
from src.sources.file_source import FileSource
from src.services.task_receiver import TaskReceiver


def test_receive_tasks_via_generator():
    result = TaskReceiver(GenerateSource(1)).receive_tasks()
    assert list(result) == [Task(input_id=1, input_description='Task number 1', input_priority=2, input_status='pending',
                                 input_create_time='2023-01-01 00:00:00', input_deadline_time='2026-01-02 14:14:14')]


def test_receive_tasks_via_api():
    result = TaskReceiver(ApiSources()).receive_tasks()
    assert list(result) == [
        Task(input_id=1,
             input_description='some content 1',
             input_priority=1, input_status='pending',
             input_create_time='2023-01-01 00:00:00',
             input_deadline_time='2026-01-02 14:14:14'
             ),
        Task(input_id=2,
             input_description='some content 2',
             input_priority=3, input_status='active',
             input_create_time='2026-03-01 10:40:00',
             input_deadline_time='2026-04-29 14:14:14'
             )
    ]


def test_receive_tasks_via_file():
    result = TaskReceiver(FileSource("friday.txt")).receive_tasks()
    assert list(result) == [
        Task(input_id=1,
             input_description='Finish sprint presentation',
             input_priority=100,
             input_status='finished',
             input_create_time='2026-03-26 23:00:00',
             input_deadline_time='2026-03-27 09:00:00'),
        Task(input_id=2,
             input_description='Presentation protection',
             input_priority=1000,
             input_status='finished',
             input_create_time='2026-03-06 23:00:00',
             input_deadline_time='2026-03-27 09:15:00'),
        Task(input_id=3,
             input_description='Python laboratory work',
             input_priority=10,
             input_status='active',
             input_create_time='2026-03-14 12:00:00',
             input_deadline_time='2026-03-28 23:59:59'),
        Task(input_id=4,
             input_description='Prepare to Python context',
             input_priority=90,
             input_status='active',
             input_create_time='2026-03-21 12:00:00',
             input_deadline_time='2026-03-28 13:00:00'),
    ]


def test_display_received_tasks_1():
    result = TaskReceiver(GenerateSource(1))
    tasks = result.display_tasks()
    assert not tasks


def test_display_received_tasks_2():
    result = TaskReceiver(FileSource("sus"))
    tasks = result.display_tasks()
    assert not tasks
