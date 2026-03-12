from src.sources.api_source import ApiSources
from src.models.task import Task


def test_api_sources():
    a = ApiSources()
    tasks = list(a.get_tasks())
    assert tasks == [Task(id=1, payload='some content 1'),
                     Task(id=2, payload='some content 2')]
