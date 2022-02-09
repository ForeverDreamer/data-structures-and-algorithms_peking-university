"""
HJ18 识别有效的IP地址和掩码并进行分类统计

描述
请解析IP地址和对应的掩码，进行分类识别。要求按照A/B/C/D/E类地址归类，不合法的地址和掩码单独归类。

所有的IP地址划分为 A,B,C,D,E五类

A类地址1.0.0.0~126.255.255.255;

B类地址128.0.0.0~191.255.255.255;

C类地址192.0.0.0~223.255.255.255;

D类地址224.0.0.0~239.255.255.255；

E类地址240.0.0.0~255.255.255.255


私网IP范围是：

10.0.0.0-10.255.255.255

172.16.0.0-172.31.255.255

192.168.0.0-192.168.255.255


子网掩码为二进制下前面是连续的1，然后全是0。（例如：255.255.255.32就是一个非法的掩码）
（注意二进制下全是1或者全是0均为非法子网掩码）

注意：
1. 类似于【0.*.*.*】和【127.*.*.*】的IP地址不属于上述输入的任意一类，也不属于不合法ip地址，计数时请忽略
2. 私有IP地址和A,B,C,D,E类地址是不冲突的

输入描述：
多行字符串。每行一个IP地址和掩码，用~隔开。

输出描述：
统计A、B、C、D、E、错误IP地址或错误掩码、私有IP的个数，之间以空格隔开。

示例1
输入：
10.70.44.68~255.254.255.0
1.0.0.1~255.0.0.0
192.168.0.2~255.255.255.0
19..0.~255.255.255.0
复制
输出：
1 0 1 0 0 2 1
复制
说明：
10.70.44.68~255.254.255.0的子网掩码非法，19..0.~255.255.255.0的IP地址非法，所以错误IP地址或错误掩码的计数为2；
1.0.0.1~255.0.0.0是无误的A类地址；
192.168.0.2~255.255.255.0是无误的C类地址且是私有IP；
所以最终的结果为1 0 1 0 0 2 1
示例2
输入：
0.201.56.50~255.255.111.255
127.201.56.50~255.255.111.255
复制
输出：
0 0 0 0 0 0 0
复制
说明：
类似于【0.*.*.*】和【127.*.*.*】的IP地址不属于上述输入的任意一类，也不属于不合法ip地址，计数时请忽略
"""


# 牛客网答案
# 代码1
# import sys
#
# res = [0,0,0,0,0,0,0]
#
# def puip(ip):
#     if 1 <= ip[0] <= 126:				# A类地址判断条件
#         res[0] += 1
#     elif 128 <= ip[0] <= 191:			# B类地址判断条件
#         res[1] += 1
#     elif 192 <= ip[0] <= 223:			# C类地址判断条件
#         res[2] += 1
#     elif 224 <= ip[0] <= 239:			# D类地址判断条件
#         res[3] += 1
#     elif 240 <= ip[0] <= 255:			# E类地址判断条件
#         res[4] += 1
#     return
#
# def prip(ip):			# 私有IP地址判断条件
#     if (ip[0] == 10) or (ip[0] == 172 and 16 <= ip[1] <= 32) or (ip[0] == 192 and ip[1] == 168):
#         res[6] += 1
#     return
#
# def ym(msk):			# 判断掩码合法性
#     val = (msk[0] << 24) + (msk[1] << 16) + (msk[2] << 8) + msk[3]		# 转换成32位
#     if val == 0:														  # 排除全0的情况
#         return False
#     if (val+1) == (1<<32):												# 排除全1的情况
#         return False
#     flag = 0
#     while(val):
#         digit = val & 1													# 逐位判断
#         if digit == 1:
#             flag = 1
#         if flag == 1 and digit == 0:									# flag=1表示已经不允许再出现0
#             return False
#         val >>= 1
#     return True
#
#
# def judge(line):
#     ip, msk = line.strip().split('~')
#     ips = [int(x) for x in filter(None, ip.split('.'))]				# 获得表示IP的列表，理论上应该包含四个元素
#     msks = [int(x) for x in filter(None, msk.split('.'))]			# 获得表示掩码的列表，理论上应该包含四个元素
#     if ips[0] == 0 or ips[0] == 127:								# 排除非法IP不计数
#         return
#     if len(ips) < 4 or len(msks) < 4:								  # 判断错误掩码或错误IP
#         res[5] += 1
#         return
#     if ym(msks) == True:											# 通过掩码判断的可以进行IP判断
#         puip(ips)
#         prip(ips)
#     else:
#         res[5] += 1
#     return
#
# for line in sys.stdin:
#     judge(line)
# # judge("192.168.0.2~255.255.255.0")
#
# res = [str(x) for x in res]
# print(" ".join(res))


# 代码2
# import re
# res=[0,0,0,0,0,0,0]
# def toBin(str_list):
#     return "".join(str(i1) for i1 in [bin(int(i))[2:].rjust(8,'0') for i in str_list])
#
# def mask_val(mask):
#     mask_str = mask.split(".")
#     if "" not in mask_str:
#         mask_bin = toBin(mask_str)
# #         print(mask_bin)
#         if (re.search("[0][1]", mask_bin) or "1" not in mask_bin or "0" not in mask_bin):
#             return False
#     return True
#
# try:
#     while True:
#         raw = input().split("~")
#         ip = raw[0]
#         mask = raw[1]
#         ip_str = ip.split(".")
# #         print(mask_val(mask))
#         if "" not in ip_str:
#             if not(ip.startswith("127") or ip.startswith("0")):
#                 if mask_val(mask):
#                     ip_bin = toBin(ip_str)
#                     #Class A to E
#                     if ip_bin.startswith("0"):
#     #                     print(ip+"~"+mask)
#                         res[0] += 1
#                     elif ip_bin.startswith("10"):
#                         res[1] += 1
#                     elif ip_bin.startswith("110"):
#                         res[2] += 1
#                     elif ip_bin.startswith("1110"):
#                         res[3] += 1
#                     elif ip_bin.startswith("1111"):
#                         res[4] += 1
#                     #Private IP
#                     if (ip_str[0]=="10" and 0<=int(ip_str[1])<= 255 and  0<=int(ip_str[2])<=255 and 0<=int(ip_str[3])<=255) or (ip_str[0]=="172" and  16<=int(ip_str[1])<=31 and 0<=int(ip_str[2])<=255 and 0<=int(ip_str[3])<=255) or (ip_str[0]=="192" and ip_str[1] == "168" and 0<=int(ip_str[2])<=255 and 0<=int(ip_str[3])<=255):
#                         res[-1] += 1
#                 else:
#                     res[-2] += 1
#         else:
# #             print(ip+"~"+mask)
#             res[-2] += 1
#
# except EOFError:
#     print(" ".join(str(i) for i in res))


# 代码3
# 8/10 组用例通过
# def checkvalid(ip, ym):
#     # 若ip错误，则掩码无需判断
#     ip1 = filter(None, ip.split('.'))
#     ip2 = [int(x) for x in ip1]
#     if len(ip2) < 4:
#         return False
#     else:
#         # 子网掩码去掉分隔符'.'
#         ym1 = list(map(int, ym.split('.')))
#         # 二进制转换和高位补0
#         ym2 = ''.join(['{:08b}'.format(i) for i in ym1])
#         if ym2.find('0') == -1 or ym2.find('1') == -1 or ym2.find('0') != ym2.rfind('1') + 1:
#             return False
#         return True
#
# def publicip(ip):
#     ipn = [int(n) for n in ip.split('.')]
#     if 1 <= ipn[0] <= 126:
#         return 'a'
#     elif 128 <= ipn[0] <= 191:
#         return 'b'
#     elif 192 <= ipn[0] <= 223:
#         return 'c'
#     elif 224 <= ipn[0] <= 239:
#         return 'd'
#     elif 240 <= ipn[0] <= 255:
#         return 'e'
#     else:
#         return 'ignore'
#
# def privateip(ip):
#     ipn = [int(n) for n in ip.split('.')]
#     if (ipn[0] == 10) or (ipn[0] == 172 and (16 <= ipn[1] <= 31)) or (ipn[0] == 192 and ipn[1] == 168):
#         return True
#     return False
#
# def resprint(ip, ym, classdic):
#     if checkvalid(ip, ym):
#         classdic[publicip(ip)] += 1
#         if privateip(ip):
#             classdic['private'] += 1
#     else:
#         classdic['wrong'] += 1
#     return classdic
#
#
# import sys
# from collections import defaultdict
# def main():
#     classdic = defaultdict(int)
#     for line in sys.stdin:
#         ip, ym = line.split('~')
#         resprint(ip, ym, classdic)
#     res = []
#     for key in ['a', 'b', 'c', 'd', 'e', 'wrong', 'private']:
#         res.append(str(classdic[key]))
#     print(' '.join(res))
#
# main()