"""
HJ4 字符串分隔

描述
•连续输入字符串，请按长度为8拆分每个输入字符串并进行输出；
•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
（注：本题有多组输入）
输入描述：
连续输入字符串(输入多次,每个字符串长度小于等于100)

输出描述：
依次输出所有分割后的长度为8的新字符串

示例1
输入：
abc
123456789
输出：
abc00000
12345678
90000000
"""

input_seq = ['abc', '123456789']
# 牛客网代码
# input_seq = []
# while True:
#     try:
#         input_seq.append(input().strip())
#     except EOFError:
#         break

output_seq = []
unit_len = 8

for item in input_seq:
    start = 0
    while start < len(item):
        if len(item) <= unit_len:
            zeros = ''.join(['0']*(unit_len-len(item)))
            output_seq.append(item+zeros)
            break
        else:
            sub_item = item[start:start + unit_len]
            zeros = ''.join(['0'] * (unit_len - len(sub_item)))
            output_seq.append(sub_item+zeros)
            start += unit_len

for item in output_seq:
    print(item)
