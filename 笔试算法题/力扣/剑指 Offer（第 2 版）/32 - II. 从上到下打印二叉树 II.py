"""
剑指 Offer 32 - II. 从上到下打印二叉树 II

从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
 

提示：
节点总数 <= 1000

Python 中使用 collections 中的双端队列 deque() ，其 popleft() 方法可达到 O(1)O(1) 时间复杂度；列表 list 的 pop(0) 方法时间复杂度为 O(N)O(N) 。
"""

import collections

from utils import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        return res
