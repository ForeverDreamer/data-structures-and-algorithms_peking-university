"""{4}--604树的链表实现6m57s"""


class BinaryTree:
    def __init__(self, data):
        self._data = data
        self._left_child = None
        self._right_child = None

    def insert_left(self, data):
        if self._left_child is None:
            self._left_child = BinaryTree(data)
        else:
            t = BinaryTree(data)
            t._left_child = self._left_child
            self._left_child = t

    def insert_right(self, data):
        if self._right_child is None:
            self._right_child = BinaryTree(data)
        else:
            t = BinaryTree(data)
            t._right_child = self._right_child
            self._right_child = t

    def preorder(self):
        print(self._data)
        if self._left_child:
            self._left_child.preorder()
        if self._right_child:
            self._right_child.preorder()

    @property
    def left_child(self):
        return self._left_child

    @property
    def right_child(self):
        return self._right_child

    @property
    def root_data(self):
        return self._data

    @root_data.setter
    def root_data(self, data):
        self._data = data


if __name__ == '__main__':
    r = BinaryTree('a')
    r.insert_left('b')
    r.insert_right('c')
    r.right_child.root_data = 'hello'
    r.left_child.insert_right('d')
    print(r)
