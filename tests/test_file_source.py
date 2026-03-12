from src.sources.file_source import FileSource
from src.models.task import Task


def test_file_sources_1():
    a = FileSource("thursday.txt")
    tasks = list(a.get_tasks())
    assert tasks == [Task(id=1, payload='Attend networks basics lecture'), Task(id=2, payload='Register to the billiards tournament'), Task(
        id=3, payload='Finish python laboratory work'), Task(id=4, payload='Make linear algebra homework'), Task(id=5, payload='Plan TeamFlow pages scheme and connections')]


def test_file_sources_2():
    a = FileSource("friday.txt")
    tasks = list(a.get_tasks())
    assert tasks == [Task(id=1, payload='Attend Faberge meeting'), Task(id=2, payload='Visit gym'), Task(id=3, payload='Make progress with mathematical analysis homework'), Task(
        id=4, payload='Attend python web development lecture'), Task(id=5, payload='Attend mathematical analysis online seminar')]


def test_file_sources_3():
    a = FileSource("saturday.txt")
    tasks = list(a.get_tasks())
    assert tasks == [Task(id=1, payload='Attend python laboratory work, and lectures'), Task(id=2, payload='Fix bugs in discrete mathematics laboratory work'), Task(
        id=3, payload='Design first page of the Faberge project site'), Task(id=4, payload='Design first page of the TeamFlow project')]


def test_wrong_file_source():
    a = FileSource("wrong_file.txt")
    tasks = list(a.get_tasks())
    assert tasks == []
