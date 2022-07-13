"""list和dict的in 操作对比"""
from timeit import Timer
import random

for num in range(10000, 100001, 10000):
    t = Timer(f'random.randrange({num}) in data', 'from __main__ import random, data')
    data = list(range(num))
    list_time = t.timeit(number=1000)
    data = {k: None for k in range(num)}
    dict_time = t.timeit(number=1000)
    print(f'{num}, {list_time:9.7f}, {dict_time:9.7f}')
