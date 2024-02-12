class PathFinder:
    def __init__(self, database):
        self.database = database

    def find_data_for_room(self, room_number):
        room_number = int(room_number)
        side = "right" if room_number % 2 == 0 else "left"

        data = self.database.get_data_for_room(str(room_number))

        if side == "right":
            previous_room_number = room_number + 2
            while previous_room_number <= 106:
                previous_data = self.database.get_data_for_room(str(previous_room_number))
                data.extend(previous_data)
                previous_room_number += 2

        if side == "left":
            previous_room_number = room_number + 2
            while previous_room_number <= 105:
                previous_data = self.database.get_data_for_room(str(previous_room_number))
                data.extend(previous_data)
                previous_room_number += 2

        return data, side
