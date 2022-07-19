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

    def __str__(self):
        current = self._head
        datas = []
        while current:
            datas.append(current.data)
            current = current.next

        return f'UnorderedList: {datas}'

    @property
    def head(self):
        return self._head

    def empty(self):
        return self._head is None

    def add_to_tail(self, new_node):
        if self._head is None:
            self._head = new_node
        else:
            previous = None
            current = self._head
            while current:
                previous = current
                current = current.next
            previous.next = new_node
        return self._head

    def add(self, new_node):
        new_node.next = self._head
        self._head = new_node

    def size(self):
        current = self._head
        count = 0
        while current:
            count += 1
            current = current.next

        return count

    def search(self, data):
        current = self._head
        found = False
        while current:
            if current.data == data:
                found = True
                break
            else:
                current = current.next

        return found

    def remove(self, data):
        if self._head is None:
            raise ValueError('数据不存在！')
        previous = None
        current = self._head
        found = False
        while current:
            if current.data == data:
                if previous is None:
                    self._head = current.next
                else:
                    previous.next = current.next
                found = True
                break
            else:
                previous = current
                current = current.next
        if not found:
            raise ValueError('数据不存在！')


class OrderedList:

    def __init__(self):
        self._head = None

    def __str__(self):
        current = self._head
        datas = []
        while current:
            datas.append(current.data)
            current = current.next

        return f'OrderedList: {datas}'

    @property
    def head(self):
        return self._head

    def add(self, new_node):
        if self._head is None:
            new_node.next = self._head
            self._head = new_node
        else:
            previous = None
            current = self._head
            while current:
                if current.data >= new_node.data:
                    break
                else:
                    previous = current
                    current = current.next
            if previous is None:
                new_node.next = self._head
                self._head = new_node
            else:
                new_node.next = current
                previous.next = new_node

    def search(self, data):
        if self._head is None:
            return False
        current = self._head
        found = False
        while current:
            if current.data == data:
                found = True
                break
            else:
                if current.data > data:
                    break
                else:
                    current = current.next

        return found


def main_ul():
    ul = UnorderedList()
    ul.add(Node(1))
    print(ul)
    ul.add(Node(2))
    print(ul)
    ul.add(Node(3))
    print(ul)
    ul.add_to_tail(Node(4))
    print(ul)
    ul.add_to_tail(Node(5))
    print(ul)
    ul.add_to_tail(Node(6))
    print(ul)
    ul.remove(3)
    print(ul)
    ul.remove(1)
    print(ul)
    ul.remove(5)
    print(ul)

    try:
        ul.remove(7)
    except ValueError as e:
        print(e)

    try:
        UnorderedList().remove(1)
    except ValueError as e:
        print(e)


def main_ol():
    ol = OrderedList()
    ol.add(Node(4))
    print(ol)
    ol.add(Node(5))
    print(ol)
    ol.add(Node(6))
    print(ol)
    ol.add(Node(1))
    print(ol)
    ol.add(Node(2))
    print(ol)
    ol.add(Node(3))
    print(ol)


if __name__ == '__main__':
    # main_ul()
    main_ol()
