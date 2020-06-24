"""{3}--703图抽象数据类型的Python实现5m26s"""


class Vertex:
    _key = 1

    def __init__(self, data):
        self._key = Vertex._key
        self._data = data
        self._connected_to = {}
        Vertex._key += 1

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

    def weight(self, neighbor):
        return self._connected_to[neighbor]

    def __str__(self):
        return str(self._key) + ' connected to: ' + str([neighbor.key for neighbor in self.connected_to])


class Graph:
    def __init__(self):
        self._vertexs = {}
        self._num_of_vertex = 0

    def __contains__(self, key):
        return key in self._vertexs

    def _iter__(self):
        return iter(self._vertexs.values())

    def add_vertex(self, v):
        self._vertexs[v.key] = v
        self._num_of_vertex += 1
        return v

    def vertex(self, key):
        return self._vertexs.get(key)

    def add_edge(self, from_vertex, to_vertex, weight=0):
        if from_vertex not in self._vertexs:
            self.add_vertex(from_vertex)
        if to_vertex not in self._vertexs:
            self.add_vertex(to_vertex)
        from_vertex.add_neighbor(to_vertex, weight)

    @property
    def vertexes(self):
        return self._vertexs.values()
