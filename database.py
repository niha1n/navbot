class Database:
    def __init__(self):
        self.room_data_mapping = {
            "101": [("./images/101.jpg", "This is Text 1")],
            "102": [("./images/102.jpg", "This is Text 2")],
            "103": [("./images/103.jpg", "This is Text 3")],
            "104": [("./images/104.jpg", "This is Text 4")],
            "105": [("./images/105.jpg", "This is Text 5")],
            "106": [("./images/106.jpg", "This is Text 6")],
        }

    def get_data_for_room(self, room_number):
        return self.room_data_mapping.get(room_number, [])