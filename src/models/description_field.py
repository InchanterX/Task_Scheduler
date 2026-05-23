from src.infrastructure.logger import logger
from typing import Union, Optional


class DescriptionField:
    '''Description field for Task model'''

    def __set_name__(self, owner: type, name: str):
        '''Determine the attribute name'''
        self.attr_name = "_" + name

    def __set__(self, field_instance: object, description: str) -> None:
        '''Determine how description will set when assigned'''
        if not isinstance(description, str):
            logger.error(f"Invalid description type: {type(description)}")
            raise TypeError("Description must be a string!")
        logger.debug(f"Setting description for Task: '{description}'")
        field_instance.__dict__[self.attr_name] = description

    def __get__(self, field_instance: object, owner: Optional[type] = None) -> Union[str, "DescriptionField"]:
        '''Determine how description will get when accessed'''
        if not field_instance:
            logger.error("Field instance is required to access description.")
            return self
        logger.debug(
            f"Accessing description for Task. Current description: '{field_instance.__dict__.get(self.attr_name)}'")
        return field_instance.__dict__[self.attr_name]

    def __delete__(self, field_instance) -> None:
        '''Determine how description will be deleted'''
        if not field_instance:
            logger.error("Field instance is required to delete description.")
            return
        logger.debug(
            f"Deleting description for Task. Current description: '{field_instance.__dict__.get(self.attr_name)}'")
        field_instance.__dict__[self.attr_name] = ""
