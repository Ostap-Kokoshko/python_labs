"""
Import abstract stadium.
"""
from models.abstract_stadium import AbstractStadium
# pylint: disable = line-too-long
# pylint: disable = too-many-arguments


class SkiResort(AbstractStadium):
    """
    Class representing a ski resort stadium.

    This class inherits from the AbstractStadium class and provides specific implementation for a ski resort.

    Attributes:
        name (str): The name of the ski resort.
        capacity (int): The maximum capacity of the ski resort.
        current_attendance (int): The current number of attendees in the ski resort.
        descent_length (float): The length of the ski descent in the resort.
        slope_steepness_in_degrees (float): The steepness of the ski slope in degrees.
    """

    def __init__(self, name, capacity, current_attendance, descent_length, slope_steepness_in_degrees):
        """
        Params:
            name (str): The name of the ski resort.
            capacity (int): The maximum capacity of the ski resort.
            current_attendance (int): The current number of attendees in the ski resort.
            descent_length (float): The length of the ski descent in the resort.
            slope_steepness_in_degrees (float): The steepness of the ski slope in degrees.
        """
        super().__init__(name, capacity, current_attendance)
        self.descent_length = descent_length
        self.slope_steepness_in_degrees = slope_steepness_in_degrees

    def get_supported_sports(self):
        """
        Returns a list of sports supported by the ski resort.

        Returns:
            list: A list of sports supported by the ski resort.
        """
        return ["Ski racing", "Biathlon", "FreeStyle", "Ski dueling", "Ski jumping"]

    def __str__(self):
        return f"{super().__str__()}, Descent length - {self.descent_length}, Slope steepness in degrees - " \
               f"{self.slope_steepness_in_degrees}"
