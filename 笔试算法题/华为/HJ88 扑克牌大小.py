"""
HJ88 扑克牌大小

描述
扑克牌游戏大家应该都比较熟悉了，一副牌由54张组成，含3~A、2各4张，小王1张，大王1张。牌面从小到大用如下字符和字符串表示（其中，小写joker表示小王，大写JOKER表示大王）：
3 4 5 6 7 8 9 10 J Q K A 2 joker JOKER
输入两手牌，两手牌之间用"-"连接，每手牌的每张牌以空格分隔，"-"两边没有空格，如：4 4 4 4-joker JOKER。
请比较两手牌大小，输出较大的牌，如果不存在比较关系则输出ERROR。
基本规则：
（1）输入每手牌可能是个子、对子、顺子（连续5张）、三个、炸弹（四个）和对王中的一种，不存在其他情况，由输入保证两手牌都是合法的，顺子已经从小到大排列；
（2）除了炸弹和对王可以和所有牌比较之外，其他类型的牌只能跟相同类型的存在比较关系（如，对子跟对子比较，三个跟三个比较），不考虑拆牌情况（如：将对子拆分成个子）；
（3）大小规则跟大家平时了解的常见规则相同，个子、对子、三个比较牌面大小；顺子比较最小牌大小；炸弹大于前面所有的牌，炸弹之间比较牌面大小；对王是最大的牌；

（4）输入的两手牌不会出现相等的情况。

数据范围：字符串长度：3≤s≤10

输入描述：
输入两手牌，两手牌之间用"-"连接，每手牌的每张牌以空格分隔，"-"两边没有空格，如 4 4 4 4-joker JOKER。

输出描述：
输出两手牌中较大的那手，不含连接符，扑克牌顺序不变，仍以空格隔开；如果不存在比较关系则输出ERROR。

示例1
输入：
4 4 4 4-joker JOKER
输出：
joker JOKER
"""

# 代码1
# 认证读题很重要 o(╥﹏╥)o
power = ["3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2", "joker", "JOKER"]

while 1:
    try:
        sa, sb = input().split('-')
        sas = sa.split()
        sbs = sb.split()

        # 注：
        # 除了炸弹和对王可以和所有牌比较之外，其他类型的牌只能跟相同类型的存在比较关系
        # 如果不存在比较关系则输出ERROR

        if len(sas) == len(sbs):
            if power.index(sas[0]) > power.index(sbs[0]):
                print(sa)
            else:
                print(sb)
        else:
            # 王炸
            if ["joker", "JOKER"] == sas or ["joker", "JOKER"] == sbs:
                print("joker JOKER")
            elif sas.count(sas[0]) == 4:
                print(sa)
            elif sbs.count(sbs[0]) == 4:
                print(sb)
            else:
                print("ERROR")
    except:
        break


# 代码2
# dic = {
#     '3' : 1, '4' : 2, '5' : 3, '6' : 4, '7' : 5, '8': 6,
#     '9' : 7, '10' : 8, 'J' : 9, 'Q' : 10, 'K' : 11, 'A' : 12,
#     '2' : 13, 'joker' : 14, 'JOKER' : 15
# }
#
# def isboom(lst):
#     if len(lst) == 4 and len(set(lst)) == 1:
#         return True
#     return False
#
# while True:
#     try:
#         s1, s2 = input().split('-')
#         lst1, lst2 = s1.split(), s2.split()
#         L1, L2 = len(lst1), len(lst2)
#         if L1 == L2:
#             if dic[lst1[0]] > dic[lst2[0]]:
#                 print(s1)
#             else:
#                 print(s2)
#         else:
#             if 'joker JOKER' in (s1, s2):
#                 print('joker JOKER')
#             elif isboom(lst1):
#                 print(s1)
#             elif isboom(lst2):
#                 print(s2)
#             else:
#                 print('ERROR')
#     except:
#         break

