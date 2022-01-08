class Node:
    def __init__(self, key, data, left=None, right=None, parent=None):
        self._key = key
        self._data = data
        self._left = left
        self._right = right
        self._parent = parent

    def __iter__(self):
        if self.has_left():
            for key, data in self.left:
                yield key, data
        yield self.key, self.data
        if self.has_right():
            for key, data in self.right:
                yield key, data

    @property
    def key(self):
        return self._key

    @property
    def data(self):
        return self._data

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        self._parent = node

    def has_left(self):
        return self._left

    def has_only_left(self):
        return self._left and not self._right

    def has_right(self):
        return self._right

    def has_only_right(self):
        return not self._left and self._right

    def is_left(self):
        return self._parent and self._parent._left == self

    def is_right(self):
        return self._parent and self._parent._right == self

    def is_root(self):
        return not self._parent

    def is_leaf(self):
        return not (self._left or self._right)

    def has_child(self):
        return self._left or self._right

    def has_both_children(self):
        return self._left and self._right

    def update_node(self, key, data, left, right):
        self._key = key
        self._data = data
        self._left = left
        self._right = right
        if left:
            left.parent = self
        if right:
            right.parent = self


class BinarySearchTree:
    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        if self._root:
            return iter(self._root)
            # return self._root.__iter__()

    def __setitem__(self, key, data):
        self.put(key, data)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return True if self.get(key) else False

    def __delitem__(self, key):
        self.delete(key)

    @property
    def size(self):
        return self._size

    def _put(self, key, data, current):
        if key < current.key:
            if current.has_left():
                self._put(key, data, current.left)
            else:
                current.left = Node(key, data, parent=current)
        else:
            if current.has_right():
                self._put(key, data, current.right)
            else:
                current.right = Node(key, data, parent=current)

    def put(self, key, data):
        if self._root:
            self._put(key, data, self._root)
        else:
            self._root = Node(key, data)
        self._size += 1

    def _get(self, key, current):
        if not current:
            return None
        elif current.key == key:
            return current
        elif key < current.key:
            return self._get(key, current.left)
        else:
            return self._get(key, current.right)

    def get(self, key):
        if self._root:
            node = self._get(key, self._root)
            return node.data if node else None
        else:
            return None

    def remove(self, node):
        # 这个节点没有子节点
        if node.is_leaf():
            if node.is_left:
                node.parent.left = None
            else:
                node.parent.right = None
        # 这个节点有1个子节点
        # 这个节点有2个子节点

    def delete(self, key):
        if self.size == 0:
            raise KeyError('数据不存在')
        if self.size == 1:
            if self._root.key == key:
                self._root = None
                self._size -= 1
                return
            else:
                raise KeyError('数据不存在')
        node = self.get(key)
        if node:
            self.remove(node)
            self._size -= 1
        else:
            raise KeyError('数据不存在')


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst[3] = 'red'
    bst[4] = 'blue'
    bst[6] = 'yellow'
    bst[2] = 'white'
    print(3 in bst)
    print(5 in bst)
    print(bst[6])
    # del bst[6]
    print(bst[3])
    for k, d in bst:
        print(k, d)
