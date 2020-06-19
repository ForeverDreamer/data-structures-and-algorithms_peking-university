"""{1}--308队列抽象数据类型及Python实现10m01s"""


class Queue:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return len(self._items) == 0

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)
