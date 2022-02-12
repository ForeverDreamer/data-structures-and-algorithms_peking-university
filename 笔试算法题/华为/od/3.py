"""
用列表实现的二叉树, 下标为N的节点，其左子节点为2*N，其右子节点为2*N+1,
空节点用-1表示，输出从根节点到最小叶节点的路径，保证最小叶节点唯一。

输入: 3 5 7 -1 -1 2 4

       3
     /   \
    5     7
         / \
        2   4

输出: 3 7 2
"""

# input_seq = [3, 5, 7, -1, -1, 2, 4]
# input_seq = [3, 5, 7, 1, -1, 2, 4]
# input_seq = [3, 5, 7, -1, -1, 2, 1]
input_seq = [4, 5, 7, 8, 9, 6, 3, 1, -1]


class BinTree:
    def __init__(self, data):
        self.data = [0] + data
        self.min_num = min([n for n in self.data if n > 0])

    def dsf(self, i, out):
        if self.data[i] == -1:
            return False
        out.append(self.data[i])
        if i*2+1 > len(self.data)-1:
            if out[-1] != self.min_num:
                out.pop()
                return False
            return True
        for j in (i * 2, i * 2 + 1):
            if self.dsf(j, out):
                return True
        out.pop()
        return False


out_put = []
BinTree(input_seq).dsf(1, out_put)
print(' '.join([str(n) for n in out_put]))
