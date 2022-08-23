"""
剑指 Offer 34. 二叉树中和为某一值的路径

给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
叶子节点 是指没有子节点的节点。

示例 1：
输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：[[5,4,11,2],[5,8,4,5]]

示例 2：
输入：root = [1,2,3], targetSum = 5
输出：[]

示例 3：
输入：root = [1,2], targetSum = 0
输出：[]
 
提示：

树中节点总数在范围 [0, 5000] 内
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""
from utils import TreeNode, Tree

class Solution:
    def pathSum(self, root: TreeNode, target: int):
        res, path = [], []
        def recur(root, tar):
            if not root:
                return
            tar -= root.val
            if tar < 0:
                return
            if tar == 0:
                if not root.left and not root.right:
                    path.append(root.val)
                    res.append(list(path))
                    path.pop()
                return
            path.append(root.val)
            recur(root.left, tar)
            recur(root.right, tar)
            path.pop()

        recur(root, target)
        return res


# 需要调一下，Tree实现有问题
print(Solution().pathSum(Tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]).root, 22))
