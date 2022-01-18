"""
HJ29 字符串加解密

描述
1、对输入的字符串进行加解密，并输出。

2、加密方法为：

当内容是英文字母时则用该英文字母的后一个字母替换，同时字母变换大小写,如字母a时则替换为B；字母Z时则替换为a；

当内容是数字时则把该数字加1，如0替换1，1替换2，9替换0；

其他字符不做变化。

3、解密方法为加密的逆过程。

本题含有多组样例输入。

数据范围：输入的两个字符串长度满足  ，保证输入的字符串都是大小写字母或者数字
输入描述：
输入说明
输入一串要加密的密码
输入一串加过密的密码

输出描述：
输出说明
输出加密后的字符
输出解密后的字符

示例1
输入：
abcdefg
BCDEFGH
输出：
BCDEFGH
abcdefg
"""

from string import ascii_lowercase, ascii_uppercase, digits
import operator

input_seq = ['abcdefg', 'BCDEFGH']
letters_len = 26
digits_len = 10


def transform(chars, decrypt=False):
    oper = operator.sub if decrypt else operator.add
    result = ''

    for c in chars:
        if c in ascii_lowercase:
            result += ascii_lowercase[oper(ascii_lowercase.index(c), 1) % letters_len].upper()
        elif c in ascii_uppercase:
            result += ascii_uppercase[oper(ascii_uppercase.index(c), 1) % letters_len].lower()
        else:
            result += digits[oper(digits.index(c), 1) % digits_len]

    return result


def encrypt_decrypt(seq):
    output_seq = []

    i = 0
    while i + 1 < len(seq):
        e_chars = seq[i]
        d_chars = seq[i+1]
        output_seq.append(transform(e_chars))
        output_seq.append(transform(d_chars, True))
        i += 2

    return output_seq


for item in encrypt_decrypt(input_seq):
    print(item)
