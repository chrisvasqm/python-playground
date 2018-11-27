# Design a class that represents a stopwatch.
# The consumer of this class should be able to
# start, stop and get the time passed in between each call to
# start and stop.
# Remember to prevent the user to start the stopwatch twice.

import time


def main():
    stopwatch = Stopwatch()
    stopwatch.start()
    
    # Wait for 3 seconds to pass
    time.sleep(3)

    stopwatch.stop()
    print(stopwatch.counter)


class Stopwatch(object):

    def __init__(self):
        self.is_running = False
        self._counter = time.time()

    @property
    def counter(self):
        return self._counter

    def start(self):
        if self.is_running == True:
            raise AlreadyStartedException()
        else:
            self._counter = time.time()
            self.is_running = True

    def stop(self):
        self._counter = time.time() - self._counter
        self.is_running = False


class AlreadyStartedException(Exception):
    def __init__(self):
        super().__init__("Stopwatch is already started.")


if __name__ == "__main__":
    main()
