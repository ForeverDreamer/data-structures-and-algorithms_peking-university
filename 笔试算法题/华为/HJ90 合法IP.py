"""
HJ90 合法IP

描述
IPV4地址可以用一个32位无符号整数来表示，一般用点分方式来显示，点将IP地址分成4个部分，每个部分为8位，表示成一个无符号整数（因此正号不需要出现），如10.137.17.1，是我们非常熟悉的IP地址，一个IP地址串中没有空格出现（因为要表示成一个32数字）。

现在需要你用程序来判断IP是否合法。

注意本题有多组样例输入。
数据范围：数据组数：1≤t≤18
进阶：时间复杂度：O(n) ，空间复杂度：O(n)

输入描述：
输入一个ip地址，保证不包含空格

输出描述：
返回判断的结果YES or NO

示例1
输入：
10.138.15.1
255.0.0.255
255.255.255.1000
复制
输出：
YES
YES
NO
"""


# 代码1
# 因为题目中有'+8' '01'这种字符，所以不能简单的用int()转换。
# 创建了一个0-255的str列表
# 输入值以'.'分割成list,先判断分割的list长度是否是4，如果不是直接输出NO
# 然后判断list中所有元素的是否在str列表中
# lista = [str(i) for i in range(0, 256)]
# def daxiao(n):
#     if n in lista:
#         return True
#     else:
#         return False
#
# while True:
#     try:
#         a = input().split('.')
#         x = []
#         if len(a)!=4:
#             print('NO')
#         else:
#             for i in a:
#                 a = daxiao(i)
#                 x.append(a)
#             if x.count(True) == len(x):
#                 print('YES')
#             else:
#                 print('NO')
#     except:
#         break


# 代码2
# 这题主要是由几种特殊情况比较烦 用数组而不是直接用flag的好处就是不用在意这种情况; 符合.不符合.符合.符合 由于中间不符合，flag为0，
# 但是后面有符合的，flag又置为1，最终flag还是1，用数组的话就能解决这问题
while True:
    try:
        lst=list(input().split("."))
        #print(lst)
        #flag=1
        tmpflag=[]#非指向性
        if len(lst)!=4:#针对只写了3个的
            tmpflag.append(0)
        for i in lst:
            if i.isnumeric():#针对+1，+4这种奇葩的结构，就用这个过滤
                if int(i) > 255 or (i.startswith('0') and len(i) > 1):#考虑03这种情况，startwith
                    tmpflag.append(0)
                else:
                    tmpflag.append(1)
            else:
                tmpflag.append(0)
        if 0 in tmpflag:
            print("NO")
        else:
            print("YES")
    except:
        break
