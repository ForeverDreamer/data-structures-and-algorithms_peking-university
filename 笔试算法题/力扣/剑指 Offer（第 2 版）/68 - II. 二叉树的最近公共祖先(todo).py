"""
剑指 Offer 68 - II. 二叉树的最近公共祖先

复杂度分析：
时间复杂度 O(N)O(N) ： 其中 NN 为二叉树节点数；最差情况下，需要递归遍历树的所有节点。
空间复杂度 O(N)O(N) ： 最差情况下，递归深度达到 NN ，系统使用 O(N)O(N) 大小的额外空间。

作者：jyd
链接：https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/solution/mian-shi-ti-68-ii-er-cha-shu-de-zui-jin-gong-gon-7/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

from utils import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left: return right
        if not right: return left
        return root
