"""
HJ68 成绩排序

描述
查找和排序

题目：输入任意（用户，成绩）序列，可以获得成绩从高到低或从低到高的排列,相同成绩
都按先录入排列在前的规则处理。

例示：
jack      70
peter     96
Tom       70
smith     67

从高到低  成绩
peter     96
jack      70
Tom       70
smith     67

从低到高

smith     67

jack      70

Tom       70
peter     96

注：0代表从高到低，1代表从低到高

注意：本题含有多组输入数据！
数据范围：人数：1≤n≤200 ，数据组数：1≤t≤5
进阶：时间复杂度：O(nlogn) ，空间复杂度：O(n)
输入描述：
输入多行，先输入要排序的人的个数，然后分别输入他们的名字和成绩，以一个空格隔开

输出描述：
按照指定方式输出名字和成绩，名字和成绩之间以一个空格隔开

示例1
输入：
3
0
fang 90
yang 50
ning 70
输出：
fang 90
ning 70
yang 50

示例2
输入：
3
1
fang 90
yang 50
ning 70
3
0
moolgouua 43
aebjag 87
b 67
输出：
yang 50
ning 70
fang 90
aebjag 87
b 67
moolgouua 43

说明：
第一组用例:
3
1
fang 90
yang 50
ning 70
升序排序为：
yang 50
ning 70
fang 90
第二组降序为:
aebjag 87
b 67
moolgouua 43
"""

# import operator

input_seq = [
    '4', '0', 'jack 70', 'peter 96', 'Tom 70', 'smith 67',
    '4', '1', 'jack 70', 'peter 96', 'Tom 70', 'smith 67',
    '3', '0', 'fang 90', 'yang 50', 'ning 70',
    '3', '1', 'fang 90', 'yang 50', 'ning 70',
    '3', '0', 'moolgouua 43', 'aebjag 87', 'b 67',
]


def execute(scores, desc):
    reverse = True if desc else False
    # 成绩升序降序在变，输入顺序固定，所以不能用此种方法
    # scores.sort(key=operator.itemgetter(1, 2), reverse=reverse)
    scores.sort(key=lambda elem: elem[1], reverse=reverse)
    i = 0
    while i+1 < len(scores):
        if scores[i][1] == scores[i+1][1] and scores[i][2] > scores[i+1][2]:
            scores[i], scores[i+1] = scores[i+1], scores[i]
        i += 1
    for s in scores:
        print(s[0], s[1])


def sort_score(seq):
    i = 0
    while i < len(seq):
        n = int(seq[i])
        desc = True if seq[i+1] == '0' else False
        scores = []
        for j in range(i+2, i+2+n):
            name, score = seq[j].split(' ')
            scores.append((name, int(score), j))
        execute(scores, desc)
        i += 2+n


sort_score(input_seq)
