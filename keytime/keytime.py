import pyxhook
import time
import sys

class KeyTimeLogger:
    def __init__(self, max_sec):
        self.recorded_time = 0
        self.date = time.time()
        self.max_sec = max_sec
        self.hookman = pyxhook.HookManager()
        self.hookman.KeyDown = self.key_event
        self.hookman.HookKeyboard()
    def start(self):
        self.hookman.start()
    def stop(self):
        self.hookman.cancel()
        return self.recorded_time
    def key_event(self, event):
        now = time.time()
        diff = now - self.date
        if diff <= self.max_sec:
            self.recorded_time = self.recorded_time + diff
        self.date = now

def main():
    logger = KeyTimeLogger(3)
    logger.start()
    sec = int(sys.argv[1])
    time.sleep(sec)
    print(logger.stop())

if __name__ == "__main__":
    main()
