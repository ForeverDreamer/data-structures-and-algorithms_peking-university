"""
HJ89 24点运算

描述
计算24点是一种扑克牌益智游戏，随机抽出4张扑克牌，通过加(+)，减(-)，乘(*), 除(/)四种运算法则计算得到整数24，本问题中，扑克牌通过如下字符或者字符串表示，其中，小写joker表示小王，大写JOKER表示大王：

3 4 5 6 7 8 9 10 J Q K A 2 joker JOKER

本程序要求实现：输入4张牌，输出一个算式，算式的结果为24点。

详细说明：

1.运算只考虑加减乘除运算，没有阶乘等特殊运算符号，没有括号，友情提醒，整数除法要当心，是属于整除，比如2/3=0，3/2=1；
2.牌面2~10对应的权值为2~10, J、Q、K、A权值分别为为11、12、13、1；
3.输入4张牌为字符串形式，以一个空格隔开，首尾无空格；如果输入的4张牌中包含大小王，则输出字符串“ERROR”，表示无法运算；
4.输出的算式格式为4张牌通过+-*/四个运算符相连，中间无空格，4张牌出现顺序任意，只要结果正确；
5.输出算式的运算顺序从左至右，不包含括号，如1+2+3*4的结果为24，2 A 9 A不能变为(2+1)*(9-1)=24
6.如果存在多种算式都能计算得出24，只需输出一种即可，如果无法得出24，则输出“NONE”表示无解。
7.因为都是扑克牌，不存在单个牌为0的情况，且没有括号运算，除数(即分母)的数字不可能为0

数据范围：一行由4张牌组成的字符串
输入描述：
输入4张牌为字符串形式，以一个空格隔开，首尾无空格；

输出描述：
输出怎么运算得到24，如果无法得出24，则输出“NONE”表示无解，如果输入的4张牌中包含大小王，则输出字符串“ERROR”，表示无法运算；
示例1
输入：
A A A A
复制
输出：
NONE
复制
说明：
不能实现
示例2
输入：
4 2 K A
复制
输出：
K-A*4/2
复制
说明：
 A+K*2-4也是一种答案，输出任意一种即可
示例3
输入：
B 5 joker 4
复制
输出：
ERROR
复制
说明：
 存在joker，输出ERROR
示例4
输入：
K Q 6 K
复制
输出：
NONE
复制
说明：
按一般的计算规则来看，K+K-(Q/6)=24 或 K-((Q/6)-K)=24，但是因为这个题目的运算不许有括号，所以去掉括号后变为 K+K-Q/6=26-Q/6=14/6=2 或 K-Q/6-K=1/6-K=0-K=-13，其它情况也不能运算出24点，故不存在，输出NONE 
"""

# 代码1
# from itertools import permutations
#
# card = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
# order = range(1,14)
# card_order = dict(zip(card,order))
# opts = ["+", "-", "*", "/"]
#
# def cal(a1,a2,opt):
#     if opt == 0: return a1+a2
#     elif opt == 1: return a1-a2
#     elif opt == 2: return a1*a2
#     elif opt == 3: return a1/a2
#
# def cal24(cards):
#     if "joker" in cards or "JOKER" in cards:
#         print("ERROR")
#         return
#     num_orders = permutations(cards, 4)
#     for nums in num_orders:
#         for i in range(4):
#             a = cal(card_order[nums[0]], card_order[nums[1]], i)
#             for j in range(4):
#                 b = cal(a, card_order[nums[2]], j)
#                 for k in range(4):
#                     c = cal(b, card_order[nums[3]], k)
#                     if c == 24:
#                         print("%s%s%s%s%s%s%s"%(nums[0],opts[i],nums[1],opts[j],nums[2],opts[k],nums[3]))
#                         return
#     print("NONE")
#     return
#
# cards = input().split()
# cal24(cards)


# 代码2
# from itertools import permutations
# data=[str(i) for i in range(2,11)]+['A','J','Q','K']
# a=list(map(str,input().split(' ')))
# if 'joker' in a or 'JOKER' in a:
#     print('ERROR')
# else:
#     a=' '.join(a)
#     for j in a:
#         if j=='A':
#             a=a.replace('A','1')
#         elif j=='J':
#             a=a.replace('J','11')
#         elif j=='Q':
#             a=a.replace('Q','12')
#         elif j=='K':
#             a=a.replace('K','13')
#     list1=['+','-','*','/']
#     a=list(map(str,a.split(' ')))
#     aaa=list(permutations(a))
#     list2=[]
#     for aa in aaa:
#       for x1 in list1:
#         for x2 in list1:
#             for x3 in list1:
#                 aa=list(aa)
#                 y='(('+aa[0]+x1+aa[1]+')'+x2+aa[2]+')'+x3+aa[3]
#                 y1=eval(y)
#                 y2=aa[0]+x1+aa[1]+x2+aa[2]+x3+aa[3]
#                 if y1==24 or y1==24.0:
#                     list2.append(y2)
#
#     if len(list2)!=0:
#         if '1' in list2[0]:
#            list2[0]=list2[0].replace('1','A')
#            if 'AA' in list2[0]:
#                list2[0]=list2[0].replace('AA','J')
#            if 'A2' in list2[0]:
#                list2[0]=list2[0].replace('A2','Q')
#            if 'A3' in list2[0]:
#                list2[0]=list2[0].replace('A3','K')
#         print(list2[0])
#     else:
#         print('NONE')