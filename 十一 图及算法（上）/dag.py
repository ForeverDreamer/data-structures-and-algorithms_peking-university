"""{3}--703图抽象数据类型的Python实现5m26s"""


class Vertex:
    # _key = 1

    def __init__(self, key, data):
        # self._key = Vertex._key
        self._key = key
        self._data = data
        self._connected_to = {}
        # Vertex._key += 1
        self._state = 'unprocessed'
        self._distance = 0
        self._previous = None

    def __str__(self):
        # return str(self._key) + ' connected to: ' + str([neighbor.key for neighbor in self.connected_to])
        # neighbors = {neighbor.key: neighbor.data for neighbor in self.connected_to}
        neighbors = [f'{neighbor.key},{neighbor.data},{neighbor.state},{neighbor.distance},{neighbor.previous}'
                     for neighbor in self.connected_to]
        return f'({self._key},{self._data},{self._state},{self._distance},{self._previous}) connected to: {neighbors}'

    # def __eq__(self, v):
    #     return v.data == self.data

    def add_neighbor(self, neighbor, weight=0):
        self._connected_to[neighbor] = weight

    @property
    def key(self):
        return self._key

    @property
    def data(self):
        return self._data

    @property
    def connected_to(self):
        return self._connected_to

    @property
    def connections(self):
        return self._connected_to.keys()

    def neighbor_weight(self, neighbor):
        return self._connected_to[neighbor]

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, s):
        self._state = s

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, dist):
        self._distance = dist

    @property
    def previous(self):
        return self._previous

    @previous.setter
    def previous(self, p):
        self._previous = p


class Graph:
    _num_of_vertex = 0

    def __init__(self):
        self._vertexs = {}
        # self._num_of_vertex = 0

    def __iter__(self):
        return iter(self._vertexs.values())

    def __str__(self):
        rep_str = '\n'.join([str(v) for v in self])
        return f'__str__访问\n{rep_str}'

    def __contains__(self, v):
        return v.key in self._vertexs

    def add_vertex(self, data):
        Graph._num_of_vertex += 1
        self._vertexs[Graph._num_of_vertex] = Vertex(Graph._num_of_vertex, data)
        # self._num_of_vertex += 1
        return self._vertexs[Graph._num_of_vertex]

    def vertex(self, data):
        for v in self.vertexes:
            if data == v.data:
                return v

    @property
    def vertexes(self):
        return self._vertexs.values()

    def add_edge(self, from_data, to_data, weight=0):
        from_vertex = self.vertex(from_data)
        to_vertex = self.vertex(to_data)
        if not from_vertex:
            from_vertex = self.add_vertex(from_data)
        if not to_vertex:
            to_vertex = self.add_vertex(to_data)
        from_vertex.add_neighbor(to_vertex, weight)


if __name__ == '__main__':
    g = Graph()
    # for d in range(1, 7):
    #     g.add_vertex(Vertex(d))
    # for vertex in g.vertexes:
    #     print(vertex)
    g.add_edge(1, 2, 5)
    g.add_edge(1, 6, 2)
    g.add_edge(2, 3, 4)
    g.add_edge(3, 4, 9)
    g.add_edge(5, 6, 7)
    g.add_edge(4, 6, 3)
    g.add_edge(5, 1, 1)
    g.add_edge(6, 5, 8)
    g.add_edge(6, 3, 1)
    print(g)
    print('迭代器访问')
    for vertex in g:
        print(vertex)
