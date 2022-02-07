"""
HJ55 挑7

描述
输出小于等于 n 的与 7 有关数字的个数，包括 7 的倍数，还有包含 7 的数字（如 17 ，27 ，37 ... 70 ，71 ，72 ，73...）的个数（一组测试用例里可能有多组数据，请注意处理）

数据范围： 1≤n≤30000

本题有多组输入
输入描述：
多组输入每组输入 1 个正整数 n 。( n 不大于 30000 )

输出描述：
不大于n的与7有关的数字个数，例如输入20，与7有关的数字包括7,14,17.

示例1
输入：
20
10
输出：
3
1
"""

input_seq = ['20', '10']


def execute(n):
    count = 0
    for i in range(1, n+1):
        if i % 7 == 0 or '7' in str(i):
            # print(i)
            count += 1
    return count


def pick_seven(seq):
    output_seq = []
    for n in seq:
        output_seq.append(execute(int(n)))
    # print('----------------------')
    for item in output_seq:
        print(item)


pick_seven(input_seq)
