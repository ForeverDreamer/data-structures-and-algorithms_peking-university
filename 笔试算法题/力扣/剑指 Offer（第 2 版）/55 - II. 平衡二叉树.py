"""
剑指 Offer 55 - II. 平衡二叉树

输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

 

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。

 

限制：

0 <= 树的结点个数 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 方法一：后序遍历 + 剪枝 （从底至顶）
# class Solution:
#     def isBalanced(self, root) -> bool:
#         def recur(root):
#             if not root:
#                 return 0
#             h_left = recur(root.left)
#             if h_left == -1:
#                 return -1
#             h_right = recur(root.right)
#             if h_right == -1:
#                 return -1
#             return max(h_left, h_right) + 1 if abs(h_left - h_right) <= 1 else -1
#
#         return recur(root) != -1


# 方法二：先序遍历 + 判断深度 （从顶至底）
class Solution:
    def isBalanced(self, root) -> bool:
        if not root: return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and \
            self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root: return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1
