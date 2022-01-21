"""HJ44 Sudoku
描述
问题描述：数独（Sudoku）是一款大众喜爱的数字逻辑游戏。玩家需要根据9X9盘面上的已知数字，推算出所有剩余空格的数字，并且满足每一行、每一列、每一个3X3粗线宫内的数字均含1-9，并且不重复。
例如：
输入

输出


数据范围：输入一个 9*9 的矩阵
输入描述：
包含已知数字的9X9盘面数组[空缺位以数字0表示]

输出描述：
完整的9X9盘面数组

示例1
输入：
0 9 2 4 8 1 7 6 3
4 1 3 7 6 2 9 8 5
8 6 7 3 5 9 4 1 2
6 2 4 1 9 5 3 7 8
7 5 9 8 4 3 1 2 6
1 3 8 6 2 7 5 9 4
2 7 1 5 3 8 6 4 9
3 8 6 9 1 4 2 5 7
0 4 5 2 7 6 8 3 1
输出：
5 9 2 4 8 1 7 6 3
4 1 3 7 6 2 9 8 5
8 6 7 3 5 9 4 1 2
6 2 4 1 9 5 3 7 8
7 5 9 8 4 3 1 2 6
1 3 8 6 2 7 5 9 4
2 7 1 5 3 8 6 4 9
3 8 6 9 1 4 2 5 7
9 4 5 2 7 6 8 3 1
"""

input_seq = [
    '0 9 5 0 2 0 0 6 0',
    '0 0 7 1 0 3 9 0 2',
    '6 0 0 0 0 5 3 0 4',
    '0 4 0 0 1 0 6 0 7',
    '5 0 0 2 0 7 0 0 9',
    '7 0 3 0 9 0 0 2 0',
    '0 0 9 8 0 0 0 0 6',
    '8 0 6 3 0 2 1 0 5',
    '0 5 0 0 7 0 2 8 3',
]

g_size = 9
sub_size = 3


# 同行同列同3*3方阵是否已存在n
def is_legal(data, row, col, n):
    # 所在行
    for c in range(g_size):
        if data[row][c] == n:
            return False
    # 所在列
    for r in range(g_size):
        if data[r][col] == n:
            return False

    # 所在3*3方阵
    def get_start(idx):
        if idx < sub_size:
            return 0
        elif idx < 2*sub_size:
            return 3
        else:
            return 6

    start_row = get_start(row)
    start_col = get_start(col)
    r = start_row
    while r < start_row+3:
        c = start_col
        while c < start_col + 3:
            if data[r][c] == n:
                return False
            c += 1
        r += 1

    return True


def find_zero(data, row, col):
    while row < g_size and col < g_size:
        if data[row][col] == '0':
            return row, col
        col += 1
        if col == 9:
            col = 0
            row += 1
    return None


fail_count = 0


def dst(data, path, row, col):
    if col == g_size:
        col %= g_size
        row += 1
    # 如果没有0点了，则表示完成了填充
    zero_pos = find_zero(data, row, col)
    if zero_pos is None:
        print(f'成功路径：{path}')
        return True
    zero_row, zero_col = zero_pos
    # 从1开始赋值，若填写某个数值后，其他0点位置无法找到合适值，则数值递进再次尝试
    n = 1
    while n <= g_size:
        if is_legal(data, zero_row, zero_col, str(n)):
            data[zero_row][zero_col] = str(n)
            path.append(f'({zero_row},{zero_col}): {str(n)}')
            done = dst(data, path, zero_row, zero_col)
            if done:
                return True
        n += 1
    # 若没有合适值，将当前位置置0，返回false，使上个填充数据再更换其他数值尝试
    global fail_count
    fail_count += 1
    print(f'失败次数：{fail_count}, 路径：{path}')
    data[row][col] = '0'
    path.pop()
    return False


def sudoku(seq):
    data = []
    for row in seq:
        data.append(row.split(' '))
    path = []
    dst(data, path, 0, 0)
    for row in data:
        print(' '.join(row))


sudoku(input_seq)
