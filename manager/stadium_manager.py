"""
Representing a stadium manager.
"""
from decorators.register_calls_to_file import register_calls_to_file
from decorators.save_result_to_file import save_result_to_file


# pylint: disable = line-too-long


class StadiumManager:
    """
    Class representing a stadium manager.

    This class manages a collection of stadiums and provides methods for managing and querying stadiums.

    Attributes:
        stadiums (list): A list of stadiums managed by the manager.
    """

    def __init__(self):
        """
        Initializes a new instance of the StadiumManager class.
        """
        self.stadiums = []

    @register_calls_to_file
    def add_stadium(self, stadium):
        """
        Adds a stadium to the manager's collection.

        Args:
            stadium (AbstractStadium): The stadium to add.
        """
        self.stadiums.append(stadium)

    @save_result_to_file
    def find_stadiums_with_capacity(self, capacity):
        """
        Finds stadiums with the specified capacity.

        Args:
            capacity (int): The capacity to search for.

        Returns:
            list: A list of stadiums with the specified capacity.
        """
        return [stadium for stadium in self.stadiums if stadium.capacity == capacity]

    @register_calls_to_file
    def find_stadiums_with_more_attendance_now_than(self, current_attendance):
        """
        Finds stadiums with more current attendance than the specified value.

        Args:
            current_attendance (int): The current attendance threshold.

        Returns:
            list: A list of stadiums with more current attendance than the specified value.
        """
        return [stadium for stadium in self.stadiums if stadium.current_attendance > current_attendance]

    def __len__(self):
        """
        Returns the number of stadiums in the manager's collection.

        Returns:
            int: The number of stadiums in the manager's collection.
        """
        return len(self.stadiums)

    def __getitem__(self, index):
        """
        Returns the stadium at the specified index.

        Args:
            index (int): The index of the stadium to retrieve.

        Returns:
            AbstractStadium: The stadium at the specified index.
        """
        return self.stadiums[index]

    def __iter__(self):
        """
        Returns an iterator over the stadiums in the manager's collection.

        Returns:
            iterator: An iterator over the stadiums in the manager's collection.
        """
        return iter(self.stadiums)

    def get_all_supported_sports_list(self):
        """
        Returns a list of results from calling the do_something() method on each stadium.

        Returns:
            list: A list of results from calling the do_something() method on each stadium.
        """
        return [stadium.get_supported_sports() for stadium in self.stadiums]

    def get_enumerated_stadiums(self):
        """
        Returns a concatenation of each stadium's object and its index in the manager's collection.

        Returns:
            list: A list of tuples containing each stadium's object and its index.
        """
        return [(index, stadium) for index, stadium in enumerate(self.stadiums)]

    def get_zipped_results_of_get_all_supported_sports_list(self):
        """
        Returns a concatenation of each stadium's object and the result of calling the do_something() method on it.

        Returns:
            list: A list of tuples containing each stadium's object and the result of calling the do_something() method on it.
        """
        return [(stadium, result) for stadium, result in zip(self.stadiums)]

    def check_conditions(self, condition_func):
        """
        Returns a dictionary indicating if all and any stadiums satisfy a certain condition.

        Returns:
            dict: A dictionary with keys "all" and "any" indicating if all and any stadiums satisfy a certain condition.
        """
        all_satisfy = all(condition_func(stadium) for stadium in self.stadiums)
        any_satisfy = any(condition_func(stadium) for stadium in self.stadiums)
        return {"all": all_satisfy, "any": any_satisfy}

    def get_attributes_by_type(self, data_type):
        """
        Returns a dictionary with attributes and values of each stadium that have values of the specified type.

        Args:
            data_type (type): The type of values to filter attributes by.

        Returns:
            dict: A dictionary with attributes and values of each stadium that have values of the specified type.
        """
        return {attribute: type_of_attr for obj in self.stadiums for attribute, type_of_attr in obj.__dict__.items()
                if isinstance(type_of_attr, data_type)}
