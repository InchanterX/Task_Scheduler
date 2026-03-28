from src.infrastructure.logger import logger


class PriorityField:
    '''Priority field for Task model'''

    def __set_name__(self, owner, name) -> None:
        '''Determine the attribute name'''
        self.attr_name = "_" + name

    def __set__(self, field_instance, priority) -> None:
        '''Determine how priority will set when assigned'''
        if not isinstance(priority, int):
            logger.error(
                f"Priority must be an integer! {type(priority)} was given.")
            raise TypeError("Priority must be an integer!")
        elif priority < 0:
            logger.error(f"Invalid priority value: {priority}")
            raise ValueError("Priority must be greater or equal to zero!")

        logger.info(f"Setting priority for Task: '{priority}'")
        field_instance.__dict__[self.attr_name] = priority

    def __get__(self, field_instance, owner=None):
        '''Determine how priority will get when accessed'''
        if not field_instance:
            logger.error("Field instance is required to access priority.")
            return self
        logger.info(
            f"Accessing priority for Task. Current priority: '{field_instance.__dict__.get(self.attr_name)}'")
        return field_instance.__dict__[self.attr_name]

    def __delete__(self, field_instance) -> None:
        '''Determine how priority will be deleted'''
        logger.error("Attempting to delete Task Priority.")
        raise PermissionError("Task Priority can't be deleted!")
