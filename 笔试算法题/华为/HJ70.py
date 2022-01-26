"""
HJ70 矩阵乘法计算量估算

描述
矩阵乘法的运算量与矩阵乘法的顺序强相关。
例如：

A是一个50×10的矩阵，B是10×20的矩阵，C是20×5的矩阵

计算A*B*C有两种顺序：（（AB）C）或者（A（BC）），前者需要计算15000次乘法，后者只需要3500次。

编写程序计算不同的计算顺序需要进行的乘法次数。

本题含有多组样例输入！
数据范围：数据组数：1≤t≤10 ，矩阵个数：1≤n≤15 ，行列数：1≤row_i,col_i≤100
进阶：时间复杂度：O(n) ，空间复杂度：O(n)

输入描述：
输入多行，先输入要计算乘法的矩阵个数n，每个矩阵的行数，列数，总共2n的数，最后输入要计算的法则
计算的法则为一个字符串，仅由左右括号和大写字母（'A'~'Z'）组成，保证括号是匹配的且输入合法！

输出描述：
输出需要进行的乘法次数

示例1
输入：
3
50 10
10 20
20 5
(A(BC))
输出：
3500
"""

from string import ascii_uppercase

input_seq = [
    '3', '50 10', '10 20', '20 5', '(A(BC))',
]


def execute(matrixes, order):
    for c in order:
        # 通过tree的全括号表达式解析算法解析计算顺序
        pass


def matrix_multiplication_computation(seq):
    i = 0
    while i < len(seq):
        n = int(seq[i])
        matrixes = []
        for j in range(i+1, i+1+n):
            matrixes.append([int(n) for n in seq[j].split(' ')])
        order = seq[i+1+n]
        execute(matrixes, order)
        i += 2+n


matrix_multiplication_computation(input_seq)