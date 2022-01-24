"""
HJ63 DNA序列

描述
一个 DNA 序列由 A/C/G/T 四个字母的排列组合组成。 G 和 C 的比例（定义为 GC-Ratio ）是序列中 G 和 C 两个字母的总的出现次数除以总的字母数目（也就是序列长度）。在基因工程中，这个比例非常重要。因为高的 GC-Ratio 可能是基因的起始点。

给定一个很长的 DNA 序列，以及限定的子串长度 N ，请帮助研究人员在给出的 DNA 序列中从左往右找出 GC-Ratio 最高且长度为 N 的第一个子串。
DNA序列为 ACGT 的子串有: ACG , CG , CGT 等等，但是没有 AGT ， CT 等等

数据范围：字符串长度满足 1≤n≤1000  ，输入的字符串只包含 A/C/G/T 字母
输入描述：
输入一个string型基因序列，和int型子串的长度

输出描述：
找出GC比例最高的子串,如果有多个则输出第一个的子串

示例1
输入：
ACGT
2
输出：
CG
说明：
ACGT长度为2的子串有AC,CG,GT3个，其中AC和GT2个的GC-Ratio都为0.5，CG为1，故输出CG

示例2
输入：
AACTGTGCACGACCTGA
5
输出：
GCACG
说明：
虽然CGACC的GC-Ratio也是最高，但它是从左往右找到的GC-Ratio最高的第2个子串，所以只能输出GCACG。
"""

input_seq = ['ACGT', '2', 'AACTGTGCACGACCTGA', '5']


def execute(chars, n):
    i = 0
    ratio_dic = {}
    while i+n <= len(chars):
        sub_chars = chars[i:i+n]
        count = 0
        for c in sub_chars:
            if c == 'C' or c == 'G':
                count += 1
        if sub_chars not in ratio_dic:
            ratio_dic[sub_chars] = [count / len(sub_chars), i]
        i += 1
    # for sub_chars, ratio_and_idx in ratio_dic.items():
    ratio_arr = list(ratio_dic.items())
    ratio_arr.sort(key=lambda elem: elem[1][0], reverse=True)
    max_ratio_item = ratio_arr.pop(0)
    max_ratio = max_ratio_item[1][0]
    filtered_arr = [max_ratio_item]
    for item in ratio_arr:
        if item[1][0] != max_ratio:
            break
        filtered_arr.append(item)
    filtered_arr.sort(key=lambda elem: elem[1][1])
    return filtered_arr[0][0]


def decimal_to_binary(seq):
    output_seq = []
    i = 0
    while i+1 < len(seq):
        chars = seq[i]
        n = seq[i+1]
        output_seq.append(execute(chars, int(n)))
        i += 2
    for item in output_seq:
        print(item)


decimal_to_binary(input_seq)
