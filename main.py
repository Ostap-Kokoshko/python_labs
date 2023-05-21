from models.stadium import Stadium
from models.swimming_pool import SwimmingPool
from models.ski_resort import SkiResort
from models.skating_rink import SkatingRink
from manager.stadium_manager import StadiumManager

if __name__ == '__main__':
    stadium_manager = StadiumManager()
    stadium_manager.add_stadium(Stadium("Arena Lviv", 30000, 13000, "Shahtar", "Carpatian"))
    stadium_manager.add_stadium(Stadium("Olymp", 40000, 11000, "Ukraine", "Spain"))
    stadium_manager.add_stadium(SwimmingPool("SKA", 44000, 1000, 10, 3000, 2000))
    stadium_manager.add_stadium(SwimmingPool("Kiyv", 50000, 1300, 12, 1500, 4000))
    stadium_manager.add_stadium(SkiResort("Bukovel", 9000, 300, 500.5, 30))
    stadium_manager.add_stadium(SkiResort("Italy", 10000, 300, 325.5, 25))
    stadium_manager.add_stadium(SkatingRink("Ternopil", 10000, 5000, True, 400))
    stadium_manager.add_stadium(SkatingRink("Odesa", 12000, 3000, False, 500))

    for stadium in stadium_manager.stadiums:
        print(stadium)
    print("\n")

    stadiums_with_capacity = stadium_manager.find_stadiums_with_capacity(10000)
    print("Stadiums with capacity:")
    for stadium in stadiums_with_capacity:
        print(stadium)
    print("\n")

    stadiums_with_more_attendance_now_than = stadium_manager.find_stadiums_with_more_attendance_now_than(4000)
    print("Stadiums with more attendance now than:")
    for stadium in stadiums_with_more_attendance_now_than:
        print(stadium)
