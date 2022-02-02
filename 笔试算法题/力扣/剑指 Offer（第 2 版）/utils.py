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


class Tree:
    def __init__(self):
        pass