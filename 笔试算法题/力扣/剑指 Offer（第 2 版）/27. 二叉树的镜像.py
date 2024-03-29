"""
剑指 Offer 27. 二叉树的镜像

请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
镜像输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

示例 1：
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]

限制：
0 <= 节点个数 <= 1000
"""

from utils import TreeNode, Tree


# 方法一：递归法
# class Solution:
#     def mirrorTree(self, root: TreeNode):
#         if root is None:
#             return None
#         # 先递归交换右子树，再递归交换左子树，最后交换左右子树，交换顺序自下而上：9,6,7,3,1,2,4
#         root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
#         return root


# 方法二：辅助栈（或队列）
class Solution:
    def mirrorTree(self, root: TreeNode):
        if not root:
            return
        stack = [root]
        while stack:
            # 先交换根节点，再交换右节点，最后交换左节点，交换顺序自上而下：4,7,9,6,2,3,1
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            node.left, node.right = node.right, node.left
        return root


print(Solution().mirrorTree(Tree([4, 2, 7, 1, 3, 6, 9]).root))
