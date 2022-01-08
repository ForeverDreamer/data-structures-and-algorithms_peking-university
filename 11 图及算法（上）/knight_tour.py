"""骑士周游问题"""
import os

from dag import Graph


def legal_coordinate(coordinate, board_size):
    return True if 0 <= coordinate < board_size else False


move_off_sets = ((-1, -2), (-1, 2), (-2, -1), (-2, 1), (1, -2), (1, 2), (2, -1), (2, 1))


def generate_legal_moves(x, y, board_size):
    legal_moves = []

    for off_set in move_off_sets:
        new_x = x + off_set[0]
        new_y = y + off_set[1]
        if legal_coordinate(new_x, board_size) and legal_coordinate(new_y, board_size):
            legal_moves.append((new_x, new_y))

    return legal_moves


def coordinate_to_vertex(x, y, board_size):
    return str(x)+str(y), y*board_size+x


def knight_graph(board_size):
    g = Graph()
    for y in range(board_size):
        for x in range(board_size):
            key1, data1 = coordinate_to_vertex(x, y, board_size)
            legal_coordinates = generate_legal_moves(x, y, board_size)
            for coordinates in legal_coordinates:
                key2, data2 = coordinate_to_vertex(coordinates[0], coordinates[1], board_size)
                g.add_edge({'key': key1, 'data': data1}, {'key': key2, 'data': data2})
    return g


def trace_path(path):
    p_str = []
    for v in path:
        p_str.extend([str(v.key), ' -> '])
    print(f'路径长度：{len(path)-1}, 失败次数：{fail_count}')
    print(''.join(p_str[:-1]))
    # filename = 'kt.log'
    # try:
    #     os.remove(filename)
    # except OSError:
    #     pass
    # with open(filename, 'at', encoding='utf-8') as wf:
    #     wf.write(f'路径长度：{len(path)-1}, 失败次数：{fail_count}\n{"".join(p_str[:-1])}\n')


fail_count = 0


def knight_tour(level, path, current, limit):
    current.state = 'gray'
    path.append(current)
    if level < limit:
        neighbors = list(current.connections)
        # 按可选择走法升序排序，即先搜索四周，再搜索中间
        # neighbors = order_by_avail(current)
        i = 0
        done = False
        while i < len(neighbors) and not done:
            if neighbors[i].state == 'white':
                done = knight_tour(level+1, path, neighbors[i], limit)
            i += 1
        # Prepare to backtrack
        if not done:
            global fail_count
            fail_count += 1
            trace_path(path)
            path.pop()
            current.state = 'white'
    else:
        done = True
    return done


def order_by_avail(n):
    res_list = []
    for v in n.connections:
        if v.state == 'white':
            c = 0
            for w in v.connections:
                if w.state == 'white':
                    c += 1
            res_list.append((c, v))
    res_list.sort(key=lambda x: x[0])
    return [y[1] for y in res_list]


if __name__ == '__main__':
    kg = knight_graph(5)
    print(kg)
    print('---------------------------------')
    p = []
    # knight_tour(0, p, kg.get_vertex('00'), 24)
    # trace_path(p)
    # print('---------------------------------')
    # p.clear()
    # knight_tour(0, p, kg.get_vertex('01'), 24)
    # trace_path(p)
    # print('---------------------------------')
    # p.clear()
    # knight_tour(0, p, kg.get_vertex('02'), 24)
    # trace_path(p)
    # print('---------------------------------')
    p.clear()
    knight_tour(0, p, kg.get_vertex('04'), 24)
    trace_path(p)
    print('---------------------------------')
    # p_str = []
    # for v in p:
    #     p_str.extend([str(v.data), ' -> '])
    # print(f'路径长度：{len(p[1:])}')
    # print(''.join(p_str[:-1]))
