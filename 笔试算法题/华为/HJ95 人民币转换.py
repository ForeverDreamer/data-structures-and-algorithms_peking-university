"""
HJ95 人民币转换

描述
考试题目和要点：

1、中文大写金额数字前应标明“人民币”字样。中文大写金额数字应用壹、贰、叁、肆、伍、陆、柒、捌、玖、拾、佰、仟、万、亿、元、角、分、零、整等字样填写。

2、中文大写金额数字到“元”为止的，在“元”之后，应写“整字，如532.00应写成“人民币伍佰叁拾贰元整”。在”角“和”分“后面不写”整字。

3、阿拉伯数字中间有“0”时，中文大写要写“零”字，阿拉伯数字中间连续有几个“0”时，中文大写金额中间只写一个“零”字，如6007.14，应写成“人民币陆仟零柒元壹角肆分“。
4、10应写作“拾”，100应写作“壹佰”。例如，1010.00应写作“人民币壹仟零拾元整”，110.00应写作“人民币壹佰拾元整”
5、十万以上的数字接千不用加“零”，例如，30105000.00应写作“人民币叁仟零拾万伍仟元整”


本题含有多组样例输入。

输入描述：
输入一个double数

输出描述：
输出人民币格式

示例1
输入：
151121.15
10012.02
13.64
0.85
复制
输出：
人民币拾伍万壹仟壹佰贰拾壹元壹角伍分
人民币壹万零拾贰元贰分
人民币拾叁元陆角肆分
人民币捌角伍分
复制
示例2
输入：
1010.00
110.00
复制
输出：
人民币壹仟零拾元整
人民币壹佰拾元整
"""


# 代码1
# while 1:
#     try:
#         n,x=list(map(str,input().strip().split('.')))
#         ch = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖','拾']
#         cz = ['元','拾','佰','仟','万','拾','佰','仟','亿','拾','佰','仟']
#         cx = ['角','分']
#         w='人民币'
#         c=len(n)
#         for i in range(c):#整数
#             if i+1==c:
#                 w+=ch[int(n[i])]
#                 w+='元'
#             elif n[i]=='0' and n[i+1]=='0':
#                 if cz[c-i-1]=='万':
#                     w+=cz[c-i-1]
#                 continue#零拾->0
#             else:
#                 w+=ch[int(n[i])]
#                 w+=cz[c-i-1]
#         w=w.replace('零元','')
#         w=w.replace('零仟','零')
#         w=w.replace('零佰','零')#万单独处理
#         w=w.replace('拾零','拾')
#         w=w.replace('壹拾','拾')
#         for i in range(2):#角分
#             if x[0]=='0'and x[1]=='0':
#                 w+='元整'
#                 break
#             else:
#                 w+=ch[int(x[i])]
#                 w+=cx[i]
#         w=w.replace('零角','')
#         w=w.replace('零分','')
#         print(w)
#     except:
#         break


# 代码2
# ch = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
#
# while True:
#     try:
#         s = input()
#         before, after = s.split('.')
#         head, body, tail = '人民币', '', ''
#         if after == '00':
#             tail = '元整'
#         else:
#             if before == '0':
#                 tail = ''
#             else:
#                 tail = '元'
#             if after[0] != '0':
#                 tail += ch[int(after[0])] + '角'
#             if after[1] != '0':
#                 tail += ch[int(after[1])] + '分'
#         lst, i = [], len(before)
#         while i - 4 >= 0:
#             lst.insert(0, before[i - 4:i])
#             i -= 4
#         if i > 0:
#             lst.insert(0, before[:i])
#
#         for i, num in enumerate(lst):  # 如：['15', '1121']
#             flag = True
#             for j, c in enumerate(num):
#                 if c == '0':
#                     if num == '0000':
#                         if lst[-1] != '0000' and flag:
#                             body += '零'
#                             flag = False
#                             continue
#                     else:
#                         if j != len(num) - 1 and num[j + 1] != '0' and flag:
#                             body += '零'
#                             flag = False
#                             continue
#                 else:
#                     if len(num[j:]) == 4:
#                         body += ch[int(c)] + '仟'
#                     elif len(num[j:]) == 3:
#                         body += ch[int(c)] + '佰'
#                     elif len(num[j:]) == 2:
#                         if c != '1':
#                             body += ch[int(c)] + '拾'
#                         else:
#                             body += '拾'
#                     else:
#                         body += ch[int(c)]
#             if len(lst[i:]) == 3:
#                 body += '亿'
#             elif len(lst[i:]) == 2 and num != '0000':
#                 body += '万'
#         print(head + body + tail)
#
#     except:
#         break
