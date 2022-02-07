"""
HJ52 计算字符串的距离

描述
Levenshtein 距离，又称编辑距离，指的是两个字符串之间，由一个转换成另一个所需的最少编辑操作次数。许可的编辑操作包括将一个字符替换成另一个字符，插入一个字符，删除一个字符。编辑距离的算法是首先由俄国科学家 Levenshtein 提出的，故又叫 Levenshtein Distance 。

Ex：

字符串A: abcdefg

字符串B: abcdef

通过增加或是删掉字符 ”g” 的方式达到目的。这两种方案都需要一次操作。把这个操作所需要的次数定义为两个字符串的距离。

要求：

给定任意两个字符串，写出一个算法计算它们的编辑距离。


数据范围：给定的字符串长度满足 1≤len(str)≤500

本题含有多组输入数据。


输入描述：
每组用例一共2行，为输入的两个字符串

输出描述：
每组用例输出一行，代表字符串的距离

示例1
输入：
abcdefg
abcdef
abcde
abcdf
abcde
bcdef
输出：
1
1
2

解题思路：
说明一：
传递公式：
lev[i][j]用来表示字符串a的[1…i]和字符串b[1…j]的levenshtein距离；
插入和删除操作互为逆过程：a删除指定字符变b等同于b插入指定字符变a；
如果a[i] == b[j]，则说明a[i]和b[j]分别加入a，b之后不会影响levenshtein距离，lev[i][j] = lev[i-1][j-1] + 0;
如果a[i] != b[j]，则需要考虑3种情况的可能：
a中插入字符，即lev[i][j] = lev[i-1][j] + 1;
b中插入字符，即lev[i][j] = lev[i][j-1] + 1;
a[i]替换成b[j]，或b[j]替换成a[i]，lev[i][j] = lev[i-1][j-1] + 1;
取这3种情况的最小值

说明二：
(1)当两个字符串都为空串，编辑距离为0；
(2)当其中一个字符串为空串时，那么编辑距离为另一个非空字符串的长度；
上面两种情况初始化赋值

(3)当两个字符串均为非空时(长度分别为 i 和 j )，取以下三种情况最小值即可：
1、长度分别为 i-1 和 j 的字符串的编辑距离已知，那么加1即可（插入）；
2、长度分别为 i 和 j-1 的字符串的编辑距离已知，那么加1即可（插入）；
3、长度分别为 i-1 和 j-1 的字符串的编辑距离已知:
此时考虑两种情况，若第i个字符和第j个字符不同，那么加1即可（替换）；如果相同，那么不需要加1（两个字符串都加上相同的字符，不影响距离）。

    h e l l o
  0 1 2 3 4 5
k 1 1 2 3 4 5
e 2 2 1 2 3 4
l 3 3 2 1 2 3
m 4 4 3 2 2 3
"""

input_seq = ['kelm', 'hello', 'abcdefg', 'abcdef', 'abcde', 'abcdf', 'abcde', 'bcdef']


def execute(chars1, chars2):
    distances = []
    for i in range(len(chars1)+1):
        distances.append([0]*(len(chars2)+1))
        i += 1
    for i in range(len(chars1)+1):
        distances[i][0] = i
    for j in range(len(chars2)+1):
        distances[0][j] = j
    for i in range(1, len(chars1) + 1):
        for j in range(1, len(chars2) + 1):
            if chars1[i-1] == chars2[j-1]:
                distances[i][j] = distances[i-1][j-1]
            else:
                distances[i][j] = min(distances[i][j-1], distances[i-1][j], distances[i-1][j-1]) + 1
    return distances[len(chars1)][len(chars2)]


def levenshtein_distance(seq):
    output_seq = []
    i = 0
    while i+1 < len(seq):
        chars1 = seq[i]
        chars2 = seq[i+1]
        output_seq.append(execute(chars1, chars2))
        i += 2
    for item in output_seq:
        print(item)


levenshtein_distance(input_seq)
