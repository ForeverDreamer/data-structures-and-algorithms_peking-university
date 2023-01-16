# Searching a key on a B-tree in Python
import random

# 视频著名代码出处，尊重别人劳动成果：https://www.programiz.com/dsa/b-tree


# Create a node
class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []


# Tree
class BTree:
    def __init__(self, order):
        self.root = BTreeNode(True)
        self.order = order

    def insert(self, k):
        root = self.root
        # 根节点满了，分裂节点，树的高度加1
        if len(root.keys) == self.order - 1:
            new_root = BTreeNode()
            self.root = new_root
            new_root.children.insert(0, root)
            self.split_children(new_root, 0)
            self.insert_non_full(new_root, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, node, k):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append((None, None))
            # 插入排序的算法，比新k大的都往后移动
            while i >= 0 and k[0] < node.keys[i][0]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            # 新k插入到合适的位置
            node.keys[i + 1] = k
        else:
            # 对当前节点的keys从右往左遍历查找新k合适的位置
            while i >= 0 and k[0] < node.keys[i][0]:
                i -= 1
            i += 1
            # 当前节点满了就先分裂当前节点
            if len(node.children[i].keys) == self.order - 1:
                self.split_children(node, i)
                if k[0] > node.keys[i][0]:
                    i += 1
            self.insert_non_full(node.children[i], k)

    # 以中间节点为中心把当前keys分为左中右三部分，中间部分即中间节点向上插入父节点，左右部分各自分裂成独立的左右节点
    def split_children(self, node, i):
        order = self.order
        mid = order // 2
        child = node.children[i]
        new_child = BTreeNode(child.leaf)
        node.children.insert(i+1, new_child)
        node.keys.insert(i, child.keys[mid-1])
        new_child.keys = child.keys[mid:order-1]
        child.keys = child.keys[0:mid-1]
        # 如果不是叶节点，还要把子节点分裂成左右两部分
        if not child.leaf:
            new_child.children = child.children[mid:order]
            child.children = child.children[0:mid]

    def print_tree(self, node, level=0):
        print("Level", level, end=": ")
        print([key[0] for key in node.keys])
        level += 1
        if len(node.children) > 0:
            for i in node.children:
                self.print_tree(i, level)

    def search_key(self, k, node=None):
        if node is not None:
            i = 0
            while i < len(node.keys) and k > node.keys[i][0]:
                i += 1
            if i < len(node.keys) and k == node.keys[i][0]:
                return node, i
            elif node.leaf:
                return None
            else:
                return self.search_key(k, node.children[i])
        else:
            return self.search_key(k, self.root)


def main():
    b_tree = BTree(4)
    # for i in range(10):
    #     B.insert((i, 2 * i))
    # keys = [1, 2, 5, 6, 7, 9, 12, 16, 17, 18, 19, 20, 21]
    # random.shuffle(keys)
    # key做为排序的依据必须是唯一的
    # keys = [18, 16, 7, 5, 6, 1, 12, 21, 2, 9, 17]
    keys = [21, 17, 19, 1, 20, 9, 16, 2, 6, 12, 18, 5, 7]
    for k in keys:
        b_tree.insert((k, 2 * k))

    b_tree.print_tree(b_tree.root)

    if b_tree.search_key(18) is not None:
        print("\nFound")
    else:
        print("\nNot Found")


if __name__ == '__main__':
    main()
