"""
HJ27 查找兄弟单词

描述
定义一个单词的“兄弟单词”为：交换该单词字母顺序（注：可以交换任意次），而不添加、删除、修改原有的字母就能生成的单词。
兄弟单词要求和原来的单词不同。例如： ab 和 ba 是兄弟单词。 ab 和 ab 则不是兄弟单词。
现在给定你 n 个单词，另外再给你一个单词 str ，让你寻找 str 的兄弟单词里，按字典序排列后的第 k 个单词是什么？
注意：字典中可能有重复单词。本题含有多组输入数据。

数据范围：，输入的字符串长度满足  ，
输入描述：
先输入单词的个数n，再输入n个单词。 再输入一个单词，为待查找的单词x 最后输入数字k
输出描述：
输出查找到x的兄弟单词的个数m 然后输出查找到的按照字典顺序排序后的第k个兄弟单词，没有符合第k个的话则不用输出。

示例1
输入：
3 abc bca cab abc 1
输出：
2
bca

示例2
输入：
6 cab ad abcd cba abc bca abc 1
输出：
3
bca

说明：
abc的兄弟单词有cab cba bca，所以输出3
经字典序排列后，变为bca cab cba，所以第1个字典序兄弟单词为bca
"""

input_str = '6 cab ad abcd cba abc bca abc 1'


def is_anagram(d_x, word_brother):
    d_brother = {}

    for c in word_brother:
        code = ord(c)
        if code in d_brother:
            d_brother[code] += 1
        else:
            d_brother[code] = 1

    if len(d_x) != len(d_brother):
        return False
    for key in d_x:
        if d_x.get(key) == d_brother.get(key):
            continue
        return False

    return True


def find_brothers(data):
    seq = data.split(' ')
    # n = int(seq[0])
    x = seq[-2]
    k = int(seq[-1])
    words = seq[1:-2]
    d_x = {}
    for c in x:
        code = ord(c)
        if code in d_x:
            d_x[code] += 1
        else:
            d_x[code] = 1

    m = 0
    brothers = []
    for w in words:
        # 兄弟单词要求和原来的单词不同
        if x == w:
            continue
        # 是否变位词
        if is_anagram(d_x, w):
            m += 1
            brothers.append(w)
    # 按字典序排列
    brothers.sort()

    k_word = brothers[k-1] if len(brothers) >= k else None
    return m, k_word


for item in find_brothers(input_str):
    if item is not None:
        print(item)
