"""二叉堆"""


class BinHeap:
    def __init__(self):
        self._heap_list = [0]
        self._current_size = 0

    def __str__(self):
        return f'{self._heap_list[1:]}'
    #     rep_strs = ['  ', str(self._heap_list[1])]
    #     for pos in range(2, len(self._heap_list), 2):
    #         rep_strs.extend(self.visualize_sub_tree(pos, pos+1))
    #     return ''.join(rep_strs)
    #
    # def visualize_sub_tree(self, left_child_pos, right_child_pos):
    #     if left_child_pos*2+1 <= self._current_size:
    #         return self.visualize_sub_tree(left_child_pos * 2, left_child_pos * 2 + 1)
    #     else:
    #         if right_child_pos//2 < self._current_size:
    #             rep_strs = ['  ', '\n', '  ', '/', '\\', '\n', ' ', str(self._heap_list[left_child_pos//2]), ' ',
    #                         str(self._heap_list[right_child_pos//2])]
    #         else:
    #             rep_strs = ['  ', '\n', '  ', '/', '\\', '\n', ' ', str(self._heap_list[left_child_pos//2]), ' ']
    #         return rep_strs

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
            return pos*2 if self._heap_list[pos*2] < self._heap_list[pos*2+1] else pos*2+1

    def sink_down(self, pos):
        while pos*2 <= self._current_size:
            mc_pos = self.min_child(pos)
            if self._heap_list[pos] > self._heap_list[mc_pos]:
                self._heap_list[pos], self._heap_list[mc_pos] = self._heap_list[mc_pos], self._heap_list[pos]
            else:
                break
            pos = mc_pos

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
        while pos > 0:
            self.sink_down(pos)
            pos -= 1


if __name__ == '__main__':
    bin_heap = BinHeap()
    bin_heap.build_heap([27, 17, 33, 21, 19, 18, 14, 11, 9, 5])
    # print(bin_heap._heap_list[1:])
    print(bin_heap)
