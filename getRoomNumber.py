from database import Database
database = Database()


def validate_room_number(room_number, db):
    if db.room_exists(room_number):
        return True
    else:
        return False


def get_room_number_from_input(room_number):
    if validate_room_number(room_number, database):
        return room_number
    else:
        print("Invalid room number. Please try again.")

