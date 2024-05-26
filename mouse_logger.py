# mouse_logger.py
import logging
from pynput.mouse import Listener

class MouseLogger:
    def __init__(self, append_log):
        self.append_log = append_log

    def on_move(self, x, y):
        current_move = f"Mouse moved to {x} {y}"
        self.append_log(current_move)

    def on_click(self, x, y, button, pressed):
        current_click = f"Mouse {'pressed' if pressed else 'released'} at {x} {y}"
        self.append_log(current_click)

    def on_scroll(self, x, y, dx, dy):
        current_scroll = f"Mouse scrolled at {x} {y}"
        self.append_log(current_scroll)

    def run(self):
        with Listener(on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll) as mouse_listener:
            mouse_listener.join()
