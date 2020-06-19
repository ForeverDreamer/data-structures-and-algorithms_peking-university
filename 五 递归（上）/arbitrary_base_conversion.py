"""{2}--402递归的应用：任意进制转换6m32s"""


def arbitrary_base_conversion(quotient, base):
    token_table = '0123456789ABCDEF'
    if quotient < base:
        return token_table[quotient]
    else:
        return arbitrary_base_conversion(quotient // base, base) + token_table[quotient % base]
