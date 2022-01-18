"""
HJ30 字符串合并处理

描述
按照指定规则对输入的字符串进行处理。

详细描述：

第一步：将输入的两个字符串str1和str2进行前后合并。如给定字符串 "dec" 和字符串 "fab" ， 合并后生成的字符串为 "decfab"

第二步：对合并后的字符串进行排序，要求为：下标为奇数的字符和下标为偶数的字符分别从小到大排序。这里的下标的意思是字符在字符串中的位置。注意排序后在新串中仍需要保持原来的奇偶性。例如刚刚得到的字符串“decfab”，分别对下标为偶数的字符'd'、'c'、'a'和下标为奇数的字符'e'、'f'、'b'进行排序（生成 'a'、'c'、'd' 和 'b' 、'e' 、'f'），再依次分别放回原串中的偶数位和奇数位，新字符串变为“abcedf”

第三步：对排序后的字符串中的'0'~'9'、'A'~'F'和'a'~'f'字符，需要进行转换操作。
转换规则如下：
对以上需要进行转换的字符所代表的十六进制用二进制表示并倒序，然后再转换成对应的十六进制大写字符（注：字符 a~f 的十六进制对应十进制的10~15，大写同理）。
如字符 '4'，其二进制为 0100 ，则翻转后为 0010 ，也就是 2 。转换后的字符为 '2'。
如字符 ‘7’，其二进制为 0111 ，则翻转后为 1110 ，对应的十进制是14，转换为十六进制的大写字母为 'E'。
如字符 'C'，代表的十进制是 12 ，其二进制为 1100 ，则翻转后为 0011，也就是3。转换后的字符是 '3'。
根据这个转换规则，由第二步生成的字符串 “abcedf” 转换后会生成字符串 "5D37BF"


注意本题含有多组样例输入。

数据范围：输入的字符串长度满足

输入描述：
本题含有多组样例输入。每组样例输入两个字符串，用空格隔开。

输出描述：
输出转化后的结果。每组样例输出一行。

示例1
输入：
dec fab
输出：
5D37BF

示例2
输入：
ab CD
输出：
3B5D
说明：
合并后为abCD，按奇数位和偶数位排序后是CDab（请注意要按ascii码进行排序，所以C在a前面，D在b前面），转换后为3B5D

示例3
输入：
123 15
输出：
88C4A
"""
input_seq = ['dec fab', 'ab CD', '123 15']

tokens = '0123456789ABCDEF'


def execute(chars):
    # 第一步
    # chars = (str1 + str2)
    # 第二步
    evens = []
    odds = []
    i = 0
    while i < len(chars):
        if i % 2 == 0:
            evens.append(chars[i])
        else:
            odds.append(chars[i])
        i += 1
    evens.sort()
    odds.sort()
    # evens.sort(key=lambda elem: ord(elem))
    # odds.sort(key=lambda elem: ord(elem))
    seq = []
    for e, o in zip(evens, odds):
        seq.append(e)
        seq.append(o)
    if len(chars) % 2 == 1:
        seq.append(evens[0])
    # 第三步
    output = []
    for c1 in seq:
        bin_seq = ''
        if c1.upper() not in tokens:
            output.append(c1)
            continue
        n = tokens.index(c1.upper())
        if n == 0:
            output.append(tokens[0])
            continue
        # 转换成倒序的二进制
        while n > 0:
            remainder = n % 2
            bin_seq += str(remainder)
            n = n // 2
        bin_seq_reverse = bin_seq[::-1]
        i = 0
        result = 0
        while i < len(bin_seq_reverse):
            if bin_seq_reverse[i] == '0':
                i += 1
                continue
            c2 = int(bin_seq_reverse[i])
            result += c2*2**i
            i += 1
        output.append(tokens[result])
    return ''.join(output)


def transform(seq):
    output_seq = []
    for line in seq:
        line = ''.join(line.split(' '))
        output_seq.append(execute(line))
    return output_seq


for item in transform(input_seq):
    print(item)
