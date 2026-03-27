from src.models.task import Task
from src.sources.generate_source import GenerateSource


def test_generate_sources_1():
    a = GenerateSource(1)
    tasks = list(a.get_tasks())
    assert tasks == [Task(input_id=1, input_description='Task number 1', input_priority=2, input_status='pending',
                          input_create_time='2023-01-01 00:00:00', input_deadline_time='2026-01-02 14:14:14')
                     ]


def test_generate_sources_10():
    a = GenerateSource(10)
    tasks = list(a.get_tasks())
    assert tasks == [
        Task(input_id=1, input_description='Task number 1', input_priority=2, input_status='pending',
             input_create_time='2023-01-01 00:00:00', input_deadline_time='2026-01-02 14:14:14'),
        Task(input_id=2, input_description='Task number 2', input_priority=3, input_status='pending',
             input_create_time='2023-01-01 00:00:00', input_deadline_time='2026-01-02 14:14:14'),
        Task(input_id=3, input_description='Task number 3', input_priority=4, input_status='pending',
             input_create_time='2023-01-01 00:00:00', input_deadline_time='2026-01-02 14:14:14'),
        Task(input_id=4, input_description='Task number 4', input_priority=5, input_status='pending',
             input_create_time='2023-01-01 00:00:00', input_deadline_time='2026-01-02 14:14:14'),
        Task(input_id=5, input_description='Task number 5', input_priority=1, input_status='pending',
             input_create_time='2023-01-01 00:00:00', input_deadline_time='2026-01-02 14:14:14'),
        Task(input_id=6, input_description='Task number 6', input_priority=2, input_status='pending',
             input_create_time='2023-01-01 00:00:00', input_deadline_time='2026-01-02 14:14:14'),
        Task(input_id=7, input_description='Task number 7', input_priority=3, input_status='pending',
             input_create_time='2023-01-01 00:00:00', input_deadline_time='2026-01-02 14:14:14'),
        Task(input_id=8, input_description='Task number 8', input_priority=4, input_status='pending',
             input_create_time='2023-01-01 00:00:00', input_deadline_time='2026-01-02 14:14:14'),
        Task(input_id=9, input_description='Task number 9', input_priority=5, input_status='pending',
             input_create_time='2023-01-01 00:00:00', input_deadline_time='2026-01-02 14:14:14'),
        Task(input_id=10, input_description='Task number 10', input_priority=1, input_status='pending',
             input_create_time='2023-01-01 00:00:00', input_deadline_time='2026-01-02 14:14:14'),
    ]
