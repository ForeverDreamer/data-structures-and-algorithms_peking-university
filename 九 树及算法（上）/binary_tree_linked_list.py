"""{4}--604树的链表实现6m57s"""


class BTNode:
    def __init__(self, v):
        self._data = v
        self._left = None
        self._right = None

    def insert_left(self, v):
        if self._left is None:
            self._left = BTNode(v)
        else:
            t = BTNode(v)
            t._left = self._left
            self._left = t

    def insert_right(self, v):
        if self._right is None:
            self._right = BTNode(v)
        else:
            t = BTNode(v)
            t._right = self._right
            self._right = t

    def preorder(self):
        print(self._data)
        if self._left:
            self._left.preorder()
        if self._right:
            self._right.preorder()

    def inorder(self):
        if self._left:
            self._left.preorder()
        print(self._data)
        if self._right:
            self._right.preorder()

    def postorder(self):
        if self._left:
            self._left.preorder()
        if self._right:
            self._right.preorder()
        print(self._data)

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, v):
        self._data = v


if __name__ == '__main__':
    r = BTNode('a')
    r.insert_left('b')
    r.insert_left('c')
    r.insert_left('d')
    r.insert_right('e')
    r.insert_right('f')
    r.right.data = 'hello'
    r.left.insert_right('g')
    r.preorder()
    print('-------------------------------')
    r.inorder()
    print('-------------------------------')
    r.postorder()
