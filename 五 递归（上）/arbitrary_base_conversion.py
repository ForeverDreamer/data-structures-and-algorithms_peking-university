"""{2}--402递归的应用：任意进制转换6m32s"""

token_table = '0123456789ABCDEF'


def arbitrary_base_conversion(quotient, base):
    if quotient < base:
        return token_table[quotient]
    else:
        return arbitrary_base_conversion(quotient // base, base) + token_table[quotient % base]


if __name__ == '__main__':
    print(arbitrary_base_conversion(1453, 16))
