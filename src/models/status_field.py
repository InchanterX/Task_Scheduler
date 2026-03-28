from src.infrastructure.logger import logger


class StatusField:
    '''Status field for Task model'''

    def __set_name__(self, owner, name) -> None:
        '''Determine the attribute name'''
        self.attr_name = "_" + name

    def __set__(self, field_instance, status) -> None:
        '''Determine how status will set when assigned'''
        if not isinstance(status, str):
            logger.error(f"Status must be a string! {type(status)} was given.")
            raise TypeError("Status must be a string!")
        elif status.lower() not in ["pending", "active", "finished", "canceled"]:
            logger.error(f"Invalid status value: {status}")
            raise ValueError(
                f"Status of the Task can only be: pending, active, finished, canceled. {status} was given."
            )
        logger.info(f"Setting status to '{status}' for Task.")
        field_instance.__dict__[self.attr_name] = status.lower()

    def __get__(self, field_instance, owner=None):
        '''Determine how status will get when accessed'''
        if not field_instance:
            logger.error("Field instance is required to access status.")
            return self
        logger.info(
            f"Accessing status for Task. Current status: '{field_instance.__dict__.get(self.attr_name)}'")
        return field_instance.__dict__[self.attr_name]

    def __delete__(self, field_instance) -> None:
        '''Determine how status will be deleted'''
        logger.error("Attempting to delete Task Status.")
        raise PermissionError("Task Status can't be deleted!")
