class IdField:
    def __set_name__(self, owner, name):
        self.attr_name = "_" + name

    def __set__(self, field_instance, id: int) -> None:
        if not isinstance(id, int):
            raise TypeError("ID must be an integer!")
        elif id < 0:
            raise ValueError("ID must be greater or equal to zero!")

        if self.attr_name in vars(field_instance):
            raise PermissionError("Task ID can't be modified!")
        field_instance.__dict__[self.attr_name] = id

    def __get__(self, field_instance, owner=None) -> None:
        if not field_instance:
            return self
        return field_instance.__dict__[self.attr_name]

    def __delete__(self, field_instance) -> None:
        raise PermissionError("Task ID can't be deleted!")
