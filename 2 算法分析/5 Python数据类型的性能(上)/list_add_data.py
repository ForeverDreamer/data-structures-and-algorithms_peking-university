"""list插入数据性能测试"""
from timeit import Timer


def test1():
    l = []
    for i in range(1000):
        l += [i]


def test2():
    l = []
    for i in range(1000):
        l.append(i)


def test3():
    l = [i for i in range(1000)]


def test4():
    l = list(range(1000))


t1 = Timer('test1()', 'from __main__ import test1')
print(f'concat {t1.timeit(number=1000)} seconds')

t2 = Timer('test2()', 'from __main__ import test2')
print(f'append {t2.timeit(number=1000)} seconds')

t3 = Timer('test3()', 'from __main__ import test3')
print(f'comprehension {t3.timeit(number=1000)} seconds')

t4 = Timer('test4()', 'from __main__ import test4')
print(f'list range {t4.timeit(number=1000)} seconds')

