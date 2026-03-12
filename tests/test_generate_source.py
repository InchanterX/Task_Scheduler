from src.models.task import Task
from src.sources.generate_source import GenerateSource


def test_generate_sources_1():
    a = GenerateSource(1)
    tasks = list(a.get_tasks())
    assert tasks == [Task(id=1, payload='Task number 1')]


def test_generate_sources_10():
    a = GenerateSource(10)
    tasks = list(a.get_tasks())
    assert tasks == [Task(id=1, payload='Task number 1'),
                     Task(id=2, payload='Task number 2'),
                     Task(id=3, payload='Task number 3'),
                     Task(id=4, payload='Task number 4'),
                     Task(id=5, payload='Task number 5'),
                     Task(id=6, payload='Task number 6'),
                     Task(id=7, payload='Task number 7'),
                     Task(id=8, payload='Task number 8'),
                     Task(id=9, payload='Task number 9'),
                     Task(id=10, payload='Task number 10')]
