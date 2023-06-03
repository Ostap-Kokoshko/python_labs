"""
Importing models and manager
"""
from models.stadium import Stadium
from models.swimming_pool import SwimmingPool
from models.ski_resort import SkiResort
from models.skating_rink import SkatingRink
from manager.stadium_manager import StadiumManager
from manager.set_manager import SetManager

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
    # pylint: disable = line-too-long
    print("Stadiums with more attendance now than:")
    for stadium in stadiums_with_more_attendance_now_than:
        print(stadium)

    def capacity_condition(some_stadium):
        return some_stadium.capacity > 10000

    print(f"Test for condition capacity > 3000")
    test_result = stadium_manager.check_conditions(capacity_condition)

    print("All stadiums satisfy the capacity condition: ", test_result["all"])
    print("Any stadiums satisfy the capacity condition: ", test_result["any"])

    test_manager = StadiumManager()
    test_manager.add_stadium(Stadium("Arena Lviv", 30000, 13000, "Shahtar", "Carpatian"))
    test_by_value = test_manager.get_attributes_by_type(int)
    print(f"List of attributes by value: ")
    for test_stadium in test_by_value:
        print(test_stadium)

    set_manager = SetManager(stadium_manager)

    print(f"Length of Set Manager: ", len(set_manager))
    print(f"Items in sets: ")
    for item in set_manager:
        print(item)
