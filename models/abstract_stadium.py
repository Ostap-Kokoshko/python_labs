"""
Abstract base class representing a stadium.
"""
from abc import ABC, abstractmethod
# pylint: disable = line-too-long
# pylint: disable = too-many-arguments


class AbstractStadium(ABC):
    """
    Abstract base class representing a stadium.

    This class defines the common attributes and methods that are expected to be implemented by concrete stadium classes

    Attributes:
        name (str): The name of the stadium.
        capacity (int): The maximum capacity of the stadium.
        current_attendance (int): The current number of attendees in the stadium.
    """

    def __init__(self, name, capacity, current_attendance):
        """
        Params:
            name (str): The name of the stadium.
            capacity (int): The maximum capacity of the stadium.
            current_attendance (int): The current number of attendees in the stadium.
        """
        self.name = name
        self.capacity = capacity
        self.current_attendance = current_attendance
        self.supported_sports_set = set()

    def __iter__(self):
        return iter(self.supported_sports_set)

    @abstractmethod
    def get_supported_sports(self):
        """
        Abstract method to be implemented by subclasses.

        This method should return a list of sports supported by the stadium.

        Returns:
            list: A list of sports supported by the stadium.
        """

    def __str__(self):
        return f"Name - {self.name}, Capacity = {self.capacity}, Current Attendance = {self.current_attendance}"
