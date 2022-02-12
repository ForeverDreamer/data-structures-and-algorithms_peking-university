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

input_seq = [3, 5, 7, -1, -1, 2, 4]


class BinTree:
    def __init__(self, data):
        self.data = [0] + data
        self.min_num = min([n for n in self.data if n > 0])

    def dsf(self, i, out):
        if self.data[i] == -1:
            return False
        out.append(self.data[i])
        level = 1
        i = 1
        if self.data[i * 2] == -1 and self.data[i * 2 + 1] == -1:
            if out[-1] != self.min_num:
                return False
            return True
        if self.data[i * 2] == -1:
            out.append(self.data[i * 2 + 1])
            done = self.dsf(i*2+2, out)
        if self.data[i * 2 + 1] == -1:
            out.append(self.data[i * 2])
            done = self.dsf(i*2+2, out)
        if self.data[i * 2] < self.data[i * 2 + 1]:
            out.append(self.data[i * 2])
            done = self.dsf(i*2+2, out)
        else:
            out.append(self.data[i * 2 + 1])
            done = self.dsf(i*2+2, out)
        if done:
            return True
        else:
            out.pop()
            done = self.dsf(i // 2, out)
        # while i*2+1 <= len(self.data):
        #     if self.data[i*2] == -1 and self.data[i*2+1] == -1:
        #         break
        #     if self.data[i*2] == -1:
        #         data.append(self.data[i*2+1])
        #         break
        #     if self.data[i*2+1] == -1:
        #         data.append(self.data[i*2])
        #         break
        #     if self.data[i*2] < self.data[i*2+1]:
        #         data.append(self.data[i*2])
        #     else:
        #         data.append(self.data[i*2+1])
        #     level += 1
        #     i = i*2+1



out_put = []
BinTree(input_seq).dsf(1, out_put)
print(' '.join([str(n) for n in out_put]))
