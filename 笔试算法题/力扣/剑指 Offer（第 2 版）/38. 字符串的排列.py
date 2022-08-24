"""
剑指 Offer 38. 字符串的排列

输入一个字符串，打印出该字符串中字符的所有排列。
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

示例:
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
 
限制：
1 <= s 的长度 <= 8
"""


class Solution:
    def permutation(self, s: str):
        all_chars, res = list(s), []
        def dfs(pos):
            if pos == len(all_chars) - 1:
                res.append(''.join(all_chars))   # 添加排列方案
                return
            pos_chars = set()
            for i in range(pos, len(all_chars)):
                if all_chars[i] in pos_chars:
                    continue  # 重复，因此剪枝
                pos_chars.add(all_chars[i])
                if i != pos:
                    all_chars[i], all_chars[pos] = all_chars[pos], all_chars[i]  # 交换，将 c[i] 固定在第 x 位
                dfs(pos+1)               # 开启固定第 x + 1 位字符
                if i != pos:
                    all_chars[i], all_chars[pos] = all_chars[pos], all_chars[i]  # 恢复交换
        dfs(0)
        return res


print(Solution().permutation('abc'))
print(Solution().permutation('abb'))
