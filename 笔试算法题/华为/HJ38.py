"""
HJ38 求小球落地5次后所经历的路程和第5次反弹的高度

描述
假设一个球从任意高度自由落下，每次落地后反跳回原高度的一半; 再落下, 求它在第5次落地时，共经历多少米?第5次反弹多高？

最后的误差判断是小数点6位


数据范围：输入的小球初始高度满足 1≤n≤1000  ，且保证是一个整数

输入描述：
输入起始高度，int型

输出描述：
分别输出第5次落地时，共经过多少米第5次反弹多高

示例1
输入：
1
输出：
2.875
0.03125
"""

input_seq = ['1']


def execute(n):
    distance = 0
    i = 1
    while i <= 5:
        # 落下高度
        distance += n
        n /= 2
        # 最后一次不计算弹回高度
        if i == 5:
            break
        # 弹回高度
        distance += n
        i += 1

    return distance, n


def bounce_height(seq):
    output_seq = []
    for n in seq:
        n = int(n)
        result = execute(n)
        output_seq.append(result[0])
        output_seq.append(result[1])
    return output_seq


for item in bounce_height(input_seq):
    print(item)
