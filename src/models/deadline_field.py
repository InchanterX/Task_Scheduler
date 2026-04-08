from datetime import datetime
from src.infrastructure.validation import time_validation
from src.infrastructure.logger import logger
from typing import Union, Optional


class DeadlineField:
    def __set_name__(self, owner: type, name: str) -> None:
        '''Determine the attribute name'''
        self.attr_name = "_" + name

    def __set__(self, field_instance: object, create_date: str) -> None:
        '''Determine how deadline will set when assigned'''
        if not isinstance(create_date, str):
            logger.error(f"Invalid deadline type: {type(create_date)}")
            raise TypeError(
                "Deadline date must be in the format: YYYY-MM-DD HH:MM:SS")
        elif not time_validation(create_date):
            logger.error(f"Invalid deadline format: {create_date}")
            raise ValueError("Time must be in the format: YYYY-MM-DD HH:MM:SS")

        logger.info(f"Setting deadline for Task: '{create_date}'")
        field_instance.__dict__[
            self.attr_name] = datetime.strptime(create_date, "%Y-%m-%d %H:%M:%S")

    def __get__(self, field_instance: object, owner: Optional[type] = None) -> Union[str, "DeadlineField"]:
        '''Determine how deadline will get when accessed'''
        if not field_instance:
            logger.error("Field instance is required to access deadline.")
            return self
        logger.info(
            f"Accessing deadline for Task. Current deadline: '{field_instance.__dict__.get(self.attr_name)}'")
        return field_instance.__dict__[self.attr_name]

    def __delete__(self, field_instance: object) -> None:
        '''Determine how deadline will be deleted'''
        logger.error("Attempting to delete Task Deadline.")
        raise PermissionError("Deadline time can't be deleted!")
