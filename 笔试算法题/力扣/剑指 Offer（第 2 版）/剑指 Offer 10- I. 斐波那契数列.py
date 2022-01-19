"""
剑指 Offer 10- I. 斐波那契数列

写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：
输入：n = 2
输出：1

示例 2：
输入：n = 5
输出：5

提示：
0 <= n <= 100

方法一：动态规划
斐波那契数的边界条件是 F(0)=0F(0)=0 和 F(1)=1F(1)=1。当 n>1n>1 时，每一项的和都等于前两项的和，因此有如下递推关系：

F(n)=F(n-1)+F(n-2)
F(n)=F(n−1)+F(n−2)

由于斐波那契数存在递推关系，因此可以使用动态规划求解。动态规划的状态转移方程即为上述递推关系，边界条件为 F(0)F(0) 和 F(1)F(1)。

根据状态转移方程和边界条件，可以得到时间复杂度和空间复杂度都是 O(n)O(n) 的实现。由于 F(n)F(n) 只和 F(n-1)F(n−1) 与 F(n-2)F(n−2) 有关，因此可以使用「滚动数组思想」把空间复杂度优化成 O(1)O(1)。如下的代码中给出的就是这种实现。

计算过程中，答案需要取模 1e9+7。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/solution/fei-bo-na-qi-shu-lie-by-leetcode-solutio-hbss/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution:
    # def fib(self, n: int) -> int:
    #     if n < 2:
    #         return n
    #     return (self.fib(n - 2) + self.fib(n - 1)) % 1000000007

    def fib(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        if n < 2:
            return n
        p, q, r = 0, 0, 1
        for i in range(2, n + 1):
            p = q
            q = r
            r = (p + q) % MOD
        return r


s = Solution()
print(s.fib(37))