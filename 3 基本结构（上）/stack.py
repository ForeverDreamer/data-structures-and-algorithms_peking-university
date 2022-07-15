"""{2}--302栈抽象数据类型及Python实现10m14s"""


class StackEnd:
    """栈顶尾端实现，时间复杂度为O(1)"""
    def __init__(self):
        self._items = []

    def __repr__(self):
        return str(self._items)

    def is_empty(self):
        return len(self._items) == 0

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def size(self):
        return len(self._items)


class StackFront:
    """栈顶首端实现，时间复杂度为O(n)"""
    def __init__(self):
        self._items = []

    def is_empty(self):
        return len(self._items) == 0

    def push(self, item):
        self._items.insert(0, item)

    def pop(self):
        return self._items.pop(0)

    def peek(self):
        return self._items[0]

    def size(self):
        return len(self._items)


def main():
    s = StackEnd()
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.is_empty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())


if __name__ == '__main__':
    main()
