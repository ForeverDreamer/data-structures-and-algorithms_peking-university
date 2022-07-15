"""{4}--304栈的应用：十进制转换为二进制9m34s"""
from stack import StackEnd


def divide_by_2(quotient):
    s = StackEnd()

    while quotient > 0:
        s.push(quotient % 2)
        quotient = quotient // 2

    bin_string = ''
    while not s.is_empty():
        bin_string = bin_string + str(s.pop())

    return bin_string


if __name__ == '__main__':
    print(divide_by_2(224))
