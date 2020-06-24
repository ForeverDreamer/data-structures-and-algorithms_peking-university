"""
{6}--313无序表抽象数据类型及Python实现11m03s
{7}--314无序表的链表实现12m54s
"""


class Node:

    def __init__(self, d):
        self._data = d
        self._next = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, d):
        self._data = d

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, n):
        self._next = n


class UnorderedList:

    def __init__(self):
        self._head = None

    def empty(self):
        return self._head is None

    def add_node(self, data):
        new_node = Node(data)
        new_node.next = self._head
        self._head = new_node

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.next

        return count

    def search(self, data):
        current = self._head
        found = False
        while current is not None and not found:
            if current.data == data:
                found = True
            else:
                current = current.next

        return found

    def remove(self, data):
        current = self._head
        previous = None
        found = False
        while not found and current is not None:
            if current.data == data:
                found = True
            else:
                previous = current
                current = current.next
        if not found:
            raise ValueError('数据不存在！')

        if previous is None:
            self._head = current.next
        else:
            previous.next = current.next


class OrderedList:

    def __init__(self):
        self._head = None

    def add(self, data):
        current = self._head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.data > data:
                stop = True
            else:
                previous = current
                current = current.next

        new_node = Node(data)
        if previous is None:
            new_node.next = self._head
            self._head = new_node
        else:
            new_node.next = current
            previous.next = new_node

    def search(self, data):
        current = self._head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.data == data:
                found = True
            else:
                if current.data > data:
                    stop = True
                else:
                    current = current.next

        return found
