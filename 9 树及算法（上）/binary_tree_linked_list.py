"""{4}--604树的链表实现6m57s"""


class BTNode:
    def __init__(self, key):
        self._key = key
        self._left = None
        self._right = None

    def insert_left(self, key):
        if self._left is None:
            self._left = BTNode(key)
        else:
            node = BTNode(key)
            node._left = self._left
            self._left = node

    def insert_right(self, key):
        if self._right is None:
            self._right = BTNode(key)
        else:
            node = BTNode(key)
            node._right = self._right
            self._right = node

    def preorder(self):
        print(self._key)
        if self._left:
            self._left.preorder()
        if self._right:
            self._right.preorder()

    def inorder(self):
        if self._left:
            self._left.inorder()
        print(self._key)
        if self._right:
            self._right.inorder()

    def postorder(self):
        if self._left:
            self._left.postorder()
        if self._right:
            self._right.postorder()
        print(self._key)

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, k):
        self._key = k


if __name__ == '__main__':
    r = BTNode('a')
    r.insert_left('b')
    r.insert_left('c')
    r.insert_left('d')
    r.insert_right('e')
    r.insert_right('f')
    r.right.key = 'hello'
    r.left.insert_right('g')
    r.preorder()
    print('-------------------------------')
    r.inorder()
    print('-------------------------------')
    r.postorder()

#       a
#      / \
#     d   hello
#    / \   \
#   c   g    e
#  /
# b
