import time

import pyautogui

from const import (
    images_fletcher,
    images_imbuer,
    images_blacksmith,
    island_num,
    labours,
    labour_coordinates,
    inventory_coords,
)
from mouse_events.click import click, move_cursor, click_drags


def worker_processing(labour_number: int) -> None:
    """
    Collect items from labour and check who it is to put correct journal
    """
    worker_counter: int = 0
    click(282, 945)  # collect items from labour
    time.sleep(0.5)

    for image_path, coords, message in labours:
        try:
            if pyautogui.locateOnScreen(image_path, confidence=0.9) is not None:
                print(
                    f"Putted into {message} number {labour_number} on {island_num.get()} island\n"
                    f"--------------------------------------------------------------------"
                )
                click_drags(*coords)
                break
        except pyautogui.ImageNotFoundException:
            worker_counter += 1
            if worker_counter == 3:

                print(
                    f"Worker number {labour_number}, on island {island_num.get()} not served\n"
                    f"----------------------------------------------------------------"
                )
            continue
    time.sleep(0.5)
    click(145, 943)  # accept work
    time.sleep(0.2)


def walk_to_labours() -> None:
    images = [
        "C:\\AO_labour_bot\\images\\day_flag.png",
        "C:\\AO_labour_bot\\images\\evening_flag.png",
        "C:\\AO_labour_bot\\images\\night_flag.png",
    ]

    way_counter: int = 0

    for image_path in images:
        try:
            """
            Move character from island's start to enter town hall
            """
            if pyautogui.locateOnScreen(image_path, confidence=0.8) is not None:
                print("Way to labours found")
                time.sleep(1)
                click(1920, 0)
                time.sleep(4.7)
                click(1320, 0)
                time.sleep(1.9)
                click(1060, 305)
                time.sleep(1.9)
                """
                Worker_processing
                """
                for labour_number, coords in enumerate(labour_coordinates, start=1):
                    click(*coords)
                    time.sleep(1)
                    worker_processing(labour_number)
                    time.sleep(1)
                pyautogui.press("r")
                time.sleep(20)
                break
        except pyautogui.ImageNotFoundException:
            way_counter += 1
            if way_counter == 3:
                print("Way to labours not found")
            continue


def picking_journals(images: list[str]) -> None:
    """
    Pick journal from base island
    :param images: journals
    :return: None
    """
    for image_path, coords, message in images:
        try:
            if pyautogui.locateOnScreen(image_path, confidence=0.9) is not None:
                print(message)
                click_drags(*coords)
                break
        except pyautogui.ImageNotFoundException:
            continue
    print("Load ended")


def load_from_morgana_chest() -> None:
    click(1153, 278)  # click on journal's morgana chest
    time.sleep(2)
    picking_journals(images_fletcher)  # pick fletcher journals
    time.sleep(1)
    picking_journals(images_imbuer)  # pick imbuer journals
    time.sleep(1)
    picking_journals(images_blacksmith)  # pick blacksmith journals
    time.sleep(2)
    pyautogui.press("r")  # return to city
    time.sleep(20)


def put_items_to_chest() -> None:
    time.sleep(2)
    print("Drop items")
    click(1105, 636)  # click on resource's morgana chest
    time.sleep(2)
    click_drags(586, 385, 583, 579)  # scroll down chest inventory
    time.sleep(1)
    for (
        coords
    ) in inventory_coords:  # transfer items from character's inventory to chest's
        click_drags(*coords)
        time.sleep(0.5)
    click(425, 906)  # click stack
    time.sleep(0.1)
    click(539, 906)  # click sort
    time.sleep(15)
    pyautogui.press("r")
    time.sleep(20)


def travel_to_island() -> None:
    """
    Chose island from island_num context var
    :return: None
    """

    click(1607, 735)  # go to traveler
    time.sleep(2)
    click(328, 234)  # click on island
    time.sleep(0.5)
    move_cursor(306, 306)
    time.sleep(0.5)
    move_cursor(596, 439)
    time.sleep(1)
    click(613, 444)
    time.sleep(0.5)
    click(323, 234)
    pyautogui.press("right")
    for i in range(9):
        pyautogui.press("left")
    if island_num.get() < 10:
        pyautogui.press("backspace")
        pyautogui.press(f"{island_num.get()}")
    else:
        pyautogui.press("backspace")
        pyautogui.press("backspace")
        pyautogui.press(f"{str(island_num.get())[0]}")
        pyautogui.press(f"{str(island_num.get())[1]}")

    time.sleep(0.5)
    click(384, 948)
