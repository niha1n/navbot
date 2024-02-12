from database import Database
from pathFinder import PathFinder
from speechWithImg import display_image_with_text
from speechInput import speech_input
import pyaudio
if __name__ == "__main__":
    # Initialize database
    database = Database()

    # Initialize path-finder
    path_finder = PathFinder(database)
    room_number = speech_input()
    if room_number is None:
        room_number = input("Microphone detection failed. Please enter the room number manually: ")

    # Example: Find data for room 102
    # room_number = str(input("Enter the room number: "))
    data, side = path_finder.find_data_for_room(room_number)

    data.reverse()
    # Display images and speak out text
    for image_path, text in data:
        print("Displaying frame:", image_path)
        display_image_with_text(image_path, text)
