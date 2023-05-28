"""
Import abstract stadium.
"""
from models.abstract_stadium import AbstractStadium
# pylint: disable = line-too-long
# pylint: disable = too-many-arguments


class SwimmingPool(AbstractStadium):
    """
    Class representing a swimming pool stadium.

    This class inherits from the AbstractStadium class and provides specific implementation for a swimming pool.

    Attributes:
        name (str): The name of the swimming pool.
        capacity (int): The maximum capacity of the swimming pool.
        current_attendance (int): The current number of attendees in the swimming pool.
        number_of_bathrooms (int): The number of bathrooms available in the swimming pool.
        volume (float): The volume of water in the swimming pool.
        max_number_of_visitors (int): The maximum number of visitors allowed in the swimming pool.
    """

    def __init__(self, name, capacity, current_attendance, number_of_bathrooms, volume, max_number_of_visitors):
        """
        Params:
            name (str): The name of the swimming pool.
            capacity (int): The maximum capacity of the swimming pool.
            current_attendance (int): The current number of attendees in the swimming pool.
            number_of_bathrooms (int): The number of bathrooms available in the swimming pool.
            volume (float): The volume of water in the swimming pool.
            max_number_of_visitors (int): The maximum number of visitors allowed in the swimming pool.
        """
        super().__init__(name, capacity, current_attendance)
        self.number_of_bathrooms = number_of_bathrooms
        self.volume = volume
        self.max_number_of_visitors = max_number_of_visitors
        self.supported_sports_set = {"Swimming", "Water Polo"}

    def get_supported_sports(self):
        """
        Returns a list of sports supported by the swimming pool.

        Returns:
            list: A list of sports supported by the swimming pool.
        """
        return ["Swimming", "Water Polo"]

    def __str__(self):
        return f"{super().__str__()}, Number of bathrooms = {self.number_of_bathrooms}, Volume = {self.volume}, " \
               f"Max number of visitors = {self.max_number_of_visitors}"

    def __repr__(self):
        return f"{super().__str__()}, Number of bathrooms = {self.number_of_bathrooms}, Volume = {self.volume}, " \
               f"Max number of visitors = {self.max_number_of_visitors}"