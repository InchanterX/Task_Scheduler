from src.models.task import Task
import pytest


@pytest.fixture
def base_task():
    return Task(input_id=1, input_description='Test task', input_priority=1, input_status='pending',
                input_create_time='2026-01-01 00:00:00', input_deadline_time='2026-01-02 14:14:14')


def test_task_id(base_task):
    assert base_task.id == 1


@pytest.mark.parametrize("field_name,new_value,error_msg", [
    ("id", 2, "Task ID can't be modified!"),
    ("create_time", "2026-01-01 00:00:00", "Creation time can't be modified!"),
])
def test_field_cannot_be_modified(base_task, field_name, new_value, error_msg):
    with pytest.raises(PermissionError, match=error_msg):
        setattr(base_task, field_name, new_value)


@pytest.mark.parametrize("field_name,error_msg", [
    ("id", "Task ID can't be deleted!"),
    ("priority", "Task Priority can't be deleted!"),
    ("status", "Task Status can't be deleted!"),
    ("create_time", "Creation time can't be deleted!"),
    ("deadline_time", "Deadline time can't be deleted!"),
])
def test_field_cannot_be_deleted(base_task, field_name, error_msg):
    with pytest.raises(PermissionError, match=error_msg):
        delattr(base_task, field_name)


def test_task_description(base_task):
    assert base_task.description == 'Test task'


def test_task_description_can_be_deleted(base_task):
    del base_task.description
    assert base_task.description == ''


def test_task_priority(base_task):
    assert base_task.priority == 1


@pytest.mark.parametrize("field_name,initial_value,new_value,expected", [
    ("description", "Test task", "New description", "New description"),
    ("priority", 5, 10, 10),
    ("deadline_time", "2026-01-02 14:14:14",
     "2026-12-31 23:59:59", "2026-12-31 23:59:59"),
])
def test_field_can_be_modified(base_task, field_name, initial_value, new_value, expected):
    setattr(base_task, field_name, new_value)
    assert str(getattr(base_task, field_name)) == str(expected)


def test_task_status(base_task):
    assert base_task.status == 'pending'


def test_task_create_time(base_task):
    assert str(base_task.create_time) == '2026-01-01 00:00:00'


def test_task_deadline_time(base_task):
    assert str(base_task.deadline_time) == '2026-01-02 14:14:14'
