"""
HJ67 24点游戏算法

描述
给出4个1-10的数字，通过加减乘除运算，得到数字为24就算胜利,除法指实数除法运算,本题对数字选取顺序无要求，但每个数字仅允许使用一次，且不考虑括号运算
此题允许数字重复，如3 3 4 4为合法输入，此输入一共有两个3，但是每个数字只允许使用一次，则运算过程中两个3都被选取并进行对应的计算操作。
输入描述：
本题有多组案例。对于每组案例读入4个[1,10]的整数，数字允许重复，测试用例保证无异常数字。

输出描述：
对于每组案例，输出一行表示能否得到24点，能输出true，不能输出false

示例1
输入：
7 2 1 10
输出：
true
"""

import operator

input_seq = ['7 2 1 10']
operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}


# def execute(nums, target, expression):
#     if len(nums) == 1:  # 剩一个数时，若相等即可拼成24点
#         if nums[0] == target:
#             expression.insert(0, str(nums[0]))
#             return True
#         return False
#     else:
#         for i in range(len(nums)):
#             sub_nums = nums[:i] + nums[i+1:]  # 取出一个数，其他三个数继续做计算
#             temp = nums[i]
#             # 一个递归完再递归第二个
#             for token, func in operators.items():
#                 expression.insert(0, str(temp))
#                 if token == '+':
#                     expression.insert(0, '-')
#                 elif token == '-':
#                     expression.insert(0, '+')
#                 elif token == '*':
#                     expression.insert(0, '/')
#                 elif token == '/':
#                     expression.insert(0, '*')
#                 if execute(sub_nums, func(target, temp), expression):
#                     print('成功: ', ''.join(expression))
#                     return True
#                 print(''.join(expression))
#                 for _ in range(2):
#                     if len(expression) > 0:
#                         expression.pop(0)
#             # if execute(sub_nums, target-temp) or execute(sub_nums, target+temp) \
#             #         or execute(sub_nums,  target*temp) or execute(sub_nums, target/temp):
#             #     # 有其中一个递归返回true就是找到答案
#             #     return True
#         return False


# def point_24(seq):
#     output_seq = []
#     for line in seq:
#         nums = [int(n) for n in line.split(' ')]
#         expression = []
#         output_seq.append('true' if execute(nums, 24, expression) else 'false')
#     for item in output_seq:
#         print(item)


def execute(nums, target):
    if len(nums) == 1:  # 剩一个数时，若相等即可拼成24点
        return nums[0] == target
    else:
        for i in range(len(nums)):
            sub_nums = nums[:i] + nums[i+1:]  # 取出一个数，其他三个数继续做计算
            temp = nums[i]
            # 一个递归完再递归第二个
            if execute(sub_nums, target-temp) or execute(sub_nums, target+temp) \
                    or execute(sub_nums,  target*temp) or execute(sub_nums, target/temp):
                # 有其中一个递归返回true就是找到答案
                return True
        return False


def point_24(seq):
    output_seq = []
    for line in seq:
        nums = [int(n) for n in line.split(' ')]
        output_seq.append('true' if execute(nums, 24) else 'false')
    for item in output_seq:
        print(item)


point_24(input_seq)
