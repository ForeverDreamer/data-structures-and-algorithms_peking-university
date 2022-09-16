"""
剑指 Offer 33. 二叉搜索树的后序遍历序列

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3

示例 1：
输入: [1,6,3,2,5]
输出: false

示例 2：
输入: [1,3,2,6,5]
输出: true

提示：
数组长度 <= 1000
"""


class Solution:
    def verifyPostorder(self, postorder: [int]) -> bool:
        def _verify(start, root):
            if start >= root:
                return True
            i = start
            # 跳过左子树
            while postorder[i] < postorder[root]:
                i += 1
            left_root = i - 1
            # 跳过右子树
            while postorder[i] > postorder[root]:
                i += 1
            # 判断最后剩下的是不是根节点，递归验证左子树和右子树
            return i == root and _verify(start, left_root) and _verify(left_root+1, root-1)

        return _verify(0, len(postorder) - 1)


print(Solution().verifyPostorder([1, 3, 2, 6, 5]))
