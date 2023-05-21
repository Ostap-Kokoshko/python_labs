from abc import ABC, abstractmethod


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
        self.name = name
        self.capacity = capacity
        self.current_attendance = current_attendance

    @abstractmethod
    def get_supported_sports(self):
        """
        Abstract method to be implemented by subclasses.

        This method should return a list of sports supported by the stadium.

        Returns:
            list: A list of sports supported by the stadium.
        """
        pass

    def __str__(self):
        return f"Name - {self.name}, Capacity = {self.capacity}, Current Attendance = {self.current_attendance}"