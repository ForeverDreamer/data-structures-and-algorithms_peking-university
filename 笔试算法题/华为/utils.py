import sys


def input_one():
    return input().strip()


def input_many():
    input_seq = []
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        input_seq.append(line)

    return input_seq


# import sys
#
#
# input_seq = []
# while True:
#     line = sys.stdin.readline().strip()
#     if line == '':
#         break
#     input_seq.append(line)
