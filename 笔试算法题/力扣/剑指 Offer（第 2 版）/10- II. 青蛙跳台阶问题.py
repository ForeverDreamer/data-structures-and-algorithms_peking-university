"""
剑指 Offer 10- II. 青蛙跳台阶问题

一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：2
示例 2：

输入：n = 7
输出：21
示例 3：

输入：n = 0
输出：1

问题分析：
青蛙的最后一步只有两种跳法： 跳上1级或2级台阶，不管是哪种跳法，各自都定了只有这一种跳法，总的跳法只是由到达起跳位置的跳法数量决定，至此一步步往前推算；
如果最后跳了1级台阶，即最后一步的起跳位置就是n-1：需要计算到达此台阶有多少种跳法即f(n-1)；
如果最后跳了2级台阶，即最后一步的起跳位置就是n-2：同样需要计算到达此台阶有多少种跳法即f(n-2)；
两种情况之和就是总的跳法，即f(n) = f(n-1) + f(n-2)

贴一下这个题的整体思路 非记忆化递归时间复杂度O(2^n)，空间复杂度O(n)肯定会超时——存在重复子问题 记忆化递归，时间复杂度O(n)，空间复杂度O(n)

class Solution {
    private int[] memo;

    public int numWays(int n) {
        memo = new int[n + 1];
        Arrays.fill(memo, -1);
        return jump(n);
    }

    private int jump(int n) {
        if (memo[n] != -1) {
            return memo[n];
        }
        if (n == 1 || n == 0) {
            return 1;
        }
        memo[n] = (jump(n - 1) + jump(n - 2)) % 1000_000_007;
        return memo[n];
    }
}
动态规划，时间复杂度O(n)，空间复杂度O(n);

public class Solution {
    public int numWays(int n) {
        if (n == 0 || n == 1) {
            return 1;
        }
        int[] dp = new int[n + 1];
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i <= n; i++) {
            dp[i] = (dp[i - 2] + dp[i - 1]) % 1000_000_007;
        }
        return dp[n];
    }
}
O(1)空间复杂度的动态规划

public class Solution {
    public int numWays(int n) {
        if (n == 0 || n == 1) {
            return 1;
        }
        int pre = 1, cur = 2;
        for (int i = 3; i <= n; i++) {
            int tmp = (pre + cur) % 1000_000_007;
            pre = cur;
            cur = tmp;
        }
        return cur;
    }
}
"""


class Solution:
    def numWays(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        pre = 1
        cur = 2
        for _ in range(3, n+1):
            pre, cur = cur, (pre + cur)
        return cur % 1000000007

        # def numWays(self, n: int) -> int:
        #     a, b = 1, 1
        #     for _ in range(n):
        #         a, b = b, a + b
        #     return a % 1000000007


print(Solution().numWays(3))
