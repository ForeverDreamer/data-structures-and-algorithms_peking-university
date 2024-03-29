"""打印机类"""


class Printer:
    def __init__(self, print_speed):
        self._senconds_per_page = 60 / print_speed
        self._current_task = None
        self._time_remaining = 0

    def tick(self):
        if self._current_task is None:
            return
        self._time_remaining -= 1
        if self._time_remaining <= 0:
            self._current_task = None

    def busy(self):
        return True if self._current_task else False

    def start_next(self, new_task):
        self._current_task = new_task
        self._time_remaining = new_task.page_num * self._senconds_per_page
