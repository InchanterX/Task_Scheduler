class PriorityField:
    def __set_name__(self, owner, name) -> None:
        self.attr_name = "_" + name

    def __set__(self, field_instance, priority) -> None:
        if not isinstance(priority, int):
            raise TypeError("Priority must be an integer!")
        elif priority < 0:
            raise ValueError("Priority must be greater or equal to zero!")
        field_instance.__dict__[self.attr_name] = priority

    def __get__(self, field_instance, owner=None) -> int:
        if not field_instance:
            return self
        return field_instance.__dict__[self.attr_name]

    def __delete__(self, field_instance) -> None:
        raise PermissionError("Task Priority can't be deleted!")
