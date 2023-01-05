# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class List:
    def __init__(self, values):
        self.head = ListNode(values[0])
        cur = self.head
        for v in values[1:]:
            cur.next = ListNode(v)
            cur = cur.next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.key)


class Tree:
    def __init__(self, nums):
        start, end = 0, 1
        level_nums = []
        while end <= len(nums):
            curs = nums[start:end]
            level_nums.append(curs)
            curs_not_null = [n for n in curs if n]
            start += len(curs)
            end += len(curs_not_null)*2

        i = 1
        parents = [TreeNode(n) for n in level_nums[0]]
        while i < len(level_nums) and parents:
            children = [TreeNode(n) if n else None for n in level_nums[i]]
            j = 0
            tmp_parents = []
            for parent in parents:
                if i == 1:
                    self._root = parent
                parent.left = children[j]
                parent.right = children[j+1]
                if parent.left:
                    tmp_parents.append(parent.left)
                if parent.right:
                    tmp_parents.append(parent.right)
                j += 2
            parents = tmp_parents
            i += 1

    @property
    def root(self):
        return self._root
