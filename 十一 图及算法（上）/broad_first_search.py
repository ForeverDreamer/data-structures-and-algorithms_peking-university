"""广度优先搜索算法"""
from my_queue import MyQueue
from word_ladder import build_graph


def bfs(start):
    # start.distance = 0
    # start.previous = None
    vertex_queue = MyQueue()
    vertex_queue.enqueue(start)
    while vertex_queue.size() > 0:
        current = vertex_queue.dequeue()
        for nbr in current.connections:
            if nbr.state == 'unprocessed':
                nbr.state = 'processing'
                nbr.distance = current.distance + 1
                nbr.previous = current
                vertex_queue.enqueue(nbr)
        current.state = 'processed'


def traverse(dest):
    while dest.previous:
        print(dest.data)
        dest = dest.previous
    print(dest.data)


if __name__ == '__main__':
    g = build_graph('words_bfs.txt')
    # print(g)
    bfs(g.vertex('fool'))
    traverse(g.vertex('sage'))
