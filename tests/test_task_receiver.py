from src.models.task import Task
from src.sources.generate_source import GenerateSource
from src.sources.api_source import ApiSources
from src.sources.file_source import FileSource
from src.services.task_receiver import TaskReceiver


def test_receive_tasks_via_generator():
    result = TaskReceiver(GenerateSource(1)).receive_tasks()
    assert list(result) == [Task(id=1, payload='Task number 1')]


def test_receive_tasks_via_api():
    result = TaskReceiver(ApiSources()).receive_tasks()
    assert list(result) == [Task(id=1, payload='some content 1'),
                            Task(id=2, payload='some content 2')]


def test_receive_tasks_via_file():
    result = TaskReceiver(FileSource("thursday.txt")).receive_tasks()
    assert list(result) == [Task(id=1, payload='Attend networks basics lecture'), Task(id=2, payload='Register to the billiards tournament'), Task(
        id=3, payload='Finish python laboratory work'), Task(id=4, payload='Make linear algebra homework'), Task(id=5, payload='Plan TeamFlow pages scheme and connections')]


def test_display_received_tasks_1():
    result = TaskReceiver(GenerateSource(1))
    tasks = result.display_tasks()
    assert not tasks


def test_display_received_tasks_2():
    result = TaskReceiver(FileSource("sus"))
    tasks = result.display_tasks()
    assert not tasks
