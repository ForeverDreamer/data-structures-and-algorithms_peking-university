"""打印任务类"""
import random


class Task:
    page_num_limit = 20

    def __init__(self, submit_time):
        self._submit_time = submit_time
        self._page_num = random.randrange(1, Task.page_num_limit + 1)

    @property
    def submit_time(self):
        return self._submit_time

    @property
    def page_num(self):
        return self._page_num

    def wait_time(self, now):
        return now - self._submit_time

    @staticmethod
    def new_task():
        senconds_per_task = 180
        # 不一定非要等于senconds_per_task, 1~180之间的任意一个数都可以，概率是一样的
        return True if random.randrange(1, senconds_per_task + 1) == senconds_per_task else False
