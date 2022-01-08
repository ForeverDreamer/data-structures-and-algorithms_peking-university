"""list弹出数据性能测试"""
from timeit import Timer

l = list(range(2000000))

pop_zero = Timer('l.pop(0)', 'from __main__ import l')
print(f'pop_zero {pop_zero.timeit(number=1000)} seconds')

pop_end = Timer('l.pop()', 'from __main__ import l')
print(f'pop_end {pop_end.timeit(number=1000)} seconds')

print('pop(0)      pop()')
for num in range(1000000, 10000001, 1000000):
    l = list(range(num))
    pz = pop_zero.timeit(number=1000)
    pe = pop_end.timeit(number=1000)
    print(f'{pz:9.7f},  {pe:9.7f}')
