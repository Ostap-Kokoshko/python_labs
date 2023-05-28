"""
Import abstract stadium.
"""
from models.abstract_stadium import AbstractStadium
# pylint: disable = line-too-long
# pylint: disable = too-many-arguments


class SkatingRink(AbstractStadium):
    """
    Class representing a skating rink stadium.

    This class inherits from the AbstractStadium class and provides specific implementation for a skating rink.

    Attributes:
        name (str): The name of the skating rink.
        capacity (int): The maximum capacity of the skating rink.
        current_attendance (int): The current number of attendees in the skating rink.
        has_natural_ice (bool): Indicates whether the skating rink has natural ice or not.
        area_in_square_meters (float): The area of the skating rink in square meters.
    """

    def __init__(self, name, capacity, current_attendance, has_natural_ice, area_in_square_meters):
        """
        Params:
            name (str): The name of the skating rink.
            capacity (int): The maximum capacity of the skating rink.
            current_attendance (int): The current number of attendees in the skating rink.
            has_natural_ice (bool): Indicates whether the skating rink has natural ice or not.
            area_in_square_meters (float): The area of the skating rink in square meters.
        """
        super().__init__(name, capacity, current_attendance)
        self.has_natural_ice = has_natural_ice
        self.area_in_square_meters = area_in_square_meters
        self.supported_sports_set = {"Hockey", "Figure skating"}

    def get_supported_sports(self):
        """
        Returns a list of sports supported by the skating rink.

        Returns:
            list: A list of sports supported by the skating rink.
        """
        return ["Hockey", "Figure skating"]

    def __str__(self):
        return f"{super().__str__()}, Has natural ice - {self.has_natural_ice}, " \
               f"Area in square meters - {self.area_in_square_meters}"
