class PriorityField:
    '''Priority field for Task model'''

    def __set_name__(self, owner, name) -> None:
        '''Determine the attribute name'''
        self.attr_name = "_" + name

    def __set__(self, field_instance, priority) -> None:
        '''Determine how priority will set when assigned'''
        if not isinstance(priority, int):
            raise TypeError("Priority must be an integer!")
        elif priority < 0:
            raise ValueError("Priority must be greater or equal to zero!")
        field_instance.__dict__[self.attr_name] = priority

    def __get__(self, field_instance, owner=None):
        '''Determine how priority will get when accessed'''
        if not field_instance:
            return self
        return field_instance.__dict__[self.attr_name]

    def __delete__(self, field_instance) -> None:
        '''Determine how priority will be deleted'''
        raise PermissionError("Task Priority can't be deleted!")
