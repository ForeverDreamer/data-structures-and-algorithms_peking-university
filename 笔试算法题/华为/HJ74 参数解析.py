"""
HJ74 参数解析

在命令行输入如下命令：

xcopy /s c:\\ d:\\e，

各个参数如下：

参数1：命令字xcopy

参数2：字符串/s

参数3：字符串c:\\

参数4: 字符串d:\\e

请编写一个参数解析程序，实现将命令行各个参数解析出来。


解析规则：

1.参数分隔符为空格
2.对于用""包含起来的参数，如果中间有空格，不能解析为多个参数。比如在命令行输入xcopy /s "C:\\program files" "d:\"时，参数仍然是4个，第3个参数应该是字符串C:\\program files，而不是C:\\program，注意输出参数时，需要将""去掉，引号不存在嵌套情况。
3.参数不定长

4.输入由用例保证，不会出现不符合要求的输入
数据范围：字符串长度：1≤s≤1000
进阶：时间复杂度：O(n) ，空间复杂度：O(n)
输入描述：
输入一行字符串，可以有空格

输出描述：
输出参数个数，分解后的参数，每个参数都独占一行

示例1
输入：
xcopy /s c:\\ d:\\e
复制
输出：
4
xcopy
/s
c:\\
d:\\e


题目分析
题目给出我们一个命令行输入的字符串
我们要根据规则将命令切分成子参数
规则一：空格隔开的部分被视为不同的参数
规则二：如果存在引号包含的参数，则不管有无空格，引号内的部分视作一个参数

方法一：分割空格判断引号
实现思路
我们首先将给定字符串按照空格来分割开得到列表m
列表m中一定存在有被错误分割的部分，由于引号囊括的参数也被错误地无差别分割了
但是引号存在的特征一定是在某一个子串的首，该字串或另一个子串的尾
只要把握这个特征就可以重新连接起来这个引号部分的参数信息
具体实现和注释见下面的代码
def solution(s):
    m = s.split()
    pos = -1                                      # 筛选出来的下一个字符串的为止
    l = []                                        # 结果列表
    for i in range(len(m)):
        if i < pos:                               # 如果i不够pos的值则说明当前i对应的字符串已经是""引号处理中的一部分了
            continue
        res = m[i]
        if m[i][0] == '"':                        # 如果有一个位置开始有引号
            res = m[i][1:]                        # 舍弃引号保留字符串部分
            if m[i][-1] != '"':                   # 处理本字符串只有左侧有引号，另一引号在其他字符串中的情况
                for j in range(i+1, len(m)):      # 继续从i遍历知道找到第二个引号
                    res = res + " " + m[j]        # 连接整个长的字符串
                    if m[j][-1] == '"':           # 找到第二个引号结束标志
                        res = res[:-1]            # 将目标串存储在res中
                        pos = j+1                 # 标记下一需要定位的位置
                        break
            else:
                res = m[i][1:-1]                  # 处理本字符串前后都有引号的情况
        l.append(res)

    print(len(l))
    for s in l:
        print(s)
    return

while True:
    try:
        s = input()
        solution(s)
    except:
        break
复杂度分析
时间复杂度：O(n)O(n)O(n)，遍历整个字符串和处理字符串都是O(n)O(n)O(n)的时间代价，中间虽然有重组部分的循环开销，但是外层循环继续处理的部分也是重组之后的剩余字符串，用Continue语句跳过了很多不必要的开销
空间复杂度：O(n)O(n)O(n)，res列表的开销

方法二：分割引号判断空格
实现思路
我们可以换一种思维，首先分割引号，这样直接保留了不会被破坏的包含空格的参数
然后其他参数由于未被完全分割，还存在在未完全分割的较长串中
但是这些较长串有一个特征，就是首尾一定有一个空格元素（除了给定输入字符串中本来就无引号的情况）
根据这一特征同样可以确定哪些部分需要空格分割，哪些部分不需要空格分割
def solution(s):
    m = filter(None , s.split('"'))                # 用引号分割字符串，并除去其中的空串部分
    res = []
    if '"' in s:                                   # 判断最初的字符串中是否有引号
        for c in m:
            if c[0] != ' ' and c[-1] != ' ':       # 对于s中引号部分的参数，其首尾一定非空格
                res.append(c)
            else:                                  # 否则就是应该用空格切分开的不同参数
                p = c.split()
                for n in p:
                    res.append(n)

    else:                                          # 对于无引号的字符串直接空格切割输出即可
        for c in s.split():
            res.append(c)
    print(len(res))
    for i in res:
        print(i)
    return

while True:
    try:
        s = input()
        solution(s)
    except:
        break
复杂度分析
时间复杂度：O(n)O(n)O(n)，分割字符串和遍历字符串的开销都是O(n)O(n)O(n)
空间复杂度：O(n)O(n)O(n)，res列表的开销
"""


# 牛客网答案

# 方法一：分割空格判断引号
def solution(s):
    m = s.split()
    pos = -1  # 筛选出来的下一个字符串的为止
    l = []  # 结果列表
    for i in range(len(m)):
        if i < pos:  # 如果i不够pos的值则说明当前i对应的字符串已经是""引号处理中的一部分了
            continue
        res = m[i]
        if m[i][0] == '"':  # 如果有一个位置开始有引号
            res = m[i][1:]  # 舍弃引号保留字符串部分
            if m[i][-1] != '"':  # 处理本字符串只有左侧有引号，另一引号在其他字符串中的情况
                for j in range(i + 1, len(m)):  # 继续从i遍历知道找到第二个引号
                    res = res + " " + m[j]  # 连接整个长的字符串
                    if m[j][-1] == '"':  # 找到第二个引号结束标志
                        res = res[:-1]  # 将目标串存储在res中
                        pos = j + 1  # 标记下一需要定位的位置
                        break
            else:
                res = m[i][1:-1]  # 处理本字符串前后都有引号的情况
        l.append(res)

    print(len(l))
    for s in l:
        print(s)
    return


while True:
    try:
        s = input()
        solution(s)
    except:
        break


# 方法二：分割引号判断空格
# def solution(s):
#     m = filter(None, s.split('"'))  # 用引号分割字符串，并除去其中的空串部分
#     res = []
#     if '"' in s:  # 判断最初的字符串中是否有引号
#         for c in m:
#             if c[0] != ' ' and c[-1] != ' ':  # 对于s中引号部分的参数，其首尾一定非空格
#                 res.append(c)
#             else:  # 否则就是应该用空格切分开的不同参数
#                 p = c.split()
#                 for n in p:
#                     res.append(n)
#
#     else:  # 对于无引号的字符串直接空格切割输出即可
#         for c in s.split():
#             res.append(c)
#     print(len(res))
#     for i in res:
#         print(i)
#     return
#
#
# while True:
#     try:
#         s = input()
#         solution(s)
#     except:
#         break


