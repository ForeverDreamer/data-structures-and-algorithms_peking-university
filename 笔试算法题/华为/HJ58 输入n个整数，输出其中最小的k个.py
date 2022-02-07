"""
HJ58 输入n个整数，输出其中最小的k个

描述
输入n个整数，输出其中最小的k个整数并按升序输出

本题有多组输入样例

数据范围：1≤n≤1000  ，输入的整数满足 1≤val≤10000
输入描述：
第一行输入两个整数n和k
第二行输入一个整数数组

输出描述：
输出一个从小到大排序的整数数组

示例1
输入：
5 2
1 3 5 7 2
输出：
1 2
"""

input_seq = ['5 2', '1 3 5 7 2']


def execute(k, nums):
    nums.sort()
    print(' '.join([str(i) for i in nums[:k]]))


def min_two(seq):
    output_seq = []
    i = 0
    while i + 1 < len(seq):
        _, k = seq[i].split(' ')
        k = int(k)
        nums = [int(i) for i in seq[i+1].split(' ')]
        output_seq.append(execute(k, nums))
        i += 2


min_two(input_seq)
