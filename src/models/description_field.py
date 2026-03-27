class DescriptionField:
    '''Description field for Task model'''

    def __set_name__(self, owner, name: str):
        '''Determine the attribute name'''
        self.attr_name = "_" + name

    def __set__(self, field_instance, description: str) -> None:
        '''Determine how description will set when assigned'''
        if not isinstance(description, str):
            raise TypeError("Description must be a string!")
        field_instance.__dict__[self.attr_name] = description

    def __get__(self, field_instance, owner=None):
        '''Determine how description will get when accessed'''
        if not field_instance:
            return self
        return field_instance.__dict__[self.attr_name]

    def __delete__(self, field_instance) -> None:
        '''Determine how description will be deleted'''
        if not field_instance:
            return
        field_instance.__dict__[self.attr_name] = ""
