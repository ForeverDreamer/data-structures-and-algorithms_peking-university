"""HJ35 蛇形矩阵

描述
蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。

例如，当输入5时，应该输出的三角形为：

1 3 6 10 15
2 5 9 14
4 8 13
7 12
11


请注意本题含有多组样例输入。

输入描述：
输入正整数N（N不大于100）

输出描述：
输出一个N行的蛇形矩阵。

示例1
输入：
4
输出：
1 3 6 10
2 5 9
4 8
7
"""

input_seq = ['41', '17']


def sort_by_ascii(seq):
    output_seq = []
    for num_str in seq:
        n = int(num_str)
        len_row = n
        i_y = 0
        previous_y = 1
        step_y = 1
        while i_y < n:
            i_x = len_row-1
            previous_x = previous_y
            step_x = 2+i_y
            row = []
            row.append(str(previous_x))
            while i_x > 0:
                row.append(str(previous_x+step_x))
                previous_x = previous_x+step_x
                step_x += 1
                i_x -= 1
            output_seq.append(' '.join(row))
            previous_y = previous_y + step_y
            step_y += 1
            i_y += 1
            len_row -= 1

    return output_seq


for item in sort_by_ascii(input_seq):
    print(item)
