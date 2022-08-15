"""
面试题19. 正则表达式匹配

请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。

示例 1:
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

示例 2:
输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

示例 3:
输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

示例 4:
输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

示例 5:
输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母以及字符 . 和 *，无连续的 '*'。

方法一：动态规划
复杂度分析
时间复杂度：O(mn)，其中 m 和 n 分别是字符串 s 和 p 的长度。我们需要计算出所有的状态，并且每个状态在进行转移时的时间复杂度为 O(1)。
空间复杂度：O(mn)，即为存储所有状态使用的空间。

s = "aab"
p = "c*a*b"
    c * a * b
  T F T F T F    s = ''
a F F F T T F    s = 'a'
a F F F F T F    s = 'aa'
b F F F F F T    s = 'aab'
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j-1] == '.':
                return True
            return s[i-1] == p[j-1]

        f = [[False] * (n+1) for _ in range(m+1)]
        f[0][0] = True
        for i in range(m+1):
            for j in range(1, n+1):
                # 不管以什么方式匹配，只要能匹配上，相当于新增字符就对匹配状态没有影响，当前的状态就由前边某一步的状态决定，否则就是默认的False
                # i和j是动态规划表的下标，对应的字符串的下标均需要-1
                if p[j-1] == '*':
                    # 默认匹配0次
                    f[i][j] = f[i][j-2]
                    if matches(i, j-1):
                        # 匹配0次或1次任一种情况为True当前就为True，即可以选择f[i][j-2] or f[i-1][j]
                        f[i][j] |= f[i-1][j]
                else:
                    if matches(i, j):
                        f[i][j] = f[i-1][j-1]
        return f[m][n]


print(Solution().isMatch('aab', "c*a*b"))
