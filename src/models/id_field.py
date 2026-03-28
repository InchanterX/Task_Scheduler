from src.infrastructure.logger import logger


class IdField:
    '''ID field for Task model'''

    def __set_name__(self, owner, name):
        '''Determine the attribute name'''
        self.attr_name = "_" + name

    def __set__(self, field_instance, id: int) -> None:
        '''Determine how ID will set when assigned'''
        if not isinstance(id, int):
            logger.error(f"ID must be an integer! {type(id)} was given.")
            raise TypeError("ID must be an integer!")
        elif id < 0:
            logger.error(f"Invalid ID value: {id}")
            raise ValueError("ID must be greater or equal to zero!")

        if self.attr_name in vars(field_instance):
            logger.error("Task ID can't be modified!")
            raise PermissionError("Task ID can't be modified!")
        logger.info(f"Setting ID for Task: '{id}'")
        field_instance.__dict__[self.attr_name] = id

    def __get__(self, field_instance, owner=None):
        '''Determine how ID will get when accessed'''
        if not field_instance:
            logger.error("Field instance is required to access Task ID.")
            return self
        logger.info(
            f"Accessing ID for Task. Current ID: '{field_instance.__dict__.get(self.attr_name)}'")
        return field_instance.__dict__[self.attr_name]

    def __delete__(self, field_instance) -> None:
        '''Determine how ID will be deleted'''
        logger.error("Attempting to delete Task ID.")
        raise PermissionError("Task ID can't be deleted!")
