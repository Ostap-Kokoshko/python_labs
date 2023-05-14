class Stadium:
    PEOPLE_TO_EXPEL = 100
    instance = None

    def __init__(self, name="No information", capacity=0, current_attendance=0, home_team="No information", away_team="No information"):
        self.__name = name
        self.__capacity = capacity
        self.__current_attendance = current_attendance
        self.__home_team = home_team
        self.__away_team = away_team

    @property
    def stadium_name(self):
        return self.__name

    @stadium_name.setter
    def stadium_name(self, new_name):
        self.__name = new_name

    @property
    def stadium_capacity(self):
        return self.__capacity

    @stadium_capacity.setter
    def stadium_capacity(self, new_capacity):
        self.__capacity = new_capacity

    @property
    def stadium_current_attendance(self):
        return self.__current_attendance

    @stadium_current_attendance.setter
    def stadium_current_attendance(self, new_current_attendance):
        self.__current_attendance = new_current_attendance

    @property
    def stadium_home_team(self):
        return self.__home_team

    @stadium_home_team.setter
    def stadium_home_team(self, new_home_team):
        self.__home_team = new_home_team

    @property
    def stadium_away_team(self):
        return self.__away_team

    @stadium_away_team.setter
    def stadium_away_team(self, new_away_team):
        self.__away_team = new_away_team

    @staticmethod
    def get_instance():
        if not Stadium.instance:
            Stadium.instance = Stadium()
        return Stadium.instance

    def add_attendees(self, count):
        new_attendance = self.__current_attendance + count
        if new_attendance > self.__capacity:
            print("The stadium is full!")
            return
        self.__current_attendance = new_attendance

    def decrease_attendance(self):
        if self.__current_attendance >= self.PEOPLE_TO_EXPEL:
            self.__current_attendance -= self.PEOPLE_TO_EXPEL
        else:
            print("There are no attendees left to remove!")

    def change_home_team(self, team_name):
        self.__home_team = team_name

    def change_away_team(self, team_name):
        self.__away_team = team_name

    def __str__(self):
        return f"Name - {self.__name}, capacity = {self.__capacity}, current attendance = " \
               f"{self.__current_attendance}, home team - {self.__home_team}, away team - {self.__away_team}"