"""
HJ65 查找两个字符串a,b中的最长公共子串

描述
查找两个字符串a,b中的最长公共子串。若有多个，输出在较短串中最先出现的那个。
注：子串的定义：将一个字符串删去前缀和后缀（也可以不删）形成的字符串。请和“子序列”的概念分开！

本题含有多组输入数据！
数据范围：字符串长度1≤s≤300 ，1≤t≤5
进阶：时间复杂度：O(n^3)，空间复杂度：O(n)

输入描述：
输入两个字符串

输出描述：
返回重复出现的字符

示例1
输入：
abcdefghijklmnop
abcsafjklmnopqrstuvw
输出：
jklmnop
"""


while True:
    try:
        s1 = input()
        s2 = input()
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        m, n = len(s1), len(s2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        index, max_len = 0, 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
                        index = i
                else:
                    dp[i][j] = 0
        print(s1[index-max_len:index])
    except:
        break
