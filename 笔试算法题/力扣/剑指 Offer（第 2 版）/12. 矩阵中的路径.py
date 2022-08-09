"""
剑指 Offer 12. 矩阵中的路径

复杂度分析：
M,N 分别为矩阵行列大小， K 为字符串 word 长度。

时间复杂度 O(3^KMN)： 最差情况下，需要遍历矩阵中长度为 K 字符串的所有方案，时间复杂度为 O(3^K)；矩阵中共有 MN 个起点，时间复杂度为 O(MN) 。
方案数计算： 设字符串长度为 K ，搜索中每个字符有上、下、左、右四个方向可以选择，舍弃回头（上个字符）的方向，剩下 3 种选择，因此方案数的复杂度为 O(3^K)。
空间复杂度 O(K) ： 搜索过程中的递归深度不超过 KK ，因此系统因函数调用累计使用的栈空间占用 O(K) （因为函数返回后，系统调用的栈空间会释放）。最坏情况下 K = MN(word的长度为MN)，递归深度为 MN，此时系统栈使用 O(MN) 的额外空间。
"""


class Solution:
    def exist(self, board, word: str) -> bool:
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]: return False
            if k == len(word) - 1: return True
            board[i][j] = ''
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = word[k]
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True
        return False


class SolutionTrace:

    def __init__(self):
        self._fail_count = 0
        self._max_k = 0
        self._path = []

    def exist(self, board, word: str) -> bool:

        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]):
                return False
            if board[i][j] != '':
                self._path.append((board[i][j], k))
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            board[i][j] = ''
            self._max_k += 1
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = word[k]
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    self.trace(i, j)
                    return True
                self._fail_count += 1
                self.trace(i, j)

        return False

    def trace(self, i, j):
        print(f'第{self._fail_count}次尝试, i={i}, j={j}, max_k, {self._max_k}: ')
        print(self._path)
        self._path.clear()


# print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "CCABED"))
# print(SolutionTrace().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
# print(SolutionTrace().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCEDZ"))
