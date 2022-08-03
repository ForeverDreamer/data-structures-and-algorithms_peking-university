"""{3}--703图抽象数据类型的Python实现5m26s"""


class Vertex:
    # _key = 1

    def __init__(self, payload):
        # self._key = Vertex._key
        self._key = payload['key']
        self._data = payload['data']
        self._connected_to = {}
        # Vertex._key += 1
        self._state = 'white'
        self._distance = 0
        self._previous = None

    def __str__(self):
        # return str(self._key) + ' connected to: ' + str([neighbor.key for neighbor in self.connected_to])
        nbrs = [(neighbor.key, neighbor.data) for neighbor in self.connected_to]
        return f'({self.key},{self.data}) connected to: {nbrs}'
        # neighbors = {neighbor.key: neighbor.data for neighbor in self.connected_to}
        # return f'({self._key},{self._data}) connected to: {neighbors}'
        # neighbors = [f'{neighbor.key},{neighbor.data},{neighbor.state},{neighbor.distance},{neighbor.previous}'
        #              for neighbor in self.connected_to]
        # return f'({self._key},{self._data},{self._state},{self._distance},{self._previous}) connected to: {neighbors}'

    # def __eq__(self, v):
    #     return v.data == self.data

    def add_neighbor(self, neighbor, weight=1):
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
    # _num_of_vertex = 0

    def __init__(self):
        self._vertexs = {}
        # self._num_of_vertex = 0

    def __iter__(self):
        return iter(self.vertexes)

    def __str__(self):
        sorted_data = [v for v in self]
        sorted_data.sort(key=lambda v: v.data)
        rep_str = '\n'.join([str(v) for v in sorted_data])
        return f'__str__访问\n顶点数量：{self.size}\n{rep_str}'

    def __contains__(self, key):
        return key in self._vertexs

    def add_vertex(self, payload):
        # Graph._num_of_vertex += 1
        key = payload['key']
        self._vertexs[key] = Vertex(payload)
        # self._num_of_vertex += 1
        return self._vertexs[key]

    def get_vertex(self, key):
        return self._vertexs.get(key)

    @property
    def size(self):
        return len(self._vertexs)

    @property
    def vertexes(self):
        return self._vertexs.values()

    def add_edge(self, f_payload, t_payload, weight=1):
        f_vertex = self.get_vertex(f_payload['key'])
        t_vertex = self.get_vertex(t_payload['key'])
        if f_vertex is None:
            f_vertex = self.add_vertex(f_payload)
        if t_vertex is None:
            t_vertex = self.add_vertex(t_payload)
        f_vertex.add_neighbor(t_vertex, weight)


if __name__ == '__main__':
    g = Graph()
    # for d in range(1, 7):
    #     g.add_vertex(Vertex(d))
    # for vertex in g.vertexes:
    #     print(vertex)
    g.add_edge({'key': 'v1', 'data': 1}, {'key': 'v2', 'data': 2}, 5)
    g.add_edge({'key': 'v2', 'data': 2}, {'key': 'v3', 'data': 3})
    g.add_edge({'key': 'v3', 'data': 3}, {'key': 'v4', 'data': 4}, 2)
    g.add_edge({'key': 'v4', 'data': 4}, {'key': 'v5', 'data': 5})
    g.add_edge({'key': 'v5', 'data': 5}, {'key': 'v6', 'data': 6})
    g.add_edge({'key': 'v6', 'data': 6}, {'key': 'v7', 'data': 7})
    g.add_edge({'key': 'v7', 'data': 7}, {'key': 'v8', 'data': 8})
    g.add_edge({'key': 'v1', 'data': 1}, {'key': 'v3', 'data': 3})
    g.add_edge({'key': 'v1', 'data': 1}, {'key': 'v4', 'data': 4})
    g.add_edge({'key': 'v2', 'data': 2}, {'key': 'v5', 'data': 5})
    g.add_edge({'key': 'v2', 'data': 2}, {'key': 'v6', 'data': 6})
    print(g)
    # print('迭代器访问')
    # for vertex in g:
    #     print(vertex)
