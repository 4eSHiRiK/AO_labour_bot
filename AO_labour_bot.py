import time
import PySimpleGUI as sg
import pyautogui

from const import island_num
from mouse_events.movement import (
    load_from_morgana_chest,
    travel_to_island,
    walk_to_labours,
    put_items_to_chest,
)


class LaborManagerGUI:
    """
    GUI for selecting islands
    """

    def __init__(self):
        self.fletcher_islands = self.create_checkbox_group("Fletcher", 1, 10)
        self.imbuer_islands = self.create_checkbox_group("Imbuer", 11, 20)
        self.blacksmith_islands = self.create_checkbox_group("BlackSmith", 21, 30)

        self.layout = self.create_layout()
        self.window = sg.Window("Labor Manager", self.layout)

    def create_checkbox_group(self, label, start, end) -> list[list]:
        return [
            [sg.Checkbox(f"{label} {i}", default=True, key=i)]
            for i in range(start, end + 1)
        ]

    def create_layout(self) -> list[list]:
        return [
            [sg.Text("Select Islands:")],
            [
                sg.Column(self.fletcher_islands),
                sg.Column(self.imbuer_islands),
                sg.Column(self.blacksmith_islands),
            ],
            [sg.Button("Start"), sg.Button("Exit")],
        ]

    def run(self) -> None:
        while True:
            event, values = self.window.read()
            if event in (sg.WIN_CLOSED, "Exit"):
                break
            self.handle_event(event, values)

        self.window.close()

    def handle_event(self, event, values) -> None:
        if event == "Start":
            self.start_processing(values)
        self.window.close()

    def start_processing(self, values) -> None:
        island_counter = 1  # for put collected resources into resource chest
        cur_island = 0  # Base island
        island_num.set(cur_island)
        time.sleep(3)
        travel_to_island()
        time.sleep(7)
        load_from_morgana_chest()

        selected_islands = [key for key, value in values.items() if value]

        for island in selected_islands:
            cur_island = island
            if island_counter % 11 == 0:
                island_num.set(0)
                travel_to_island()
                time.sleep(5)
                put_items_to_chest()
                island_counter = 1
            island_num.set(cur_island)
            travel_to_island()
            time.sleep(5)
            walk_to_labours()
            island_counter += 1

        cur_island = 0  # Base island
        island_num.set(cur_island)
        time.sleep(3)
        travel_to_island()


if __name__ == "__main__":
    pyautogui.FAILSAFE = False
    start_time = time.time()

    gui = LaborManagerGUI()
    gui.run()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Время выполнения: {elapsed_time:.2f} секунд")
