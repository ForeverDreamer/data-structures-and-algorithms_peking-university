"""
剑指 Offer 32 - III. 从上到下打印二叉树 III

请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

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
  [20,9],
  [15,7]
]
 
提示：
节点总数 <= 1000
"""

import collections

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        res, deque = [], collections.deque([root])
        while deque:
            tmp = collections.deque()
            length = len(deque)
            for _ in range(length):
                node = deque.popleft()
                if len(res) % 2:
                    tmp.appendleft(node.val)  # 偶数层 -> 队列头部
                else:
                    tmp.append(node.val)  # 奇数层 -> 队列尾部
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            res.append(list(tmp))
        return res
