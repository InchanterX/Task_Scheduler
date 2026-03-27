from src.sources.file_source import FileSource
from src.models.task import Task


def test_file_sources_2():
    a = FileSource("friday.txt")
    tasks = list(a.get_tasks())
    assert tasks == [
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


def test_wrong_file_source():
    a = FileSource("wrong_file.txt")
    tasks = list(a.get_tasks())
    assert tasks == []
