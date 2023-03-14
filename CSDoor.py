
from utils.ColorsUtils import Colors
import keyboard
import time

DEFAULT_EXIT_KEY = 'q'
PRESS_DELAY = 0.017


def showMainMessage():
    print(f"""========================================================
Author: https://github.com/Robbna
Github repository: https://github.com/Robbna/CSDoor

{Colors.changeColor(f"Press '{DEFAULT_EXIT_KEY}' to exit!", Colors.WARNING)}
========================================================
""")

def handler_exit():
    print("""Exiting the application...""")
    time.sleep(3)

def handle_empty_values():
    print(f"""
{Colors.changeColor("[ERROR]", Colors.FAIL)}
    {Colors.changeColor(f"Both steps are required!", Colors.WARNING)}
""")


def handle_not_valid_key(key):
    print(f"""
{Colors.changeColor("[ERROR]", Colors.FAIL)}
    {Colors.changeColor(f"'{key}' is not a valid key!", Colors.WARNING)}
""")


def operDoor(shotcut):
    keyboard.press_and_release(shotcut)


if __name__ == "__main__":

    showMainMessage()

    shortcut = input(f"""{Colors.changeColor('Step #1', Colors.OKGREEN)}
Shortcut to automatically open the door (e.g. = u):
{Colors.changeColor('>', Colors.BOLD)} """)

    key_to_open = input(f"""
{Colors.changeColor('Step #2', Colors.OKGREEN)}
Key set in game to open door (e.g. = e):
{Colors.changeColor('>', Colors.BOLD)} """)

    if shortcut and key_to_open:
        try:
            if len(key_to_open) > 1:
                raise Exception
            print("""
RUNNING!
""")
            while not keyboard.is_pressed(DEFAULT_EXIT_KEY):
                if keyboard.is_pressed(shortcut):
                    operDoor(key_to_open)
                time.sleep(PRESS_DELAY)
        except Exception:
            if len(shortcut) > 1:
                handle_not_valid_key(shortcut)
            if len(key_to_open) > 1:
                handle_not_valid_key(key_to_open)

    else:
        handle_empty_values()
    
    handler_exit()