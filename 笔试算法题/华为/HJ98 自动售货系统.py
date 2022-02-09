"""
HJ98 自动售货系统
"""

# 代码1
# def f(pq):
#     w10, w5, w2, w1 = 0, 0, 0, 0  # 记录已经找出的零钱
#     while pq > 0:  # 循环直到找零完成
#         if pq >= 10 and dic_q['10'] >= 1:  # 可以找10元时
#             pq -= 10  # 余额减10
#             w10 += 1  # 已经找出的零钱+1
#             dic_q['10'] -= 1  # 零钱10数量-1
#         elif pq >= 5 and dic_q['5'] >= 1:  # 可以找5元时
#             pq -= 5
#             w5 += 1
#             dic_q['5'] -= 1
#         elif pq >= 2 and dic_q['2'] >= 1:
#             pq -= 2
#             w2 += 1
#             dic_q['2'] -= 1
#         elif pq >= 1 and dic_q['1'] >= 1:
#             pq -= 1
#             w1 += 1
#             dic_q['1'] -= 1
#         else:
#             pq -= 1  # 耍赖，如果因零钱不足导致不能退币，则尽最大可能退币，以减少用户损失。
#     return pq, w1, w2, w5, w10
# while True:
#     try:
#         s = input().split(';')
#         dic_m = {'A1': 2, 'A2': 3, 'A3': 4, 'A4': 5, 'A5': 8, 'A6': 6}  # 商品单价字典
#         dic_n = {'A1': 0, 'A2': 0, 'A3': 0, 'A4': 0, 'A5': 0, 'A6': 0}  # 商品数量字典
#         dic_q = {'10': 0, '5': 0, '2': 0, '1': 0}  # 零钱字典
#         pq = 0
#         for i in s[:-1]:
#             if i[0] == 'r':  # 系统初始化，把商品数量和零钱放入字典
#                 b = i.split()
#                 m = b[1].split('-')
#                 q = b[2].split('-')
#                 dic_n['A1'], dic_n['A2'], dic_n['A3'], dic_n['A4'], dic_n['A5'], dic_n['A6'] = int(m[0]), int(m[1]), int(m[2]), int(m[3]), int(m[4]), int(m[5])
#                 dic_q['1'], dic_q['2'], dic_q['5'], dic_q['10'] = int(q[0]), int(q[1]), int(q[2]), int(q[3])
#                 print('S001:Initialization is successful')
#             elif i[0] == 'p':  # 投币
#                 pq1 = int(i.split()[1])
#                 if pq1 not in [1, 2, 5, 10]:  # 币值非法
#                     print('E002:Denomination error')
#                 elif pq1 not in [1, 2] and pq1 >= (dic_q['1'] + dic_q['2']*2):  # 存钱盒中1元和2元面额钱币总额小于本次投入的钱币面额
#                     print('E003:Change is not enough, pay fail')
#                 elif dic_n['A1'] == 0 and dic_n['A2'] == 0 and dic_n['A3'] == 0 and dic_n['A4'] == 0 and dic_n['A5'] == 0 and dic_n['A6'] == 0:  # 自动售货机中商品全部销售完毕
#                     print('E005:All the goods sold out')
#                 else :
#                     dic_q[str(pq1)] += 1  # 字典对应币值零钱数量加一
#                     pq += pq1  # 投币余额增加
#                     print('S002:Pay success,balance={}'.format(pq))
#             elif i[0] == 'b':  # 购买商品
#                 bn = i.split()[1]
#                 if bn not in dic_n.keys():  # 购买的商品不在商品列表中
#                     print('E006:Goods does not exist')
#                 elif dic_n[bn] == 0:  # 所购买的商品的数量为0
#                     print('E007:The goods sold out')
#                 elif int(pq) < dic_m[bn]:  # 投币余额小于待购买商品价格
#                     print('E008:Lack of balance')
#                 else:
#                     pq = int(pq) - dic_m[bn]  # 余额相应减少
#                     print('S003:Buy success,balance={}'.format(pq))
#                     dic_n[bn] -= 1  # 贩卖机物品数量减一
#             elif i[0] == 'c':
#                 if pq == 0:  # 币余额等于0
#                     print('E009:Work failure')
#                 else:  # 按照退币原则进行“找零”
#                     pq, w1, w2, w5, w10= f(pq)  # f()函数实现过程
#                     print('1 yuan coin number={}'.format(w1))
#                     print('2 yuan coin number={}'.format(w2))
#                     print('5 yuan coin number={}'.format(w5))
#                     print('10 yuan coin number={}'.format(w10))
#             elif i[0] == 'q':  # 查询功能
#                 if ' ' not in i:  # 给出的案例中q1之间无空格，非标准输入。为了过示例添加
#                     print('E010:Parameter error')
#                 elif i.split()[1] not in ['0', '1']:  # “查询类别”参数错误
#                     print('E010:Parameter error')
#                 elif i.split()[1] == '0':  # 查询类别0
#                     print('A1 2 {}'.format(dic_n['A1']))
#                     print('A2 3 {}'.format(dic_n['A2']))
#                     print('A3 4 {}'.format(dic_n['A3']))
#                     print('A4 5 {}'.format(dic_n['A4']))
#                     print('A5 8 {}'.format(dic_n['A5']))
#                     print('A6 6 {}'.format(dic_n['A6']))
#                 elif i.split()[1] == '1':  # 查询类别1
#                     print('1 yuan coin number={}'.format(dic_q['1']))
#                     print('2 yuan coin number={}'.format(dic_q['2']))
#                     print('5 yuan coin number={}'.format(dic_q['5']))
#                     print('10 yuan coin number={}'.format(dic_q['10']))
#     except:
#         break


# 代码2
# 零售机
# while True:
#     try:  # 输入数据为r 22-18-21-21-7-20 3-23-10-6;c;q0;p 1;b A6;c;b A5;b A1;c;q1;p 5;
#         # r 28-12-11-1-16-10 19-30-8-11;b A1;p 1;
#         initialization = {}  # 初始化字典用于存放商品信息
#         money = {}    #初始化字典用于存放零钱信息
#         req_count = {}
#         d = input()
#         a = d.split(';')
#         b = a[0].split()  # 按空格分离
#         c = []
#         n = 1
#         x = 0
#         m = [1, 2, 5, 10]    #钱币面额
#         p = [2, 3, 4, 5, 8, 6]    #商品价格
#         for i in range(1, len(b)):  # 商品数量和零钱数量分开存放
#             for j in b[i].split('-'):
#                 if i == 1:  # 存入商品信息
#                     initialization['A' + str(n)] = [int(j), p[n - 1]]   #用字典存入商品及对应的数量和价格
#                     n += 1
#                 else:  # 存入零钱信息
#                     money[m[x]] = int(j)
#                     x += 1
#         print('S001:Initialization is successful')
#         # 定义一些中间态参数
#         total_pay = 0   #实时变换的售货机存币
#         for dictate in a[1:]:  # 遍历命令开始执行
#             if 'p' in dictate:  # 付钱
#                 pay = int(dictate.split()[1])   #存下当前的输入钱币
#                 count = 0   #用来计算商品是否都已卖光
#                 for key in initialization.keys():   #开始计数卖光商品的种类数
#                     if initialization[key] == 0:
#                         count += 1
#                 if pay not in m:    #是不是能收入的钱币
#                     print('E002:Denomination error')
#                 elif money[1]+ money[2] * 2 < pay:  #1块和2块之和不能低于此次投入的面值
#                     print('E003:Change is not enough, pay fail')
#                 elif count == len(b[1].split('-')):     #商品都卖光了
#                     print('E005:All the goods sold out')
#                 else:
#                     total_pay += pay    #更新售货机存币
#                     money[pay] += 1     #更新售货机钱币种类个数
#                     print('S002:Pay success,balance=%d' % total_pay)
#             elif 'b' in dictate:    #购买商品
#                 good_name = dictate.split()[1]  #取出商品名称
#                 if good_name not in initialization.keys():  #商品是不是有卖的
#                     print('E006:Goods does not exist')
#                 elif initialization[good_name][0] == '0':   #商品有没有卖完
#                     print('E007:The goods sold out')
#                 elif initialization[good_name][1] > total_pay:  #商品价格是否超出售货机现有存币
#                     print('E008:Lack of balance')
#                 else:#购买成功
#                     total_pay -= initialization[good_name][1]   #更新售货机存币
#                     initialization[good_name][0] -= 1   #更新该商品存有个数
#                     print('S003:Buy success,balance=%d'%total_pay)
#             elif 'c' in dictate:    #退钱
#                 if total_pay == 0:  #没钱可退
#                     print('E009:Work failure')
#                 else:
#                     for i in range(len(m) - 1, -1, -1): #倒着遍历钱币的种类（因为要求退出的钱币总张数最小）
#                         req = money[m[i]] - (total_pay // m[i]) #售货机现有当前轮次面额的钱币张数-当前轮次面额的钱币需要多少张
#                         if req < 0:#存有的张数不够
#                             req_count[m[i]] = money[m[i]]   #用req——count接收需要的当前面额张数
#                             money[m[i]] = 0#清空当前面额的所有钱币
#                             total_pay += -m[i] * req_count[m[i]]    #总钱数-当前面额退了多少钱
#                         else:
#                             req_count[m[i]] = total_pay // m[i] #用req——count接收需要的当前面额张数
#                             money[m[i]] -= req_count[m[i]]  #更新售货机当前面额钱币张数
#                             total_pay += -m[i] * req_count[m[i]]    #总钱数-当前面额退了多少钱
#                     total_pay = 0   #无论退多少都要清空售货机的存币
#                     # 1yuancoin number = 0
#                     for i in sorted(req_count):
#                         print('%d yuan coin number=%d' % (i, req_count[i])) #列出退的钱币
#             elif 'q' in dictate:    #查询售货机
#                 try:    #参数格式可能错误，试着取出参数
#                     if dictate.split()[1]=='0': #   售货机商品详情
#                         for i in sorted(initialization.items(), key=lambda kv: (kv[1], kv[0]),reverse=True):    #根据value（各种类商品数量）排序
#                             print(str(i[0])+' '+str(i[1][0])+' '+str(i[1][1]) )
#                     elif dictate.split()[1]=='1':   #售货机钱币各种类张数
#                         for key, value in money.items():
#                             print('%d yuan coin number=%d' % (key, value))
#                     else:   #可能没有这个参数
#                         print('E010:Parameter error')
#                 except:
#                     print('E010:Parameter error')
#     except:
#         break    #有个小缺陷，商品数量相同时，没能按商品名称先后顺序排序（怎么才能快速按值排序的同时还能兼顾键的排序呢）
