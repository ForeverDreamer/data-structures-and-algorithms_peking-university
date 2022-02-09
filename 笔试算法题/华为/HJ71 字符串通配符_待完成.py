"""
HJ71 字符串通配符

描述
问题描述：在计算机中，通配符一种特殊语法，广泛应用于文件搜索、数据库、正则表达式等领域。现要求各位实现字符串通配符的算法。
要求：
实现如下2个通配符：
*：匹配0个或以上的字符（注：能被*和?匹配的字符仅由英文字母和数字0到9组成，下同）
？：匹配1个字符

注意：匹配时不区分大小写。

输入：
通配符表达式；
一组字符串。
输出：

返回不区分大小写的匹配结果，匹配成功输出true，匹配失败输出false
注意：本题含有多组样例输入！
数据范围：数据组数：1≤t≤10 ，字符串长度：1≤s≤100
进阶：时间复杂度：O(n^2)，空间复杂度：O(n)
输入描述：
先输入一个带有通配符的字符串，再输入一个需要匹配的字符串

输出描述：
返回不区分大小写的匹配结果，匹配成功输出true，匹配失败输出false

示例1
输入：
te?t*.*
txt12.xls
输出：
false

示例2
输入：
z
zz
输出：
false

示例3
输入：
pq
pppq
输出：
false

示例4
输入：
**Z
0QZz
输出：
true

示例5
输入：
?*Bc*?
abcd
输出：
true

示例6
输入：
h*?*a
h#a
输出：
false

说明：
根据题目描述可知能被*和?匹配的字符仅由英文字母和数字0到9组成，所以?不能匹配#，故输出false
示例7
输入：
p*p*qp**pq*p**p***ppq
pppppppqppqqppqppppqqqppqppqpqqqppqpqpppqpppqpqqqpqqp
复制
输出：
false
          t     x     t     1     2     .     x     l     s
  True  False False False False False False False False False
t False False False False False False False False False False
e False False False False False False False False False False
? False False False False False False False False False False
t False False False False False False False False False False
* False False False False False False False False False False
. False False False False False False False False False False
* False False False False False False False False False False

"""

from string import ascii_uppercase, ascii_lowercase, digits

input_seq = [
    # 't?t*.*', 'txt12.xls',
    # 'te?t*.*', 'txt12.xls',
    # 'z', 'zz',
    # 'pq', 'pppq',
    # '**Z', '0QZz',
    # '?*Bc*?', 'abcd',
    # 'h*?*a', 'h#a',
    # '**h', 'hhh',
    # '*h', 'h',
    # 'dvq*duz*bqlwqaxu*gtrra?k',
    # 'dvqyduzebqlwqaxusgtrratk',
    # 'h*h*ah**ha*h**h***hha',
    # 'hhhhhhhahhaahhahhhhaaahhahhahaaahhahahhhahhhahaaahaah',
    't?t*1*.*',
    'txt12.xls',
    '?*Bc*?',
    'abcd',
]


# 牛客网答案
class Solution:
    def match(self, p: str, s: str) -> bool:
        # 边界定义-各种单边或双边为空的情况
        if s == '' and p == '':
            return True
        elif s != '' and p == '':
            return False
        elif s == '':
            if p.replace('*', '') == '':
                return True
            else:
                return False
            # 字符串与通配符均不为空，递归检查
        else:
            n, m = len(s), len(p)
            # '''通配符是问号或者字母'''
            if (p[m - 1] == '?' and s[n - 1].isalnum()) or p[m - 1].lower() == s[n - 1].lower():
                return self.match(p[0:m - 1], s[0:n - 1])
            # '''通配符是星号'''
            elif p[m - 1] == '*':
                return self.match(p[0:m - 1], s) or self.match(p, s[0:n - 1])

            # '''通配符不是问号或者字母，还跟字符串匹配不上'''
            else:
                return False


while True:
    try:
        p, s = input(), input()
        s1 = Solution()
        print('true' if s1.match(p, s) else 'false')

    except:
        break

# def is_letter_or_digit(c):
#     return c in (ascii_uppercase + ascii_lowercase + digits)


# 采用递归的思路。从前向后依次匹配：
# 遇到相同字符，都向后移动一个字符；
# 如果通配符遇到"?"，则不需匹配，自动跳过一个字符；（此种情况要判断跳过的这个字符是否在限定范围内）
# 如果通配符遇到"*"，则可以匹配任意多个字符，包括0个，此时可以有三种选择：（此种情况要判断跳过的这个字符是否在限定范围内）
# 1.匹配0个，通配符向后移动一个字符，字符串不动；
# 2.匹配1个，通配符和字符串都向后移动一个字符；
# 3.匹配多个，通配符不动，字符串向后移动一个字符。
# 递归的终止条件：通配符或者字符串遇到’\0’。表示同时结束，返回true。
# ————————————————
# 版权声明：本文为CSDN博主「你板子冒烟了」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/engineer0/article/details/120574491
# def execute(pattern, chars):
#     i = 0
#     j = 0
#     while (i < len(pattern)) and (j < len(chars)):
#         c1 = pattern[i]
#         c2 = chars[j]
#         if c1 == '?':
#             if is_letter_or_digit(c2):
#                 i += 1
#                 j += 1
#             else:
#                 return False
#         elif c1 == '*':
#             if is_letter_or_digit(c2):
#                 # try:
#                 #     # 匹配0个字符
#                 #     if pattern[i+1].lower() == c2.lower():
#                 #         i += 1
#                 #         continue
#                 #     # 匹配多个字符
#                 #     while is_letter_or_digit(chars[j+1]):
#                 #         if pattern[i+1].lower() != chars[j+1].lower():
#                 #             j += 1
#                 #         else:
#                 #             break
#                 #     i += 1
#                 # except IndexError:
#                 #     j += 1
#                 # 匹配0个字符
#                 # 匹配1个字符
#                 # 匹配多个字符
#                 try:
#                     return execute(pattern[i+1], chars[j]) or execute(pattern[i+1], chars[j+1]) or execute(pattern[i], chars[j+1])
#                 except IndexError:
#                     pass
#             else:
#                 i += 1
#         else:
#             if c1.lower() == c2.lower():
#                 i += 1
#                 j += 1
#             else:
#                 return False
#     if j < len(chars):
#         return False
#     while i+1 < len(pattern):
#         if pattern[i+1] == '*':
#             i += 1
#         else:
#             return pattern[i+1] == chars[j-1]
#
#     return True


# 解题思路：(待验证)
# 本题用动态规划解比递归要方便，而且速度也快些。输入两个字符串，按照各自的尺寸建立二维数组，并定义(0,0)点为true，其他默认为false；
# 每一行首值的取值，取决于上一行首值和通配符字符串s1该位置字符是否为'*'，即当s2无字符时，s1只有首字符为'*'才能与其匹配；
# 之后继续填充，首行数值均为false，即s1无字符时，无法进行匹配；从第二行第二列开始，一行行填充，若s1对应位置的字符为'*'，
# 则该行的数值由其同行前列和同列前行决定，若其同列前行为true，表明之前的匹配均合理，再考虑到*可以匹配0个字符，所以该位置可以true，
# 但注意，还要判断s2字符是否合理；若该行对应s1字符为正常字母数字，则进行正常比对，若同s2字符一致（不区分大小写），且其前列前行为true，
# 则当前也为true，这是当前已经成功匹配的字符串位置；若s1字符为'?'，则只需判断s2字符是否合理，若合理且前列前行也为true，当前也为true。

# 动态规划的二维表遍历完，最终匹配结果就是v[m][n]。解题完毕。
# def execute(pattern, chars):
#     m = len(pattern)
#     n = len(chars)
#     table = [[False for j in range(n+1)] for i in range(m+1)]
#     table[0][0] = True
#     for i in range(1, m+1):
#         table[i][0] = table[i-1][0] and pattern[i-1] == '*'
#         for j in range(1, n+1):
#             if pattern[i-1] == '*':
#                 if is_letter_or_digit(chars[j-1]):
#                     table[i][j] = table[i-1][j] or table[i][j-1]
#                 else:
#                     if pattern[i-1].lower() == chars[j-1].lower():
#                         table[i][j] = table[i-1][j-1]
#                     if pattern[i-1] == '?' and is_letter_or_digit(chars[j-1]):
#                         table[i][j] = table[i-1][j-1]
#     return table[m][n]


# def wildcard_character(seq):
#     output_seq = []
#     i = 0
#     while i+1 < len(seq):
#         pattern = seq[i]
#         chars = seq[i+1]
#         output_seq.append('true' if execute(pattern, chars) else 'false')
#         i += 2
#     for item in output_seq:
#         print(item)
#
#
# wildcard_character(input_seq)
