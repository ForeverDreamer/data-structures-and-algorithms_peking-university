"""
HJ81 字符串字符匹配

描述
判断短字符串S中的所有字符是否在长字符串T中全部出现。
请注意本题有多组样例输入。
数据范围:1≤len(S),len(T)≤200
进阶：时间复杂度：O(n) ，空间复杂度：O(n)
输入描述：
输入两个字符串。第一个为短字符串，第二个为长字符串。两个字符串均由小写字母组成。

输出描述：
如果短字符串的所有字符均在长字符串中出现过，则输出字符串"true"。否则输出字符串"false"。

示例1
输入：
bc
abc
apgmlivuembu
tyjmrcuneguxmsqwjslqvfmw
bca
abc
复制
输出：
true
false
true
复制
说明：
第一组样例:
bc
abc
其中abc含有bc，输出"true"
第二组样例，上面短字符串的a就没有在下面长字符串出现，输出"false"
"""


while True:
    try:
        str1 = list(input())
        str2 = list(input())
        for i in str1:
            if i not in str2:
                print('false')
                break
        else:
                print('true')
    except:
        break

