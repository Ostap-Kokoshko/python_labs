class Stadium:
    """
    Represents a stadium.

    Attributes:
        PEOPLE_TO_EXPEL (int): One hundred of attendees to expel at once.
        name (str): The name of the stadium.
        capacity (int): The maximum capacity of the stadium.
        current_attendance (int): The current number of attendees in the stadium.
        home_team (str): The name of the home team.
        away_team (str): The name of the away team.

    Methods:
        get_instance(): Returns the singleton instance of the Stadium class.
        add_attendees(count: int): Adds the specified number of attendees to the stadium.
        decrease_attendance(): Decreases the attendance by expelling a fixed number of attendees.
        change_home_team(team_name: str): Changes the home team name.
        change_away_team(team_name: str): Changes the away team name.
    """
    PEOPLE_TO_EXPEL = 100
    __instance = None

    def __init__(self, name="No information", capacity=0, current_attendance=0, home_team="None", away_team="None"):
        self.name = name
        self.capacity = capacity
        self.current_attendance = current_attendance
        self.home_team = home_team
        self.away_team = away_team

    @staticmethod
    def get_instance():
        if not Stadium.__instance:
            Stadium.__instance = Stadium()
        return Stadium.__instance

    def add_attendees(self, count):
        new_attendance = self.current_attendance + count
        if new_attendance > self.capacity:
            print("The stadium is full!")
            return
        self.current_attendance = new_attendance

    def decrease_attendance(self):
        if self.current_attendance >= self.PEOPLE_TO_EXPEL:
            self.current_attendance -= self.PEOPLE_TO_EXPEL
        else:
            print("There are no attendees left to remove!")

    def change_home_team(self, team_name):
        self.home_team = team_name

    def change_away_team(self, team_name):
        self.away_team = team_name

    def __str__(self):
        return f"Name - {self.name}, capacity = {self.capacity}, current attendance = " \
               f"{self.current_attendance}, home team - {self.home_team}, away team - {self.away_team}"