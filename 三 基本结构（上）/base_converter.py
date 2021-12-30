"""{4}--304栈的应用：十进制转换为二进制9m34s"""
from stack import StackEnd


def base_converter(quotient, base):
    digits = '0123456789ABCDEFG'
    remainder_stack = StackEnd()

    while quotient > 0:
        remainder = quotient % base
        remainder_stack.push(remainder)
        quotient = quotient // base

    print(remainder_stack._items)
    new_string = ''
    while not remainder_stack.is_empty():
        new_string = new_string + digits[remainder_stack.pop()]

    return new_string


if __name__ == '__main__':
    print(base_converter(25, 2))
    print(base_converter(25, 16))
