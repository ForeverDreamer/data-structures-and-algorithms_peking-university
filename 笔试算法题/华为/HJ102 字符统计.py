"""
HJ102 字符统计

描述
输入一个只包含小写英文字母和数字的字符串，按照不同字符统计个数由多到少输出统计结果，如果统计的个数相同，则按照ASCII码由小到大排序输出。
本题含有多组样例输入
数据范围：字符串长度满足 1≤len(str)≤1000

输入描述：
一个只包含小写英文字母和数字的字符串。

输出描述：
一个字符串，为不同字母出现次数的降序表示。若出现次数相同，则按ASCII码的升序输出。

示例1
输入：
aaddccdc
1b1bbbbbbbbb
复制
输出：
cda
b1
复制
说明：
第一个样例里，c和d出现3次，a出现2次，但c的ASCII码比d小，所以先输出c，再输出d，最后输出a.
"""


# 代码1
# while True:
#     try:
#         s = input()
#         ss = sorted(list(set(s)), key=lambda x:s.count(x)*1000-ord(x), reverse=True)
#         print("".join(ss))
#     except:
#         break


# 代码2
# while True:
#     try:
#         a = input()
#         s = sorted(set(a))
#         ss = sorted(s,key=lambda x:a.count(x),reverse=True)
#         print(''.join(ss))
#     except:
#         break


# 代码3
# while True:
#     try:
#         input_string = input()
#         sorted_list = sorted(input_string)
#         dic, ans = {}, ''
#
#         for item in sorted_list:
#             if item not in dic:
#                 number = sorted_list.count(item)
#                 dic.setdefault(item, number)
#
#         new_list = sorted(dic.items(), key=lambda items:(-items[1], items[0]))
#
#         for item in new_list:
#             ans += item[0]
#
#         print(ans)
#     except:
#         break
