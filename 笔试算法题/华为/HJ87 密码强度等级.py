"""
HJ87 密码强度等级

描述
密码按如下规则进行计分，并根据不同的得分为密码进行安全等级划分。

一、密码长度:

5 分: 小于等于4 个字符

10 分: 5 到7 字符

25 分: 大于等于8 个字符

二、字母:

0 分: 没有字母

10 分: 全都是小（大）写字母

20 分: 大小写混合字母

三、数字:

0 分: 没有数字

10 分: 1 个数字

20 分: 大于1 个数字

四、符号:

0 分: 没有符号

10 分: 1 个符号

25 分: 大于1 个符号

五、奖励:

2 分: 字母和数字

3 分: 字母、数字和符号

5 分: 大小写字母、数字和符号

最后的评分标准:

>= 90: 非常安全

>= 80: 安全（Secure）

>= 70: 非常强

>= 60: 强（Strong）

>= 50: 一般（Average）

>= 25: 弱（Weak）

>= 0:  非常弱


对应输出为：

VERY_SECURE

SECURE

VERY_STRONG

STRONG

AVERAGE

WEAK

VERY_WEAK


请根据输入的密码字符串，进行安全评定。

注：

字母：a-z, A-Z

数字：0-9

符号包含如下： (ASCII码表可以在UltraEdit的菜单view->ASCII Table查看)

!"#$%&'()*+,-./     (ASCII码：0x21~0x2F)

:;<=>?@             (ASCII码：0x3A~0x40)

[\]^_`              (ASCII码：0x5B~0x60)

{|}~                (ASCII码：0x7B~0x7E)




提示:
1 <= 字符串的长度<= 300
输入描述：
本题含有多组输入样例。
每组样例输入一个string的密码

输出描述：
每组样例输出密码等级

示例1
输入：
38$@NoNoNo
123

输出：
VERY_SECURE
WEAK

说明：
第一组样例的密码长度大于等于8个字符，得25分；大小写字母都有所以得20分；有两个数字，所以得20分；包含大于1符号，所以得25分；由于该密码包含大小写字母、数字和符号，所以奖励部分得5分，经统计得该密码的密码强度为25+20+20+25+5=95分。
同理，第二组样例密码强度为5+0+20+0+0=25分。

示例2
输入：
Jl)M:+
输出：
AVERAGE

说明：
示例2的密码强度为10+20+0+25+0=55分。
"""


# 代码1
# 密码长度得分计算
def lenscore(x):
    if 0 < len(x) <= 4:
        return 5
    elif 5 <= len(x) <= 7:
        return 10
    elif len(x) >= 8:
        return 25
    else:
        return 0


# 字母大小写得分计算
def zimuscore(x):
    x = str(x)
    a = 0  # 计算小写个数
    b = 0  # 计算大写个数
    for i in x:
        if i.islower():  # 计算小写
            a += 1
        if i.isupper():  # 计算大写
            b += 1

    if (a != 0 and b == 0) or (b != 0 and a == 0):  # 全是小写或者全是大写
        return 10
    if a != 0 and b != 0:  # 大小写混合
        return 20
    else:
        return 0


# 数字得分计算：
def digtscore(x):
    x = str(x)
    a = 0  # 计算数字个数
    for i in x:
        if i.isdigit():
            a += 1

    if a == 1:
        return 10
    if a > 1:
        return 20
    else:
        return 0


# 符号得分计算
def fhscore(x):
    x = str(x)
    a = 0  # 计算符号个数
    fsm = "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
    for i in x:
        if i in fsm:
            a += 1

    if a == 1:
        return 10
    if a > 1:
        return 25
    else:
        return 0


# 奖励得分计算
def jlscore(x):
    x = str(x)
    a = 0  # 计算小写个数
    b = 0  # 计算大写个数
    for i in x:
        if i.islower():  # 计算小写
            a += 1
        if i.isupper():  # 计算大写
            b += 1

    if ((a != 0 and b == 0) or (b != 0 and a == 0)) and digtscore(x) != 0:  # 字母加数字
        return 2
    if ((a != 0 and b == 0) or (b != 0 and a == 0)) and digtscore(x) != 0 and fhscore(x):  # 字母加数字加符号
        return 3
    if (a != 0 and b != 0) and digtscore(x) != 0 and fhscore(x):  # 大小写字母加数字加符号
        return 5
    else:
        return 0


while True:
    try:
        a = str(input())
        countscore = lenscore(a) + zimuscore(a) + digtscore(a) + fhscore(a) + jlscore(a)
        # print(countscore)
        if countscore >= 90:
            print("VERY_SECURE")
        if 80 <= countscore < 90:
            print("SECURE")
        if 70 <= countscore < 80:
            print("VERY_STRONG")
        if 60 <= countscore < 70:
            print("STRONG")
        if 50 <= countscore < 60:
            print("AVERAGE")
        if 25 <= countscore < 50:
            print("WEAK")
        if 0 <= countscore < 25:
            print("VERY_WEAK")

    except:
        break


