"""
Import abstract stadium.
"""
from models.abstract_stadium import AbstractStadium
# pylint: disable = line-too-long
# pylint: disable = too-many-arguments


class Stadium(AbstractStadium):
    """
    Class representing a stadium.

    This class inherits from the AbstractStadium class and provides specific implementation for a stadium.

    Attributes:
        name (str): The name of the stadium.
        capacity (int): The maximum capacity of the stadium.
        current_attendance (int): The current number of attendees in the stadium.
        PEOPLE_TO_EXPEL (int): The number of attendees to expel at once.
        home_team (str): The name of the home team.
        away_team (str): The name of the away team.
    """
    PEOPLE_TO_EXPEL = 100

    def __init__(self, name, capacity, current_attendance, home_team, away_team):
        """
        Params:
            name (str): The name of the stadium.
            capacity (int): The maximum capacity of the stadium.
            current_attendance (int): The current number of attendees in the stadium.
            home_team (str): The name of the home team.
            away_team (str): The name of the away team.
        """
        super().__init__(name, capacity, current_attendance)
        self.home_team = home_team
        self.away_team = away_team
        self.supported_sports_set = {"Football", "Basketball", "Tennis"}

    def add_attendees(self, count):
        """
        Adds the specified number of attendees to the stadium.
        If the new attendance exceeds the stadium capacity, a message is printed.

        Args:
            count (int): The number of attendees to add.
        """
        new_attendance = self.current_attendance + count
        if new_attendance > self.capacity:
            print("The stadium is full!")
            return
        self.current_attendance = new_attendance

    def decrease_attendance(self):
        """
        Decreases the attendance by expelling a fixed number of attendees.
        If there are fewer attendees than the number to expel, a message is printed.
        """
        if self.current_attendance >= self.PEOPLE_TO_EXPEL:
            self.current_attendance -= self.PEOPLE_TO_EXPEL
        else:
            print("There are no attendees left to remove!")

    def change_home_team(self, team_name):
        """
        Changes the home team name.

        Args:
            team_name (str): The new name of the home team.
        """
        self.home_team = team_name

    def change_away_team(self, team_name):
        """
        Changes the away team name.

        Args:
            team_name (str): The new name of the away team.
        """
        self.away_team = team_name

    def get_supported_sports(self):
        """
        Returns a list of sports supported by the stadium.

        Returns:
            list: A list of sports supported by the stadium.
        """
        return ["Football", "Basketball", "Tennis"]

    def __str__(self):
        return f"{super().__str__()}, " \
               f"{self.current_attendance}, Home team - {self.home_team}, Away team - {self.away_team}"
