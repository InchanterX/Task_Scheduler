from datetime import datetime
from typing import Union, Optional
from src.infrastructure.validation import time_validation
from src.infrastructure.logger import logger


class CreateField:
    '''Creation field for Task model'''

    def __set_name__(self, owner: type, name: str) -> None:
        '''Determine the attribute name'''
        self.attr_name = "_" + name

    def __set__(self, field_instance: object, create_date: str) -> None:
        '''Determine how creation date will set when assigned'''
        if not isinstance(create_date, str):
            logger.error(f"Invalid creation date type: {type(create_date)}")
            raise TypeError(
                "Creation date must be in the format: YYYY-MM-DD HH:MM:SS")
        elif not time_validation(create_date):
            logger.error(f"Invalid creation date format: {create_date}")
            raise ValueError(
                f"Time must be in the format: YYYY-MM-DD HH:MM:SS\nFormat of the line you entered is:      {create_date} and have type {type(create_date)}")

        if self.attr_name in field_instance.__dict__:
            logger.error("Creation time can't be modified!")
            raise PermissionError("Creation time can't be modified!")

        logger.info(f"Setting creation time for Task: '{create_date}'")
        field_instance.__dict__[
            self.attr_name] = datetime.strptime(create_date, "%Y-%m-%d %H:%M:%S")

    def __get__(self, field_instance: object, owner: Optional[type] = None) -> Union[str, "CreateField"]:
        '''Determine how creation date will get when accessed'''
        if not field_instance:
            logger.error("Field instance is required to access creation date.")
            return self
        logger.info(
            f"Accessing creation date for Task. Current creation date: '{field_instance.__dict__.get(self.attr_name)}'")
        return field_instance.__dict__[self.attr_name]

    def __delete__(self, field_instance: object) -> None:
        '''Determine how creation date will be deleted'''
        logger.error("Attempting to delete Task Creation Date.")
        raise PermissionError("Creation time can't be deleted!")
