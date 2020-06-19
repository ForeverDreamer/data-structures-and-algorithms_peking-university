"""{2}--309队列的应用：热土豆7m52s"""
from queue import Queue


def hot_potato(name_list, times):
    name_queue = Queue()
    for name in name_list:
        name_queue.enqueue(name)
    while name_queue.size() > 1:
        for i in range(times):
            name_queue.enqueue(name_queue.dequeue())
        name_queue.dequeue()
    return name_queue.dequeue()


if __name__ == '__main__':
    print(hot_potato(['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'], 7))
