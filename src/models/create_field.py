from datetime import datetime

from src.infrastructure.validation import time_validation


class CreateField:
    '''Creation field for Task model'''

    def __set_name__(self, owner, name) -> None:
        '''Determine the attribute name'''
        self.attr_name = "_" + name

    def __set__(self, field_instance, create_date: str) -> None:
        '''Determine how creation date will set when assigned'''
        if not isinstance(create_date, str):
            raise TypeError(
                "Creation date must be in the format: YYYY-MM-DD HH:MM:SS")
        elif not time_validation(create_date):
            raise ValueError(
                f"Time must be in the format: YYYY-MM-DD HH:MM:SS\nFormat of the line you entered is:      {create_date} and have type {type(create_date)}")

        if self.attr_name in field_instance.__dict__:
            raise PermissionError("Creation time can't be modified!")
        field_instance.__dict__[
            self.attr_name] = datetime.strptime(create_date, "%Y-%m-%d %H:%M:%S")

    def __get__(self, field_instance, owner=None):
        '''Determine how creation date will get when accessed'''
        if not field_instance:
            return self
        return field_instance.__dict__[self.attr_name]

    def __delete__(self, field_instance) -> None:
        '''Determine how creation date will be deleted'''
        raise PermissionError("Creation time can't be deleted!")
