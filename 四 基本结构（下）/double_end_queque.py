"""{5}--312双端队列抽象数据类型及Python实现+回文词判定7m25"""


class DoubleEndQueue:

    def __init__(self):
        self._items = []

    def empty(self):
        return len(self._items) == 0

    def add_front(self, item):
        self._items.append(item)

    def remove_front(self):
        return self._items.pop()

    def add_rear(self, item):
        self._items.insert(0, item)

    def remove_rear(self):
        return self._items.pop(0)

    def size(self):
        return len(self._items)


def palindrome(string):
    de_queue = DoubleEndQueue()

    for char in string:
        de_queue.add_front(char)

    equal = True
    while de_queue.size() > 1 and equal:
        front = de_queue.remove_front()
        rear = de_queue.remove_rear()
        if front != rear:
            equal = False

    return equal


if __name__ == '__main__':
    print(palindrome('lsdkjfskf'))
    print(palindrome('radar'))
