
import time


def sum_of_n3(n):
    start = time.time()
    total = (n * (n + 1)) / 2
    end = time.time()
    return total, end - start


for i in range(5):
    total, elapse = sum_of_n3(1000000000000000000000000000000000000000000000000000000000000000000000000000)
    print(f'Sum is {total}, required {elapse:.100f} seconds')