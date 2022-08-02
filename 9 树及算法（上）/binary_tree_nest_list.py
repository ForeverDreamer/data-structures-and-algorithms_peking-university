"""{3}--603树的嵌套列表实现11m00s"""


class BTNestTree:
    def __init__(self, key):
        self._root = [key, [], []]

    def __repr__(self):
        return str(self._root)

    def insert_left(self, key):
        left = self._root.pop(1)
        if len(left) > 1:
            self._root.insert(1, [key, left, []])
        else:
            self._root.insert(1, [key, [], []])
        return self._root

    def insert_right(self, key):
        right = self._root.pop(2)
        if len(right) > 1:
            self._root.insert(2, [key, [], right])
        else:
            self._root.insert(2, [key, [], []])
        return self._root

    @property
    def root(self):
        return self._root

    @property
    def left_subtree(self):
        return self._root[1]

    @property
    def right_subtree(self):
        return self._root[2]


if __name__ == '__main__':
    tree = BTNestTree(3)
    tree.insert_left(4)
    tree.insert_left(5)
    tree.insert_right(6)
    tree.insert_right(7)
    print('root:', tree.root)
    print('left_subtree:', tree.left_subtree)
    print('right_subtree:', tree.right_subtree)

