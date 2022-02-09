"""
HJ42 学英语

描述
Jessi初学英语，为了快速读出一串数字，编写程序将数字转换成英文：

具体规则如下:
1.在英语读法中三位数字看成一整体，后面再加一个计数单位。从最右边往左数，三位一单位，例如12,345 等
2.每三位数后记得带上计数单位 分别是thousand, million, billion.
3.公式：百万以下千以上的数 X thousand X, 10亿以下百万以上的数：X million X thousand X, 10 亿以上的数：X billion X million X thousand X. 每个X分别代表三位数或两位数或一位数。
4.在英式英语中百位数和十位数之间要加and，美式英语中则会省略，我们这个题目采用加上and，百分位为零的话，这道题目我们省略and

下面再看几个数字例句：
22: twenty two
100:  one hundred
145:  one hundred and forty five
1,234:  one thousand two hundred and thirty four
8,088:  eight thousand (and) eighty eight (注:这个and可加可不加，这个题目我们选择不加)
486,669:  four hundred and eighty six thousand six hundred and sixty nine
1,652,510:  one million six hundred and fifty two thousand five hundred and ten

说明：
数字为正整数，不考虑小数，转化结果为英文小写；
保证输入的数据合法
关键字提示：and，billion，million，thousand，hundred。

数据范围：1≤n≤2000000

本题含有多组输入数据。

输入描述：
输入多行long型整数

输出描述：
输出相应的英文写法

示例1
输入：
22
100
145
1234
8088
486669
1652510
输出：
twenty two
one hundred
one hundred and forty five
one thousand two hundred and thirty four
eight thousand eighty eight
four hundred and eighty six thousand six hundred and sixty nine
one million six hundred and fifty two thousand five hundred and ten
"""

# 代码1
num1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six',
        'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
        'thirteen', 'fourteen', 'fifteen', 'sixteen',
        'seventeen', 'eighteen', 'nineteen']
num2 = [0, 0, 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
        'seventy', 'eighty', 'ninety']


# 100以内转英文
def n2w(n):
    if n > 0:
        if n < 20:
            word.append(num1[n])
        else:
            word.append(num2[n // 10])
            if n % 10 != 0:
                word.append(num1[n % 10])


# 1000以内转英文
def hun(n):
    if n >= 100:
        word.append(num1[n // 100])
        word.append('hundred')
        if n % 100 != 0:
            word.append('and')
    n2w(n % 100)


while True:
    try:
        n = int(input())
    except:
        break
    else:
        word = []
        a = n % 1000  # 个十百位
        b = (n // 1000) % 1000  # 个十百千
        c = (n // 1000000) % 1000  # 个十百m
        d = n // 1000000000  # 个十百b

        if d > 0:
            hun(d)
            word.append('billion')
        if c > 0:
            hun(c)
            word.append('million')
        if b > 0:
            hun(b)
            word.append('thousand')
        if a > 0:
            hun(a)
        print(' '.join(word))


# 代码2
# lst = [
#     'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
#     'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
#     'eighteen', 'nineteen'
# ]
#
# dic = {
#     2 : 'twenty', 3 : 'thirty', 4 : 'forty', 5 : 'fifty', 6 : 'sixty',
#     7 : 'seventy', 8 : 'eighty', 9 : 'ninety'
# }
#
# def eng(n):
#     if n < 20:
#         return lst[n - 1]
#     else:
#         if n % 10 == 0:
#             return dic[n // 10]
#         else:
#             return dic[n // 10] + ' ' + lst[n % 10 - 1]
#
# while True:
#     try:
#         s = input()
#         if not s.isdigit():
#             print('error')
#             continue
#         sgood = ''
#         for i, c in enumerate(s[::-1]):
#             sgood += c
#             if (i + 1) % 3 == 0:
#                 sgood += ','
#         sgood = sgood[::-1]
#         nums = sgood.split(',')
#         for i, n in enumerate(nums):
#             if not n:
#                 continue
#             if len(n) == 3:
#                 if n[0] != '0':
#                     print(eng(int(n[0])), 'hundred', end=' ')
#                     if int(n[1:]) > 0:
#                         print('and', end=' ')
#                         print(eng(int(n[1:])), end=' ')
#                 else:
#                     print(eng(int(n)), end=' ')
#             else:
#                 print(eng(int(n)), end=' ')
#             # 单位判断
#             if len(nums[i:]) == 4:
#                 print('billion', end=' ')
#             elif len(nums[i:]) == 3:
#                 print('million', end=' ')
#             elif len(nums[i:]) == 2:
#                 print('thousand', end=' ')
#         print()
#     except:
#         break


# 代码3
# s_1 = {'0': '', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight',
#        '9': 'nine'}
# s_2 = {'10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen',
#        '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen'}
# s_3 = {'2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty', '6': 'sixty', '7': 'seventy', '8': 'eighty',
#        '9': 'ninety', }
#
#
# def print_e(j, b):
#     if (j == 0):
#         if (b[0] == '0') & (b[1] == '0') & (b[2] == '0'):
#             return ''
#         else:
#             if (b[0] == '0'):
#                 if (b[1] == '0'):
#                     return s_1[b[2]] + ' million '
#                 elif (b[1] == '1'):
#                     return s_2[b[1] + b[2]] + ' million '
#                 else:
#                     return s_3[b[1]] + ' ' + s_1[b[2]] + ' million '
#             else:
#                 if (b[1] == '0'):
#                     return s_1[b[0]] + ' hundred' + ' and ' + s_1[b[2]] + ' million '
#                 elif (b[1] == '1'):
#                     return s_1[b[0]] + ' hundred ' + ' and ' + s_2[b[1] + b[2]] + ' million '
#                 else:
#                     return s_1[b[0]] + ' hundred ' + ' and ' + s_3[b[1]] + ' ' + s_1[b[2]] + ' million '
#     elif (j == 1):
#         if (b[0] == '0') & (b[1] == '0') & (b[2] == '0'):
#             return ''
#         else:
#             if (b[0] == '0'):
#                 if (b[1] == '0'):
#                     return s_1[b[2]] + ' thousand '
#                 elif (b[1] == '1'):
#                     return s_2[b[1] + b[2]] + ' thousand '
#                 else:
#                     return s_3[b[1]] + ' ' + s_1[b[2]] + 'thousand '
#             else:
#                 if (b[1] == '0'):
#                     return s_1[b[0]] + ' hundred' + ' and ' + s_1[b[2]] + ' thousand '
#                 elif (b[1] == '1'):
#                     return s_1[b[0]] + ' hundred' + ' and ' + s_2[b[1] + b[2]] + ' thousand '
#                 else:
#                     return s_1[b[0]] + ' hundred' + ' and ' + s_3[b[1]] + ' ' + s_1[b[2]] + ' thousand '
#     else:
#         if (b[0] == '0') & (b[1] == '0') & (b[2] == '0'):
#             return ''
#         else:
#             if (b[0] == '0'):
#                 if (b[1] == '0'):
#                     return s_1[b[2]]
#                 elif (b[1] == '1'):
#                     return s_2[b[1] + b[2]]
#                 else:
#                     return s_3[b[1]] + ' ' + s_1[b[2]]
#             else:
#                 if (b[1] == '0'):
#                     if (b[2] == '0'):
#                         return s_1[b[0]] + ' hundred '
#                     else:
#                         return s_1[b[0]] + ' hundred ' + 'and ' + s_1[b[2]]
#                 elif (b[1] == '1'):
#                     return s_1[b[0]] + ' hundred ' + 'and ' + s_2[b[1] + b[2]]
#                 else:
#                     return s_1[b[0]] + ' hundred ' + 'and ' + s_3[b[1]] + ' ' + s_1[b[2]]
#
#
# while True:
#     try:
#         num = int(input())
#         num = '{:09d}'.format(num)
#         num = list(num)
#         num.insert(3, ',')
#         num.insert(7, ',')
#         num = ''.join(num)
#         num = num.split(',')
#         num_1 = print_e(0, num[0])
#         num_2 = print_e(1, num[1])
#         num_3 = print_e(2, num[2])
#         print(num_1 + num_2 + num_3)
#
#     except:
#         break


# input_seq = ['22', '100', '145', '1234', '8088', '486669', '1652510']
#
#
# zero_to_nine = ('', "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
# eleven_to_nighteen = ("ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nighteen")
# twenty_to_ninety = ('', '', "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred")
# units = ['', '', 'thousand', 'million', 'billion']
#
#
# def transform_num(n_str):
#     n = int(n_str)
#     fixed_str = str(n)
#     if 0 <= n < 10:
#         return zero_to_nine[int(n)]
#     elif 10 <= n < 20:
#         return eleven_to_nighteen[n-10]
#     elif 20 <= n < 100:
#         return twenty_to_ninety[int(fixed_str[0])] + ' ' + zero_to_nine[int(fixed_str[1])]
#     elif 100 <= n < 1000:
#         result = zero_to_nine[int(fixed_str[0])] + ' ' + twenty_to_ninety[-1]
#         result2 = transform_num(fixed_str[1:])
#         if result2:
#             result = result + ' ' + 'and' + ' ' + result2
#         return result
#
#
# def execute(n_str):
#     n_arr = []
#     result = []
#     i = len(n_str)
#     while i-3 >= 0:
#         n_arr.append(n_str[i-3:i])
#         i -= 3
#     left_len = len(n_str)-len(n_arr)*3
#     if left_len > 0:
#         n_arr.append(n_str[0:left_len])
#     n_arr.reverse()
#     i_unit = len(n_arr)
#     for n in n_arr:
#         result.append(transform_num(n))
#         # result.append(n)
#         if units[i_unit]:
#             result.append(units[i_unit])
#         i_unit -= 1
#     return ' '.join(result)
#
#
# def num_to_english(seq):
#     output_seq = []
#     for n_str in seq:
#         output_seq.append(execute(n_str))
#     return output_seq
#
#
# for item in num_to_english(input_seq):
#     print(item)
