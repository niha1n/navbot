import cv2 as cv
import pyttsx3
import time


def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def show_image(image_path, timeout=2):
    img = cv.imread(image_path)
    cv.namedWindow("Navigation Image", cv.WND_PROP_FULLSCREEN)
    cv.setWindowProperty("Navigation Image", cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
    cv.imshow("Navigation Image", img)
    cv.waitKey(int(timeout * 1000))  # Convert timeout to milliseconds


def display_image_with_text(image_path, text):
    show_image(image_path)
    speak_text(text)
    time.sleep(1)

