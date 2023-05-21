from stadium import Stadium

if __name__ == '__main__':
    stadiums = [Stadium() for _ in range(3)]
    stadiums[0] = Stadium("Arena Lviv", 35000, 100, "Shahtar", "Carpatian")
    stadiums[1] = Stadium.get_instance()
    stadiums[2] = Stadium.get_instance()

    for stadium in stadiums:
        print(f"Stadium : {stadium.__str__()}")
