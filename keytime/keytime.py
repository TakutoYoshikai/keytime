import pyxhook
import time
import sys

class KeyTimeLogger:
    def __init__(self, max_sec):
        self.__recorded_time = 0
        self.__date = None
        self.__max_sec = max_sec
        self.__hookman = pyxhook.HookManager()
        self.__hookman.KeyDown = self.key_event
        self.__hookman.HookKeyboard()
    def start(self):
        self.__recorded_time = 0
        self.__hookman.start()
    def stop(self):
        self.__hookman.cancel()
        return self.__recorded_time
    def key_event(self, event):
        now = time.time()
        if self.__date is None:
            self.__date = now
            return
        diff = now - self.__date
        if diff <= self.__max_sec:
            self.__recorded_time = self.__recorded_time + diff
        self.__date = now

def main():
    logger = KeyTimeLogger(3)
    logger.start()
    sec = int(sys.argv[1])
    time.sleep(sec)
    print(logger.stop())

if __name__ == "__main__":
    main()
