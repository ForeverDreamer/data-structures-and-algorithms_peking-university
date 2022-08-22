# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class List:
    def __init__(self, values):
        self.head = ListNode(values[0])
        curr_node = self.head
        for v in values[1:]:
            curr_node.next = ListNode(v)
            curr_node = curr_node.next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


class Tree:
    def __init__(self, nums):
        # self._root = TreeNode(nums[0])
        # parents = [self._root]
        # i = 1
        # cur_data_length = 2
        # while i+cur_data_length <= len(nums):
        #     cur_data = nums[i:i+cur_data_length]
        #     j = 0
        #     while j < len(cur_data) and parents:
        #         p = parents.pop(0)
        #         p.left = TreeNode(cur_data[j])
        #         p.right = TreeNode(cur_data[j+1])
        #         parents.append(p.left)
        #         parents.append(p.right)
        #         j += 2
        #     i += cur_data_length
        #     cur_data_length *= 2
        start, end = 0, 1
        level_nums = []
        while end <= len(nums):
            curs = nums[start:end]
            level_nums.append(curs)
            curs_not_null = [n for n in curs if n]
            start += len(curs)
            end += len(curs_not_null)*2

        i = 0
        parents = [TreeNode(n) for n in level_nums[i]]
        while i+1 < len(level_nums):
            children = [TreeNode(n) if n else None for n in level_nums[i+1]]
            j = 0
            for parent in parents:
                if i == 0:
                    self._root = parent
                parent.left = children[j]
                parent.right = children[j+1]
                if parent.left:
                    parents.append(parent.left)
                if parent.left:
                    parents.append(parent.right)
                parents.pop(0)
                j += 2
            i += 1

    @property
    def root(self):
        return self._root
