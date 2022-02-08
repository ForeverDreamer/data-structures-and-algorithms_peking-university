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

解题思路：
A是一个50×10的矩阵，B是10×20的矩阵，C是20×5的矩阵
1.计算量：((AB)C) = 50*10*20 + 50*20*5 = 15000
                 (A(BC)) = 50*10*5 + 10*20*5 = 3500
2.使用二叉树进行计算顺序解析和计算
"""

from string import ascii_uppercase

input_seq = [
    # '3', '50 10', '10 20', '20 5', '((AB)C)',
    '3', '50 10', '10 20', '20 5', '(A(BC)',
]


class BTNode:
    def __init__(self, v):
        self._data = v
        self._left = None
        self._right = None

    def insert_left(self, v):
        if self._left is None:
            self._left = BTNode(v)
        else:
            t = BTNode(v)
            t._left = self._left
            self._left = t

    def insert_right(self, v):
        if self._right is None:
            self._right = BTNode(v)
        else:
            t = BTNode(v)
            t._right = self._right
            self._right = t

    def preorder(self):
        print(self._data)
        if self._left:
            self._left.preorder()
        if self._right:
            self._right.preorder()

    def inorder(self):
        if self._left:
            self._left.inorder()
        print(self._data)
        if self._right:
            self._right.inorder()

    def postorder(self):
        if self._left:
            self._left.postorder()
        if self._right:
            self._right.postorder()
        print(self._data)

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, v):
        self._data = v


# 通过tree的全括号表达式解析算法解析计算顺序
def build_parse_tree(expression):
    exp_list = list(expression)
    parse_stack = []
    root_node = BTNode('')
    parse_stack.append(root_node)
    current_node = root_node

    i = 0
    while i < len(exp_list):
        token = exp_list[i]
        if token == '(':
            current_node.insert_left('')
            parse_stack.append(current_node)
            current_node = current_node.left
        elif token == ')':
            current_node = parse_stack.pop()
            try:
                if exp_list[i+1] != ')':
                    current_node.insert_right('')
                    parse_stack.append(current_node)
                    current_node = current_node.right
            except IndexError:
                pass
        else:
            current_node.data = token
            current_node = parse_stack.pop()
            # current_node.data = token
            try:
                if exp_list[i+1] != ')':
                    current_node.insert_right('')
                    parse_stack.append(current_node)
                    current_node = current_node.right
            except IndexError:
                pass
        i += 1
    return root_node


def evaluate(node, matrixes, total):
    left = node.left
    right = node.right

    if left and right:
        left_arr = evaluate(left, matrixes, total)
        right_arr = evaluate(right, matrixes, total)
        total[0] += left_arr[0] * right_arr[0] * right_arr[1]
        return [left_arr[0], right_arr[1]]
    else:
        return matrixes[node.data]


def restore_exp(node):
    exp = ''
    if node.left and node.right:
        exp = '(' + restore_exp(node.left)
        exp += str(node.data)
        exp += restore_exp(node.right) + ')'
    else:
        exp += str(node.data)

    return exp


def execute(matrixes, expression):
    node = build_parse_tree(expression)
    # node.preorder()
    # print('---------------------------')
    # node.inorder()
    # print('---------------------------')
    # node.postorder()
    # print('---------------------------')
    print(restore_exp(node))
    total = [0]
    evaluate(node, matrixes, total)
    print(total[0])


def matrix_multiplication_computation(seq):
    i = 0
    while i < len(seq):
        n = int(seq[i])
        matrixes = {}
        count = 0
        for j in range(i+1, i+1+n):
            matrixes[ascii_uppercase[count]] = [int(n) for n in seq[j].split(' ')]
            count += 1
        expression = seq[i+1+n]
        execute(matrixes, expression)
        i += 2+n


matrix_multiplication_computation(input_seq)
