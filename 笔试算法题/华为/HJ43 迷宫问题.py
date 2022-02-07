"""
HJ43 迷宫问题

描述
定义一个二维数组 N*M ，如 5 × 5 数组下所示：


int maze[5][5] = {
0, 1, 0, 0, 0,
0, 1, 1, 1, 0,
0, 0, 0, 0, 0,
0, 1, 1, 1, 0,
0, 0, 0, 1, 0,
};


它表示一个迷宫，其中的1表示墙壁，0表示可以走的路，只能横着走或竖着走，不能斜着走，要求编程序找出从左上角到右下角的路线。入口点为[0,0],既第一格是可以走的路。


本题含有多组数据。

数据范围： 2≤n,m≤10  ， 输入的内容只包含 0≤val≤1

输入描述：
输入两个整数，分别表示二维数组的行数，列数。再输入相应的数组，其中的1表示墙壁，0表示可以走的路。数据保证有唯一解,不考虑有多解的情况，即迷宫只有一条通道。

输出描述：
左上角到右下角的最短路径，格式如样例所示。

示例1
输入：
5 5
0 1 0 0 0
0 1 1 1 0
0 0 0 0 0
0 1 1 1 0
0 0 0 1 0
输出：
(0,0)
(1,0)
(2,0)
(2,1)
(2,2)
(2,3)
(2,4)
(3,4)
(4,4)

示例2
输入：
5 5
0 1 0 0 0
0 1 0 1 0
0 0 0 0 1
0 1 1 1 0
0 0 0 0 0
输出：
(0,0)
(1,0)
(2,0)
(3,0)
(4,0)
(4,1)
(4,2)
(4,3)
(4,4)

说明：
注意：不能斜着走！！
"""

input_seq = [
    '3 2', '0 1', '0 1', '0 0',
    # '5 5', '0 1 0 0 0', '0 1 1 1 0', '0 0 0 0 0', '0 1 1 1 0', '0 0 0 1 0',
    # '5 5', '0 1 0 0 0', '0 1 0 1 0', '0 0 0 0 1', '0 1 1 1 0', '0 0 0 0 0',
]


offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
g_row = 0
g_col = 0
g_data = []


def move(pos, offset):
    r = pos[0]+offset[0]
    c = pos[1]+offset[1]
    if (r < 0 or c < 0) or (c >= g_col or r >= g_row) or g_data[r][c] == '1':
        return None
    return r, c


def bfs(maze_map, start):
    queue = [start]
    while len(queue) > 0:
        current = queue.pop(0)
        i = 0
        while i < len(offsets):
            new_pos = move(current['pos'], offsets[i])
            # 超出迷宫范围
            if not new_pos:
                i += 1
                continue
            r, c = new_pos
            nbr = maze_map[r][c]
            if nbr['stage'] == '0':
                nbr['stage'] = '1'
                nbr['distance'] = current['distance'] + 1
                nbr['previous'] = current
                queue.append(nbr)
            i += 1
            # path.append(new_pos)
        current['stage'] = '2'
    traverse(maze_map[g_row-1][g_col-1])


def traverse(dest):
    output_seq = []
    while dest['previous']:
        output_seq.append(dest['pos'])
        dest = dest['previous']
    output_seq.append(dest['pos'])
    for pos in output_seq[::-1]:
        print(f'({str(pos[0])},{str(pos[1])})')


def maze(seq):
    output_seq = []

    i = 0
    while i < len(seq):
        row, col = seq[i].split(' ')
        global g_row
        global g_col
        g_row, g_col = int(row), int(col)
        global g_data
        r = i+1
        while r <= i+g_row:
            g_data.append(seq[r].split(' '))
            r += 1
        maze_map = []
        for r in range(g_row):
            maze_map.append([{'pos': (r, c), 'stage': '0', 'previous': None, 'distance': 0} for c in range(g_col)])
        output_seq.append(bfs(maze_map, maze_map[0][0]))
        maze_map.clear()
        g_data.clear()
        i += g_row+1
    return output_seq


maze(input_seq)
# for item in maze(input_seq):
#     print(item)
