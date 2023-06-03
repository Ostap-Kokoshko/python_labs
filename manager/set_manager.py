"""
This is set manager file
"""


class SetManager:
    """
    Set Manager class for working with the sets of objects in a regular manager.

    Attributes:
        stadium_manager (RM): The regular manager containing the objects.
    """

    def __init__(self, stadium_manager):
        self.stadium_manager = stadium_manager
        self.index = 0

    def __iter__(self):
        """
        Returns an iterator over the sets of objects in the regular manager.

        Returns:
            iterator: An iterator over the sets of objects in the regular manager.
        """
        return iter(item for stadium in self.stadium_manager.stadiums for item in stadium.supported_sports_set)

    def __len__(self):
        """
        Returns the total number of elements in the sets of objects in the regular manager.

        Returns:
            int: The total number of elements in the sets.
        """
        return sum(len(stadium.supported_sports_set) for stadium in self.stadium_manager.stadiums)

    def __getitem__(self, index):
        """
        Returns the item at the specified index in the concatenated sets of objects.

        Args:
            index (int): The index of the item to retrieve.

        Returns:
            object: The item at the specified index.
        """
        sets = [stadium.supported_sports_set for stadium in self.stadium_manager.stadiums]
        flattened_list = [item for item_set in sets for item in item_set]
        return flattened_list[index]

    def __next__(self):
        """
        Returns the next item in the concatenated sets of objects.

        Returns:
            object: The next item.

        Raises:
            StopIteration: If there are no more items.
        """
        sets = [stadium.supported_sports_set for stadium in self.stadium_manager.stadiums]
        flattened_list = [item for item_set in sets for item in item_set]
        if self.index < len(flattened_list):
            item = flattened_list[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration
