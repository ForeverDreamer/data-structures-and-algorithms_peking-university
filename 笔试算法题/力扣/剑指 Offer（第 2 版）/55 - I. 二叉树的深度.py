"""
剑指 Offer 55 - I. 二叉树的深度

输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

提示：
节点总数 <= 10000
"""

from utils import TreeDeserialize


class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# class Solution:
#     def maxDepth(self, root) -> int:
#         if not root:
#             return 0
#         queue, res = [root], 0
#         while queue:
#             tmp = []
#             for node in queue:
#                 if node.left:
#                     tmp.append(node.left)
#                 if node.right:
#                     tmp.append(node.right)
#             queue = tmp
#             res += 1
#         return res


print(Solution().maxDepth(TreeDeserialize('[3,9,20,null,null,15,7,null,null,null,null]').root))