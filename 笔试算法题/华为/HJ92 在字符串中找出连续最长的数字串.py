"""
HJ92 在字符串中找出连续最长的数字串

描述
输入一个字符串，返回其最长的数字子串，以及其长度。若有多个最长的数字子串，则将它们全部输出（按原字符串的相对位置）
本题含有多组样例输入。

数据范围：字符串长度 1≤n≤200  ， 保证每组输入都至少含有一个数字
输入描述：
输入一个字符串。1<=len(字符串)<=200

输出描述：
输出字符串中最长的数字字符串和它的长度，中间用逗号间隔。如果有相同长度的串，则要一块儿输出（中间不要输出空格）。

示例1
输入：
abcd12345ed125ss123058789
a8a72a6a5yy98y65ee1r2
复制
输出：
123058789,9
729865,2
复制
说明：
样例一最长的数字子串为123058789，长度为9
样例二最长的数字子串有72,98,65，长度都为2
"""


# 代码1
# 把非数字的全部替换成空格，然后切割；
# 遍历一次得到最大长度；
# 再遍历一次，把符合上述最大长度的字符串取出作追加拼接。
# while True:
#     try:
#         s = input()
#         for c in s:
#             if not c.isdigit():
#                 s = s.replace(c, " ")
#         s = s.split()
#         max_flag = 0
#         res = ""
#         for c in s:
#             if len(c)>max_flag:
#                 max_flag = len(c)
#         for c in s:
#             if len(c)==max_flag:
#                 res = res+c
#         print(str(res)+','+str(max_flag))
#     except:
#         break


# 代码2
# import sys
# for line in sys.stdin:
#     s=line.strip()
#     for i in s:
#         if i.isdigit()==False: #将非数字替换成空格
#             s=s.replace(i," ")
#     s=s.split() #生成列表
#     r1=max([len(i) for i in s]) #巧妙生成长度列表，并找到最大的
#
#     for i in s:
#         if len(i)==r1:
#             print(i,end='')#不换行输出，当然也可以先拼接起来再输出
#     print(','+str(r1))
