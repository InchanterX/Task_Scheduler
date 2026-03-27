from datetime import datetime
from src.infrastructure.validation import time_validation


class DeadlineField:
    def __set_name__(self, owner, name) -> None:
        self.attr_name = "_" + name

    def __set__(self, field_instance, create_date: str) -> None:
        if not isinstance(create_date, str):
            raise TypeError(
                "Deadline date must be in the format: YYYY-MM-DD HH:MM:SS")
        elif not time_validation(create_date):
            raise ValueError("Time must be in the format: YYYY-MM-DD HH:MM:SS")

        field_instance.__dict__[
            self.attr_name] = datetime.strptime(create_date, "%Y-%m-%d %H:%M:%S")

    def __get__(self, field_instance, owner=None) -> None:
        if not field_instance:
            return self
        return field_instance.__dict__[self.attr_name]

    def __delete__(self, field_instance) -> None:
        raise PermissionError("Deadline time can't be deleted!")
