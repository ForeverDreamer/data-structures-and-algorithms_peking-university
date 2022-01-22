"""
HJ46 截取字符串

描述
输入一个字符串和一个整数 k ，截取字符串的前k个字符并输出

本题输入含有多组数据

数据范围：字符串长度满足 1≤n≤100，1≤k≤n
输入描述：
1.输入待截取的字符串

2.输入一个正整数k，代表截取的长度

输出描述：
截取后的字符串

示例1
输入：
abABCcDEF
6
输出：
abABCc

示例2
输入：
ffIKEHauv
1
bdxPKBhih
6
输出：
f
bdxPKB
"""

input_seq = ['abABCcDEF', '6', 'ffIKEHauv', '1', 'bdxPKBhih', '6']


def execute(chars, k):
    return chars[0:k]


def beautiful_degree(seq):
    output_seq = []
    i = 0
    while i+2 <= len(seq):
        chars = seq[i]
        k = int(seq[i+1])
        output_seq.append(execute(chars, k))
        i += 2
    return output_seq


for item in beautiful_degree(input_seq):
    print(item)