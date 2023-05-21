class StadiumManager:
    """
    Class representing a stadium manager.

    This class manages a collection of stadiums and provides methods for managing and querying stadiums.

    Attributes:
        stadiums (list): A list of stadiums managed by the manager.
    """
    def __init__(self):
        self.stadiums = []

    def add_stadium(self, stadium):
        """
        Adds a stadium to the manager's collection.

        Args:
            stadium (AbstractStadium): The stadium to add.
        """
        self.stadiums.append(stadium)

    def find_stadiums_with_capacity(self, capacity):
        """
        Finds stadiums with the specified capacity.

        Args:
            capacity (int): The capacity to search for.

        Returns:
            list: A list of stadiums with the specified capacity.
        """
        return [stadium for stadium in self.stadiums if stadium.capacity == capacity]

    def find_stadiums_with_more_attendance_now_than(self, current_attendance):
        """
        Finds stadiums with more current attendance than the specified value.

        Args:
            current_attendance (int): The current attendance threshold.

        Returns:
            list: A list of stadiums with more current attendance than the specified value.
        """
        return [stadium for stadium in self.stadiums if stadium.current_attendance > current_attendance]
