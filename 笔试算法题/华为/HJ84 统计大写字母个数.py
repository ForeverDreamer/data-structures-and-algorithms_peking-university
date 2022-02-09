"""
HJ84 统计大写字母个数

描述
找出给定字符串中大写字符(即'A'-'Z')的个数。
数据范围：字符串长度：1≤∣s∣≤250
字符串中可能包含空格或其他字符
进阶：时间复杂度：O(n) ，空间复杂度：O(n)
输入描述：
本题含有多组样例输入
对于每组样例，输入一行，代表待统计的字符串

输出描述：
对于每组样例，输出一个整数，代表字符串中大写字母的个数

示例1
输入：
add123#$%#%#O
150175017(&^%&$vabovbao
A 1 0 11
复制
输出：
1
0
1


解题思路
法一 用isupper()函数
while True:
try:
s=input()
res=0
for i in s:
if i.isupper():
res+=1
print(res)
except:
break
'''
#法二 用字符串的比大小！>='A' <='Z'
while True:
try:
n = input()
result = 0
for i in n:
if i >= 'A' and i <= 'Z':
result += 1
print(result)
except:
break

法三：用ord() ASCll表 <91 and ord(i)>64
while True:
try:
s = input()
n=0
for i in s:
if ord(i)<91 and ord(i)>64:
n=n+1
print(n)
except:
break
'''
"""

# 法一 用isupper()函数
while True:
    try:
        s = input()
        res = 0
        for i in s:
            if i.isupper():
                res += 1
        print(res)
    except:
        break
