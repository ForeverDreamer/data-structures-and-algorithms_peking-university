"""
HJ2 计算某字符出现次数

描述
写出一个程序，接受一个由字母、数字和空格组成的字符串，和一个字符，然后输出输入字符串中该字符的出现次数。（不区分大小写字母）

数据范围：
输入描述：
第一行输入一个由字母和数字以及空格组成的字符串，第二行输入一个字符。

输出描述：
输出输入字符串中含有该字符的个数。（不区分大小写字母）

示例1
输入：
ABCabc
A
输出：
2
"""
# s = "www.runoob.com"
# print(s.upper())          # 把所有字符中的小写字母转换成大写字母
# print(s.lower())          # 把所有字符中的大写字母转换成小写字母
# print(s.capitalize())     # 把第一个字母转化为大写字母，其余小写
# print(s.title())          # 把每个单词的第一个字母转化为大写，其余小写
# print('AaBb 2 3 c'.upper())
# print('AaBb 2 3 c'.lower())
# print(ord('A')+32)
# print(ord('a'))

# chars = 'AaBbb 2 3c'
# target = 'A'
# chars = 'c'
# target = 'j'


def count_char(chars, target):
    char = target.upper()
    count = 0
    for c in chars.upper():
        if c == char:
            count += 1
    return count


# print('A: ', count_char('A'))
# print('a: ', count_char('a'))
# print('B: ', count_char('B'))
# print('b: ', count_char('b'))
# print('空格: ', count_char(' '))
# print('2: ', count_char('2'))
# print('3: ', count_char('3'))
# print('c: ', count_char('c'))

print(count_char('AaBbb 2 3c', 'b'))
print(count_char('c', 'j'))


# 牛客网窗口代码
# input_chars = input().strip()
# input_target = input().strip()
#
#
# def count_char(chars, target):
#     char = target.upper()
#     count = 0
#     for c in chars.upper():
#         if c == char:
#             count += 1
#     return count
#
#
# print(count_char(input_chars, input_target))
