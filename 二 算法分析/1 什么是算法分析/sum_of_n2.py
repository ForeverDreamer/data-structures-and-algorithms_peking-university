import time


def sum_of_n2(n):
    start = time.time()
    total = 0
    for i in range(1, n + 1):
        total += i
    end = time.time()
    return total, end - start


for i in range(5):
    total, elapse = sum_of_n2(10000)
    print(f'Sum is {total}, required {elapse:.7f} seconds')