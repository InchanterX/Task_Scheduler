from dataclasses import dataclass
from datetime import datetime, timedelta

from src.models.id_field import IdField
from src.models.description_field import DescriptionField
from src.models.priority_field import PriorityField
from src.models.status_field import StatusField
from src.models.create_field import CreateField
from src.models.deadline_field import DeadlineField


@dataclass
class Task:
    '''Task model'''
    id: int = IdField()
    description: str = DescriptionField()
    priority: int = PriorityField()
    status: str = StatusField()
    create_time: datetime = CreateField()
    deadline_time: datetime = DeadlineField()

    def __init__(
            self,
            input_id: int,
            input_description: str,
            input_priority: int,
            input_status: str,
            input_create_time: str,
            input_deadline_time: str,
    ):
        self.id = input_id
        self.description = input_description
        self.priority = input_priority
        self.status = input_status
        self.create_time = input_create_time
        self.deadline_time = input_deadline_time

    @property
    def duration(self):
        time_delta = self.deadline_time - self.create_time
        if time_delta < timedelta(0):
            self.status = "expired"
            return timedelta(0)
        else:
            return time_delta
