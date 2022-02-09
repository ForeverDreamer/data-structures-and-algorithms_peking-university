"""
HJ75 公共子串计算

描述
给定两个只包含小写字母的字符串，计算两个字符串的最大公共子串的长度。

注：子串的定义指一个字符串删掉其部分前缀和后缀（也可以不删）后形成的字符串。
数据范围：字符串长度：1≤s≤150
进阶：时间复杂度：O(n^3)，空间复杂度：O(n)
输入描述：
输入两个只包含小写字母的字符串

输出描述：
输出一个整数，代表最大公共子串的长度

示例1
输入：
asdfas
werasdfaswer
输出：
6

方法二：动态规划
实现思路
我们定义dp[i][j]的含义为在s1，s2中分别以s1[i-1],s2[j-1]为结尾的两个公共子串的长度。当dp[i][j]=0时说明s1[i-1] != s2[j-1]
然后遍历两个字符串，指针分别为i和j，当出现s1[i] == s2[j]的时候，则说明需要更新dp[i+1][j+1] = 1 + dp[i][j]
因此我们有转移方程
dp[i+1][j+1]=1+dp[i][j]          if(s1[i]==s2[j])
最终返回记录的dp数组中最大值即可
"""


def solution(s1, s2):
    mxlen = 0
    dp = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]  # 动态规划数组
    for i in range(len(s1)):
        for j in range(len(s2)):  # 想要找到两个字符串中相同的字母，然后看看以这公共字母结尾的子串是否能进行长度拓展
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1  # 更新最长子串的值
                if dp[i + 1][j + 1] > mxlen:
                    mxlen = dp[i + 1][j + 1]
    return mxlen


while True:
    try:
        s1 = input()
        s2 = input()
        print(solution(s1, s2))
    except:
        break
