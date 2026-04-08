from src.models.task import Task
import pytest


def test_task_id():
    task = Task(input_id=1, input_description='Test task', input_priority=1, input_status='pending',
                input_create_time='2023-01-01 00:00:00', input_deadline_time='2026-01-02 14:14:14')
    assert task.id == 1


def test_task_id_cannot_be_modified():
    task = Task(input_id=1, input_description='Test task', input_priority=1, input_status='pending',
                input_create_time='2023-01-01 00:00:00', input_deadline_time='2026-01-02 14:14:14')
    with pytest.raises(PermissionError, match="Task ID can't be modified!"):
        task.id = 2


def test_task_id_cannot_be_deleted():
    task = Task(input_id=1, input_description='Test task', input_priority=1, input_status='pending',
                input_create_time='2023-01-01 00:00:00', input_deadline_time='2026-01-02 14:14:14')
    with pytest.raises(PermissionError, match="Task ID can't be deleted!"):
        del task.id


def test_task_description():
    task = Task(input_id=1, input_description='Test task', input_priority=1, input_status='pending',
                input_create_time='2023-01-01 00:00:00', input_deadline_time='2026-01-02 14:14:14')
    assert task.description == 'Test task'


def test_task_description_can_be_modified():
    task = Task(input_id=1, input_description='Test task', input_priority=1, input_status='pending',
                input_create_time='2023-01-01 00:00:00', input_deadline_time='2026-01-02 14:14:14')
    task.description = 'New description'
    assert task.description == 'New description'


def test_task_description_can_be_deleted():
    task = Task(input_id=1, input_description='Test task', input_priority=1, input_status='pending',
                input_create_time='2023-01-01 00:00:00', input_deadline_time='2026-01-02 14:14:14')
    del task.description
    assert task.description == ''


def test_task_priority():
    task = Task(input_id=1, input_description='Test task', input_priority=5, input_status='pending',
                input_create_time='2023-01-01 00:00:00', input_deadline_time='2026-01-02 14:14:14')
    assert task.priority == 5


def test_task_priority_can_be_modified():
    task = Task(input_id=1, input_description='Test task', input_priority=5, input_status='pending',
                input_create_time='2023-01-01 00:00:00', input_deadline_time='2026-01-02 14:14:14')
    task.priority = 10
    assert task.priority == 10


def test_task_priority_cannot_be_deleted():
    task = Task(input_id=1, input_description='Test task', input_priority=5, input_status='pending',
                input_create_time='2023-01-01 00:00:00', input_deadline_time='2026-01-02 14:14:14')
    with pytest.raises(PermissionError, match="Task Priority can't be deleted!"):
        del task.priority


def test_task_status():
    task = Task(input_id=1, input_description='Test task', input_priority=1, input_status='pending',
                input_create_time='2023-01-01 00:00:00', input_deadline_time='2026-01-02 14:14:14')
    assert task.status == 'pending'


def test_task_status_can_be_modified():
    task = Task(input_id=1, input_description='Test task', input_priority=1, input_status='pending',
                input_create_time='2023-01-01 00:00:00', input_deadline_time='2026-01-02 14:14:14')
    task.status = 'active'
    assert task.status == 'active'


def test_task_status_cannot_be_deleted():
    task = Task(input_id=1, input_description='Test task', input_priority=1, input_status='pending',
                input_create_time='2023-01-01 00:00:00', input_deadline_time='2026-01-02 14:14:14')
    with pytest.raises(PermissionError, match="Task Status can't be deleted!"):
        del task.status


def test_task_create_time():
    task = Task(input_id=1, input_description='Test task', input_priority=1, input_status='pending',
                input_create_time='2023-01-01 00:00:00', input_deadline_time='2026-01-02 14:14:14')
    assert str(task.create_time) == '2023-01-01 00:00:00'


def test_task_create_time_cannot_be_modified():
    task = Task(input_id=1, input_description='Test task', input_priority=1, input_status='pending',
                input_create_time='2023-01-01 00:00:00', input_deadline_time='2026-01-02 14:14:14')
    with pytest.raises(PermissionError, match="Creation time can't be modified!"):
        task.create_time = '2024-01-01 00:00:00'


def test_task_create_time_cannot_be_deleted():
    task = Task(input_id=1, input_description='Test task', input_priority=1, input_status='pending',
                input_create_time='2023-01-01 00:00:00', input_deadline_time='2026-01-02 14:14:14')
    with pytest.raises(PermissionError, match="Creation time can't be deleted!"):
        del task.create_time


def test_task_deadline_time():
    task = Task(input_id=1, input_description='Test task', input_priority=1, input_status='pending',
                input_create_time='2023-01-01 00:00:00', input_deadline_time='2026-01-02 14:14:14')
    assert str(task.deadline_time) == '2026-01-02 14:14:14'


def test_task_deadline_time_can_be_modified():
    task = Task(input_id=1, input_description='Test task', input_priority=1, input_status='pending',
                input_create_time='2023-01-01 00:00:00', input_deadline_time='2026-01-02 14:14:14')
    task.deadline_time = '2026-12-31 23:59:59'
    assert str(task.deadline_time) == '2026-12-31 23:59:59'


def test_task_deadline_time_cannot_be_deleted():
    task = Task(input_id=1, input_description='Test task', input_priority=1, input_status='pending',
                input_create_time='2023-01-01 00:00:00', input_deadline_time='2026-01-02 14:14:14')
    with pytest.raises(PermissionError, match="Deadline time can't be deleted!"):
        del task.deadline_time
