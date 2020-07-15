"""骑士周游问题"""
from dag import Graph


def legal_coordinate(coordinate, board_size):
    return True if 0 <= coordinate < board_size else False


def generate_legal_moves(x, y, board_size):
    legal_moves = []
    move_off_sets = ((-1, -2), (-1, 2), (-2, -1), (-2, 1), (1, -2), (1, 2), (2, -1), (2, 1))

    for off_set in move_off_sets:
        new_x = x + off_set[0]
        new_y = y + off_set[1]
        if legal_coordinate(new_x, board_size) and legal_coordinate(new_y, board_size):
            legal_moves.append((new_x, new_y))

    return legal_moves


def coordinate_to_vertex_key(x, y, board_size):
    return y*board_size+x


def knight_graph(board_size):
    g = Graph()
    for y in range(board_size):
        for x in range(board_size):
            vertex_key1 = coordinate_to_vertex_key(x, y, board_size)
            legal_coordinates = generate_legal_moves(x, y, board_size)
            for coordinates in legal_coordinates:
                vertex_key2 = coordinate_to_vertex_key(coordinates[0], coordinates[1], board_size)
                g.add_edge(vertex_key1, vertex_key2)
    return g


def trace_path(path):
    p_str = []
    for v in path:
        p_str.extend([str(v.data), ' -> '])
    # print(f'路径长度：{len(p[1:])}')
    print(''.join(p_str[:-1]))


def knight_tour(level, path, current, limit):
    current.state = 'processing'
    path.append(current)
    trace_path(path)
    if level < limit:
        neighbors = list(current.connections)
        i = 0
        done = False
        while i < len(neighbors) and not done:
            if neighbors[i].state == 'unprocessed':
                done = knight_tour(level+1, path, neighbors[i], limit)
            i += 1
        # Prepare to backtrack
        if not done:
            path.pop()
            current.state = 'unprocessed'
    else:
        done = True
    return done


def order_by_avail(n):
    res_list = []
    for v in n.connections:
        if v.state == 'unprocessed':
            c = 0
            for w in v.connections:
                if w.state == 'unprocessed':
                    c += 1
            res_list.append((c, v))
    res_list.sort(key=lambda x: x[0])
    return [y[1] for y in res_list]


if __name__ == '__main__':
    kg = knight_graph(5)
    print(kg._num_of_vertex)
    print(kg)
    p = []
    knight_tour(0, p, kg.vertex(0), 24)
    # p_str = []
    # for v in p:
    #     p_str.extend([str(v.data), ' -> '])
    # print(f'路径长度：{len(p[1:])}')
    # print(''.join(p_str[:-1]))
