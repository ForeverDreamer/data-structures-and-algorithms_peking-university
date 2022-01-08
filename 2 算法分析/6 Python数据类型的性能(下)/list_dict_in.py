"""list和dict的in 操作对比"""
from timeit import Timer
import random

for num in range(10000, 100001, 10000):
    t = Timer(f'random.randrange({num}) in l', 'from __main__ import random, l')
    l = list(range(num))
    list_time = t.timeit(number=1000)
    l = {k: None for k in range(num)}
    dict_time = t.timeit(number=1000)
    print(f'{num}, {list_time:9.7f}, {dict_time:9.7f}')
