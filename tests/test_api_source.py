from src.sources.api_source import ApiSources
from src.models.task import Task


def test_api_sources():
    a = ApiSources()
    tasks = list(a.get_tasks())
    assert tasks == [
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
