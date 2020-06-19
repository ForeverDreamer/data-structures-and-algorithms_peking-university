"""打印机类"""


class Printer:
    def __init__(self, print_speed):
        self._print_speed = print_speed
        self._current_task = None
        self._time_remaining = 0

    def tick(self):
        if self._current_task is None:
            return
        self._time_remaining -= 1
        if self._time_remaining <= 0:
            self._current_task = None

    def busy(self):
        return False if self._current_task is None else True

    def start_next(self, new_task):
        self._current_task = new_task
        senconds_per_page = 60 / self._print_speed
        self._time_remaining = new_task.page_num * senconds_per_page
