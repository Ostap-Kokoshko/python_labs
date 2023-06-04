class NegativeValueException(ValueError):
    """
    Exception raised when a field is assigned a negative value.

    Attributes:
        class_field (str): The name of the field with the negative value.
    """

    def __init__(self, class_field):
        self.class_field = class_field

    def __str__(self):
        return f"Field {self.class_field} can`t have negative value"


class TooManyArguments(ValueError):
    """
    Exception raised when the number of arguments exceeds the limit.

    Attributes:
        class_field (str): The name of the field with too many arguments.
    """

    def __init__(self, class_field):
        self.class_field = class_field

    def __str__(self):
        return f"Field {self.class_field} can`t have more argument"
