class StatusField:
    '''Status field for Task model'''

    def __set_name__(self, owner, name) -> None:
        '''Determine the attribute name'''
        self.attr_name = "_" + name

    def __set__(self, field_instance, status) -> None:
        '''Determine how status will set when assigned'''
        if not isinstance(status, str):
            raise TypeError("Status must be a string!")
        elif status.lower() not in ["pending", "active", "finished", "canceled"]:
            raise ValueError(
                "Status of the Task can only be: pending, active, finished, canceled")
        field_instance.__dict__[self.attr_name] = status.lower()

    def __get__(self, field_instance, owner=None):
        '''Determine how status will get when accessed'''
        if not field_instance:
            return self
        return field_instance.__dict__[self.attr_name]

    def __delete__(self, field_instance) -> None:
        '''Determine how status will be deleted'''
        raise PermissionError("Task Status can't be deleted!")
