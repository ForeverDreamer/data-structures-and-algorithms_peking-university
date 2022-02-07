"""
HJ20 密码验证合格程序

描述
密码要求:
1.长度超过8位
2.包括大小写字母.数字.其它符号,以上四种至少三种
3.不能有长度大于2的不含公共元素的子串重复 （注：其他符号不含空格或换行）

数据范围：输入的字符串长度满足

本题有多组输入
输入描述：
一组或多组字符串。每组占一行

输出描述：
如果符合要求输出：OK，否则输出NG

示例1
输入：
021Abc9000
021Abc9Abc1
021ABC9000
021$bc9000
输出：
OK
NG
NG
OK
"""

from string import ascii_lowercase, ascii_uppercase, digits

# input_seq = ['021Abc9000', '021Abc9Abc1', '021ABC9000', '021$bc9000']
input_seq = ['%61Z^0@$L@(&03^Q+!V!O~$7PJq7Z&03-(iPmo$foE*']


def validate_password(password):
    # 长度超过8位
    if len(password) <= 8:
        return 'NG'
    chars_dict = {}
    for char in password:
        if char == ' ' or char == '\n':
            return 'NG'
        if char in ascii_lowercase:
            chars_dict['lowercase'] = True
        elif char in ascii_uppercase:
            chars_dict['uppercase'] = True
        elif char in digits:
            chars_dict['digits'] = True
        # 其他符号不含空格或换行
        # elif char != ' ' and char != '\n':
        #     chars_dict['other'] = True
        else:
            chars_dict['other'] = True
    # 包括大小写字母.数字.其它符号,以上四种至少三种
    if len(chars_dict) < 3:
        return 'NG'

    # 不能有长度大于2的不含公共元素的子串重复
    def has_other(chars):
        for c in chars:
            if (c not in ascii_lowercase) and (c not in ascii_uppercase) and (c not in digits):
                return True
        return False

    step = 3
    while step <= len(password):
        start1 = 0
        start2 = start1 + step
        while start1+step <= len(password):
            first_str = password[start1:start1+step]
            if has_other(first_str):
                start1 += 1
                start2 = start1 + step
                continue
            while start2+step <= len(password):
                second_str = password[start2:start2+step]
                if first_str == second_str:
                    return 'NG'
                start2 += 1
            start1 += 1
            start2 = start1 + step
        step += 1
    return 'OK'


output_seq = [validate_password(pw) for pw in input_seq]

for item in output_seq:
    print(item)

# &4*@192*%41q6065%hV+02~S-Y!u%8@$8^4
# @Bu72v(~vxf4rf34&^#^m0V!93up+@@R(#2T0
# fi%*7z(8W~7~9-C2520)I&9f#
# m98+(@G6n32(@#&E1t#5~
# h^%7L@^)n$*8uM97^5yvr2PvQX8A!8C2G*
# 2#lv0b%^^db$184&k+12l6k0$$7%4i3E1%9K$$)4
# 5#4d~4yDd3Y7dih-Mp&fX2x1865!U
# 8G7+)p#3*6$3B&
# 68h0Z0+v0c*!9306*1E3zKM05)e4
# PV0uow@)!&#3Iab7(G6-15C$8e6S
# )6D2+-~4+T97Y&zB96l2+2!251t1uTM3tT%36E
# w9)o6axU2@U22^-&35^@!ub9^839y#A05b*GF9&2D
# 86(-a-ieC&7y)!7+$p
# A3#&*9&K!#+!
# 2$*u*^7auK*~i776)*J+z%76~322#
# -!79n2aZKVa383p3#32*Sx4@30j(3E
# #0q&#~Qk+2~iZ+8(^^5$jk2u421^jo^L$0Hg&~*+
# &@0!~@-6+7-9!5T)O8$7+
# #@%V-q2$*#9T85Yg#e(D4^Q#784!)I3-~$m54tN
# 6+6*^@f841X0F!2cB(++D@7d8D1+#6^wa03~6)%93)
# %@%!4+!^mz$N988+ju34J+osm!I
# 5h5-+6*3((d30#1270~(
# 6JD7+8+0~4819w$4F0S#*^nPH#(s0
# Z@5$w0!U!#j3ci&D(q2pSb9c#j88@
# J
# 0+0Y~dR99*Ht!047#p%
# 1(21U69DX9p2c$#7+)*97CY8~w(!*HbL
# RXb&8B%RnB(40)+)a*!z)DK2
# &%&10#7(i@0^0M@^w7h56b!+
# M%7Js#lC%rY9X5%@-4C
# %61Z^0@$L@(&03^Q+!V!O~$7PJq7Z&03-(iPmo$foE*
# +P0!P#7l&9
# $4%8$)&$6+04iT9X#2*928IG9&2Yl58#9-3OJ
# 8&PU93P8-5#!&ec47*0&$)^37)+s@U$
# 7-0c5674~#i27
# (V-Mq^-o()~)~**i4Vjb(CZ7~73t!N)$+!3a98@wQ
# s&Q32~1
# P206vW3508(9y)@8wyO02-@gZY(H~4J7-@W3
# %96h98@5+rU5N@q340H$B$-
# ^8)8^5x(*C7(99n
# W!1h~722K7MZ^86^9%^+Q+J06!dM%jl%1q17S&u29D$1L!!4
# 0~*5#&W23#14p)070(t
# 83p80H%J5478&wJ
# (C9b40)+0(GFB8B~1PP-~(!0)L3xg^!RG4%91!Z95I#
# Jf%f-94#~l5844Px*L51-74-7BS75URJs~U
# w!45E7S68$$)9403^^A
# #H(+E!Zd#(3~3
# xW6@$54-ih4Mk-%8&^D7+)2T#8)@9-
# ^rnp^0~J)s#8u4K@A
# (7&%V75$8sy(1T6v^q
# 9
