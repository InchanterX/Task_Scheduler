class DescriptionField:
    def __set_name__(self, owner, name: str):
        self.attr_name = "_" + name

    def __set__(self, field_instance, description: str) -> None:
        if not isinstance(description, str):
            raise TypeError(
                f"Description must be a string!")
        field_instance.__dict__[self.attr_name] = description

    def __get__(self, field_instance, owner=None) -> str:
        if not field_instance:
            return self
        return field_instance.__dict__[self.attr_name]

    def __delete__(self, field_instance) -> None:
        if not field_instance:
            return
        field_instance.__dict__[self.attr_name] = ""
