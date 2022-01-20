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

input_seq = ['22', '100', '145', '1234', '8088', '486669', '1652510']


zero_to_nine = ('', "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
eleven_to_nighteen = ("ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nighteen")
twenty_to_ninety = ('', '', "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred")
units = ['', '', 'thousand', 'million', 'billion']


def transform_num(n_str):
    n = int(n_str)
    fixed_str = str(n)
    if 0 <= n < 10:
        return zero_to_nine[int(n)]
    elif 10 <= n < 20:
        return eleven_to_nighteen[n-10]
    elif 20 <= n < 100:
        return twenty_to_ninety[int(fixed_str[0])] + ' ' + zero_to_nine[int(fixed_str[1])]
    elif 100 <= n < 1000:
        result = zero_to_nine[int(fixed_str[0])] + ' ' + twenty_to_ninety[-1]
        result2 = transform_num(fixed_str[1:])
        if result2:
            result = result + ' ' + 'and' + ' ' + result2
        return result


def execute(n_str):
    n_arr = []
    result = []
    i = len(n_str)
    while i-3 >= 0:
        n_arr.append(n_str[i-3:i])
        i -= 3
    left_len = len(n_str)-len(n_arr)*3
    if left_len > 0:
        n_arr.append(n_str[0:left_len])
    n_arr.reverse()
    i_unit = len(n_arr)
    for n in n_arr:
        result.append(transform_num(n))
        # result.append(n)
        if units[i_unit]:
            result.append(units[i_unit])
        i_unit -= 1
    return ' '.join(result)


def num_to_english(seq):
    output_seq = []
    for n_str in seq:
        output_seq.append(execute(n_str))
    return output_seq


for item in num_to_english(input_seq):
    print(item)
