"""
HJ17 坐标移动

描述
开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。

输入：

合法坐标为A(或者D或者W或者S) + 数字（两位以内）

坐标之间以;分隔。

非法坐标点需要进行丢弃。如AA10;  A1A;  $%$;  YAD; 等。

下面是一个简单的例子 如：

A10;S20;W10;D30;X;A1A;B10A11;;A10;

处理过程：

起点（0,0）

+   A10   =  （-10,0）

+   S20   =  (-10,-20)

+   W10  =  (-10,-10)

+   D30  =  (20,-10)

+   x    =  无效

+   A1A   =  无效

+   B10A11   =  无效

+  一个空 不影响

+   A10  =  (10,-10)

结果 （10， -10）

数据范围：每组输入的字符串长度满足  ，坐标保证满足  ，且数字部分仅含正数

注意请处理多组输入输出

输入描述：
一行字符串

输出描述：
最终坐标，以逗号分隔

示例1
输入：
A10;S20;W10;D30;X;A1A;B10A11;;A10;
输出：
10,-10

示例2
输入：
ABC;AKL;DA1;
输出：
0,0
"""

input_str = 'A10;S20;W10;D30;X;A1A;B10A11;;A10;'
legal_directions = ('A', 'D', 'W', 'S')


def validate_coordinates(seq):
    legal_moves = []

    for s in seq:
        if len(s) < 2:
            continue
        direction = s[0]
        if direction not in legal_directions:
            continue
        try:
            offset = int(s[1:])
            if offset <= 0:
                continue
        except ValueError:
            continue
        legal_moves.append(s)

    return legal_moves


def move(coordinates):
    x = 0
    y = 0

    for coordinate in coordinates:
        direction = coordinate[0]
        offset = int(coordinate[1:])
        if direction == 'A':
            x -= offset
        elif direction == 'D':
            x += offset
        elif direction == 'W':
            y += offset
        else:
            y -= offset

    return str(x)+','+str(y)


def coordinates_move(seq):
    coordinates = validate_coordinates(seq.split(';'))
    return move(coordinates)


print(coordinates_move(input_str))
