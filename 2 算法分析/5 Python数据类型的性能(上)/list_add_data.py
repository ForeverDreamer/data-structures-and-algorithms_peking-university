"""list插入数据性能测试"""
from timeit import Timer


def gen_list1():
    l = []
    for i in range(1000):
        l += [i]


def gen_list2():
    l = []
    for i in range(1000):
        l.append(i)


def gen_list3():
    l = [i for i in range(1000)]


def gen_list4():
    l = list(range(1000))


num = 10000

t1 = Timer('gen_list1()', 'from __main__ import gen_list1')
print(f'concat {t1.timeit(number=num)} seconds')

t2 = Timer('gen_list2()', 'from __main__ import gen_list2')
print(f'append {t2.timeit(number=num)} seconds')

t3 = Timer('gen_list3()', 'from __main__ import gen_list3')
print(f'comprehension {t3.timeit(number=num)} seconds')

t4 = Timer('gen_list4()', 'from __main__ import gen_list4')
print(f'list range {t4.timeit(number=num)} seconds')

