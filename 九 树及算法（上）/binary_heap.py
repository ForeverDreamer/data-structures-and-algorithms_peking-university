"""二叉堆"""


class BinHeap:
    def __init__(self):
        self._heap_list = [0]
        self._current_size = 0

    def float_up(self, pos):
        while pos//2 > 0:
            if self._heap_list[pos] < self._heap_list[pos//2]:
                self._heap_list[pos//2], self._heap_list[pos] = self._heap_list[pos], self._heap_list[pos//2]
            else:
                break
            pos //= 2

    def insert(self, data):
        self._heap_list.append(data)
        self._current_size += 1
        self.float_up(self._current_size)

    def min_child(self, pos):
        if pos*2+1 > self._current_size:
            return pos*2
        else:
            pos*2 if self._heap_list[pos*2] < self._heap_list[pos*2+1] else pos*2+1

    def sink_down(self, pos):
        while pos*2 <= self._current_size:
            mc = self.min_child(pos)
            if self._heap_list[pos] > self._heap_list[mc]:
                self._heap_list[pos], self._heap_list[mc] = self._heap_list[mc], self._heap_list[pos]
            pos = mc

    def del_min(self):
        min_val = self._heap_list[1]
        self._heap_list[1] = self._heap_list[self._current_size]
        self._current_size -= 1
        self._heap_list.pop()
        self.sink_down(1)

        return min_val

    def build_heap(self, items):
        pos = len(items) // 2
        self._current_size = len(items)
        self._heap_list = [0] + items[:]
        print(len(self._heap_list), pos)
        while pos > 0:
            print(len(self._heap_list), pos)
            self.sink_down(pos)
            pos -= 1
        print(len(self._heap_list), pos)
