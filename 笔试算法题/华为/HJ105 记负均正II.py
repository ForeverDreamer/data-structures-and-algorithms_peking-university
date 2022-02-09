"""
HJ105 记负均正II

描述
输入 n 个整型数，统计其中的负数个数并求所有非负数的平均值，结果保留一位小数，如果没有非负数，则平均值为0
本题有多组输入数据，输入到文件末尾。

数据范围：1≤n≤50000  ，其中每个数都满足 ∣val∣≤10
6

输入描述：
输入任意个整数，每行输入一个。

输出描述：
输出负数个数以及所有非负数的平均值

示例1
输入：
-13
-4
-7
复制
输出：
3
0.0
复制
示例2
输入：
-12
1
2
复制
输出：
1
1.5
"""

# 代码1
#这个题需要注意对文件结束的处理。以往的题目都是有确定数量的输入，可以在try里按既定数量获取input()，这一题是不定长的输出，只能判断文件结束符。方法见except

p_l = []
n_l = []

while True:
    try:
        i = int(input())
        if i >= 0:
            p_l.append(i)
        else:
            n_l.append(i)
    except EOFError:  ###重点重点重点，在python中对文件结束符的判断，可以用except EOFError来获取。没有碰到结束符之前，只记录输入，碰到结束符之后，处理输出。
        print(len(n_l))
        if len(p_l)>0:
            print(round(sum(p_l)/len(p_l),1))
        else:
            print('0.0')
        break


# 代码2
arr1 = []
arr2 = []
while True:
    try:
        n = int(input())
        if n > 0:
            arr1.append(n)
        else:
            arr2.append(n)
    except:
        print(len(arr2))
        if len(arr1) == 0:
            print('%.1f' % len(arr1))
        else:
            print('%.1f' % (sum(arr1) / len(arr1)))
        break
