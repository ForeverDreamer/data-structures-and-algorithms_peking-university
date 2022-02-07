"""
HJ39 判断两个IP是否属于同一子网

描述
子网掩码是用来判断任意两台计算机的IP地址是否属于同一子网络的根据。
子网掩码与IP地址结构相同，是32位二进制数，其中网络号部分全为“1”和主机号部分全为“0”。利用子网掩码可以判断两台主机是否中同一子网中。若两台主机的IP地址分别与它们的子网掩码相“与”后的结果相同，则说明这两台主机在同一子网中。

示例：
I P 地址　 192.168.0.1
子网掩码　 255.255.255.0

转化为二进制进行运算：

I P 地址　  11000000.10101000.00000000.00000001
子网掩码　11111111.11111111.11111111.00000000

AND运算   11000000.10101000.00000000.00000000

转化为十进制后为：
192.168.0.0


I P 地址　 192.168.0.254
子网掩码　 255.255.255.0


转化为二进制进行运算：

I P 地址　11000000.10101000.00000000.11111110
子网掩码  11111111.11111111.11111111.00000000

AND运算  11000000.10101000.00000000.00000000

转化为十进制后为：
192.168.0.0

通过以上对两台计算机IP地址与子网掩码的AND运算后，我们可以看到它运算结果是一样的。均为192.168.0.0，所以这二台计算机可视为是同一子网络。

输入一个子网掩码以及两个ip地址，判断这两个ip地址是否是一个子网络。
若IP地址或子网掩码格式非法则输出1，若IP1与IP2属于同一子网络输出0，若IP1与IP2不属于同一子网络输出2。

注:
有效掩码与IP的性质为：
1. 掩码与IP每一段在 0 - 255 之间
2. 掩码的二进制字符串前缀为网络号，都由‘1’组成；后缀为主机号，都由'0'组成

本题有多组输入

输入描述：
多组输入，一组3行，第1行是输入子网掩码、第2，3行是输入两个ip地址

输出描述：
若IP地址或子网掩码格式非法则输出1，若IP1与IP2属于同一子网络输出0，若IP1与IP2不属于同一子网络输出2

示例1
输入：
255.255.255.0
192.168.224.256
192.168.10.4
255.0.0.0
193.194.202.15
232.43.7.59
255.255.255.0
192.168.0.254
192.168.0.1
输出：
1
2
0

说明：
对于第一个例子:
255.255.255.0
192.168.224.256
192.168.10.4
其中IP:192.168.224.256不合法，输出1

对于第二个例子:
255.0.0.0
193.194.202.15
232.43.7.59
2个与运算之后，不在同一个子网，输出2

对于第三个例子，2个与运算之后，如题目描述所示，在同一个子网，输出0
"""

input_seq = [
    # '255.255.252.0', '173.225.245.45', '69.138.93.228',
    # '255.255.0.1', '97.151.30.191', '240.102.155.58',
    # '255.255.252.0', '0.151.30.191', '240.102.155.58',
    # '255.0.0.0', '85.122.52.249', '10.57.28.117',
    # '255.0.0.0', '193.194.202.15', '232.43.7.59',
    # '255.255.255.0', '192.168.0.254', '192.168.0.1',
    '255.255.254.0', '192.168.11.0', '192.168.10.100',
]


def validate_mask(mask):
    allow_one = True
    for bit in mask:
        if allow_one:
            if bit == '1':
                continue
            else:
                allow_one = False
        else:
            if bit == '1':
                raise ValueError()


def validate_ip(ip_segments):
    if ip_segments[0] == '00000000':
        raise ValueError()


def decimal_to_binary(n):
    if not (0 <= n <= 255):
        raise ValueError()
    bin_seq = ''
    # 转换成倒序的二进制
    while n > 0:
        remainder = n % 2
        bin_seq += str(remainder)
        n = n // 2
    bin_seq += '0' * (8 - len(bin_seq))
    return bin_seq[::-1]


def execute(mask, ip1, ip2):
    try:
        mask_segments = [decimal_to_binary(int(n)) for n in mask.split('.')]
        validate_mask(''.join(mask_segments))
        ip1_segments = [decimal_to_binary(int(n)) for n in ip1.split('.')]
        validate_ip(ip1_segments)
        ip2_segments = [decimal_to_binary(int(n)) for n in ip2.split('.')]
        validate_ip(ip2_segments)
    except ValueError:
        return 1
    for mask_segs, ip1_segs, ip2_segs in zip(mask_segments, ip1_segments, ip2_segments):
        for c1, c2, c3 in zip(mask_segs, ip1_segs, ip2_segs):
            c1, c2, c3 = int(c1), int(c2), int(c3)
            if c1 & c2 != c1 & c3:
                return 2
    return 0


def same_subnet(seq):
    output_seq = []
    i = 0
    while i+2 < len(seq):
        mask = seq[i]
        ip1 = seq[i+1]
        ip2 = seq[i+2]
        output_seq.append(execute(mask, ip1, ip2))
        i += 3
    return output_seq


for item in same_subnet(input_seq):
    print(item)
