"""
剑指 Offer 36. 二叉搜索树与双向链表
"""


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root):
        pre = None
        head = None

        def dfs(cur):
            nonlocal pre
            nonlocal head

            if not cur:
                return

            dfs(cur.left)  # 递归左子树
            if pre:  # 修改节点引用
                pre.right, cur.left = cur, pre
            else:  # 记录头节点
                head = cur
            pre = cur  # 更新pre
            dfs(cur.right)  # 递归右子树

        if not root:
            return

        dfs(root)
        head.left, pre.right = pre, head
        return head

