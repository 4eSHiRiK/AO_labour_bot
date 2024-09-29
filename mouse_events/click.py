import pyautogui

import time


def click(x: int, y: int) -> None:
    """
    Imitation of mouse's click
    :param x: coord
    :param y: coord
    :return: None
    """

    pyautogui.moveTo(x, y)
    time.sleep(0.2)
    pyautogui.click(button="left")
    time.sleep(0.1)


def click_drags(start_x, start_y, end_x, end_y) -> None:
    """
    Imitation of mouse's drag
    :param start_x:
    :param start_y:
    :param end_x:
    :param end_y:
    :return:
    """
    pyautogui.moveTo(start_x, start_y)
    pyautogui.dragTo(end_x, end_y, duration=0.4)


def move_cursor(x: int, y: int) -> None:
    pyautogui.moveTo(x, y)


def perform_shift_click(x, y) -> None:  # not working as physical mouse
    pyautogui.keyDown("shift")
    time.sleep(1)
    pyautogui.moveTo(x, y, duration=0.25)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(1)

    pyautogui.keyUp("shift")
    time.sleep(0.2)


def find_and_click(image_path) -> None:  # not used
    try:
        image_location = pyautogui.locateOnScreen(image_path, confidence=0.8)

        if image_location is not None:
            center_x, center_y = pyautogui.center(image_location)

            pyautogui.click(center_x, center_y)
            print(f"Click on image: {image_path}")
        else:
            print(f"Image {image_path} not found.")
    except pyautogui.ImageNotFoundException:
        print(f"Image {image_path} not found (exception).")
