"""
剑指 Offer 50. 第一个只出现一次的字符

在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例 1:
输入：s = "abaccdeff"
输出：'b'

示例 2:
输入：s = ""
输出：' '
 
限制：
0 <= s 的长度 <= 50000
"""

import collections

# class Solution:
#     def firstUniqChar(self, s: str) -> str:
#         dic = {}
#         for c in s:
#             dic[c] = c not in dic
#         for c in s:
#             if dic[c]: return c
#         return ' '


class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = collections.OrderedDict()
        for c in s:
            dic[c] = c not in dic
        for k, v in dic.items():
            if v:
                return k
        return ' '
