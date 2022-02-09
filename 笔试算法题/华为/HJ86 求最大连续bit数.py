"""
HJ86 求最大连续bit数

描述
求一个int类型数字对应的二进制数字中1的最大连续数，例如3的二进制为00000011，最大连续2个1
本题含有多组样例输入。
数据范围：数据组数：1≤t≤5 ，1≤n≤500000
进阶：时间复杂度：O(logn) ，空间复杂度：O(1)
输入描述：
输入一个int类型数字

输出描述：
输出转成二进制之后连续1的个数

示例1
输入：
3
5
200
复制
输出：
2
1
2
复制
说明：
3的二进制表示是11，最多有2个连续的1。
5的二进制表示是101，最多只有1个连续的1。
"""

# 代码1
# while True:
#     try:
#         x = int(input())
#         byte_x = bin(x)[2:]
#         list1 = sorted(list(set(byte_x.split('0'))), key = lambda x: len(x), reverse=True)
#         print(len(list1[0]))
#     except:
#         break


# 代码2
# while True:
#     try:
#         s = input()
#         ## 数字格式-> 二元格式 -> 清除非数字 -> 零作为间隔符号
#         string = bin(int(s)).replace("0b", "").split("0")
#         longest = 0
#         for i in string:
#             count = i.count("1")
#             if count > longest:
#                 longest = count
#         print(longest)
#     except:
#         break


# 代码3
# while True:
#     try:
#         n = int(input())
#         s = bin(n).replace('0b', '')
#         s = (8 - len(s)) * '0' + s
#         Max, count = 1, 1
#         i = s.index('1')
#         while i < len(s) - 1:
#             for j in range(i+1, len(s)):
#                 if s[j] == '1':
#                     count += 1
#                 else:
#                     break
#                 Max = max(Max, count)
#             if '1' in s[j+1:]:
#                 i = s.index('1', j+1)
#                 count = 1
#             else:
#                 break
#         print(Max)
#     except:
#         break


# 代码4
# while True:
#     try:
#         s = int(input())
#         b = bin(s)
#         print(len(max(b.split('b')[1].split('0'))))
#     except:
#         break
