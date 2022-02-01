"""
剑指 Offer 16. 数值的整数次方

实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。不得使用库函数，同时不需要考虑大数问题。

 

示例 1：

输入：x = 2.00000, n = 10
输出：1024.00000
示例 2：

输入：x = 2.10000, n = 3
输出：9.26100
示例 3：

输入：x = 2.00000, n = -2
输出：0.25000
解释：2-2 = 1/22 = 1/4 = 0.25
 

提示：

-100.0 < x < 100.0
-2^31 <= n <= 2^31-1
-10^4 <= xn <= 10^4
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 提交会超时
        # res = 1
        # if n < 0:
        #     base = 1/x
        #     n = -n
        # else:
        #     base = x
        # for _ in (range(n)):
        #     res *= base
        # return res

        return x**n


print(Solution().myPow(2.00000, 10))
print(Solution().myPow(2.00000, -2))
