"""
HJ33 整数与IP地址间的转换

描述
原理：ip地址的每段可以看成是一个0-255的整数，把每段拆分成一个二进制形式组合起来，然后把这个二进制数转变成
一个长整数。
举例：一个ip地址为10.0.3.193
每段数字             相对应的二进制数
10                   00001010
0                    00000000
3                    00000011
193                  11000001

组合起来即为：00001010 00000000 00000011 11000001,转换为10进制数就是：167773121，即该IP地址转换后的数字就是它了。

本题含有多组输入用例，每组用例需要你将一个ip地址转换为整数、将一个整数转换为ip地址。

数据范围：保证输入的是合法的 IP 序列


输入描述：
输入
1 输入IP地址
2 输入10进制型的IP地址

输出描述：
输出
1 输出转换成10进制的IP地址
2 输出转换后的IP地址

示例1
输入：
10.0.3.193
167969729
输出：
167773121
10.3.3.193
"""
input_seq = ['89.81.119.56', '1926338696', '234.237.37.104', '3165757026']


def ip_to_integer(ip):
    segments = ip.split('.')
    all_bin_seq = ''
    for s in segments:
        n = int(s)
        bin_seq = ''
        # 转换成倒序的二进制
        while n > 0:
            remainder = n % 2
            bin_seq += str(remainder)
            n = n // 2
        bin_seq += '0' * (8 - len(bin_seq))
        all_bin_seq += bin_seq[::-1]
    i = 0
    result = 0
    all_bin_seq_reverse = all_bin_seq[::-1]
    while i < len(all_bin_seq_reverse):
        if all_bin_seq_reverse[i] == '0':
            i += 1
            continue
        c2 = int(all_bin_seq_reverse[i])
        result += c2 * 2 ** i
        i += 1
    return result


def integer_to_ip(integer):
    n = int(integer)
    bin_str = ''
    # 转换成倒序的二进制
    while n > 0:
        remainder = n % 2
        bin_str += str(remainder)
        n = n // 2
    bin_str += '0' * (32 - len(bin_str))
    step = 8
    i = 0
    ip_segments = []
    while i + step <= len(bin_str):
        segment = bin_str[i:i+step]
        j = 0
        result = 0
        while j < len(segment):
            if segment[j] == '0':
                j += 1
                continue
            c2 = int(segment[j])
            result += c2 * 2 ** j
            j += 1
        ip_segments.append(str(result))
        i += step
    ip_segments = ip_segments[::-1]
    return '.'.join(ip_segments)


def transform(seq):
    output_seq = []
    i = 0
    while i+1 < len(seq):
        ip = seq[i]
        integer = seq[i+1]
        output_seq.append(ip_to_integer(ip))
        output_seq.append(integer_to_ip(integer))
        i += 2

    return output_seq


for item in transform(input_seq):
    print(item)
