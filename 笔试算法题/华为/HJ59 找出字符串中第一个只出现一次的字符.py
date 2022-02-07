"""
HJ59 找出字符串中第一个只出现一次的字符

描述
找出字符串中第一个只出现一次的字符

数据范围：输入的字符串长度满足 1≤n≤1000

输入描述：
输入几个非空字符串

输出描述：
输出第一个只出现一次的字符，如果不存在输出-1

示例1
输入：
asdfasdfo
aabb
输出：
o
-1
"""

input_seq = ['asdfasdfo', 'aabb']


def execute(chars):
    dic = {}
    for i, c in enumerate(chars):
        if c in dic:
            dic[c] = [dic[c][0]+1, dic[c][1]]
        else:
            dic[c] = [1, i]
    arr = [v[1] for v in dic.values() if v[0] == 1]
    arr.sort()
    if len(arr) == 0:
        return -1
    return chars[arr[0]]


def find_first_once_str(seq):
    output_seq = []
    for chars in seq:
        output_seq.append(execute(chars))
    for item in output_seq:
        print(item)


find_first_once_str(input_seq)
