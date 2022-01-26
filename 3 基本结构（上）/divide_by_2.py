"""{4}--304栈的应用：十进制转换为二进制9m34s"""
from stack import StackEnd


def divide_by_2(quotient):
    remainder_stack = StackEnd()

    while quotient > 0:
        remainder = quotient % 2
        remainder_stack.push(remainder)
        quotient = quotient // 2

    bin_string = ''
    while not remainder_stack.is_empty():
        bin_string = bin_string + str(remainder_stack.pop())

    return bin_string


if __name__ == '__main__':
    print(divide_by_2(224))
