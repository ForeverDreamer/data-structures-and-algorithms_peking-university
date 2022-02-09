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

# 牛客网答案
# 代码1
# def checkLegal(pswd):
#     if len(pswd) <= 8:return False
#     else:
#         #最大重复子串长度2+
#         sub = []
#         for i in range(len(pswd)-2):
#             sub.append(pswd[i:i+3])
#         if len(set(sub)) < len(sub):return False
#         #check type
#         type_ = 0
#         import re
#         Upper = '[A-Z]'
#         Lowwer = '[a-z]'
#         num = '\d'
#         chars = '[^A-Za-z0-9_]'
#         patterns = [Upper, Lowwer, num, chars]
#         for pattern in patterns:
#             pw = re.search(pattern, pswd)
#             if pw : type_ += 1
#         return True if type_ >= 3 else False
# while True:
#     try:
#         pswd = input()
#         print('OK' if checkLegal(pswd) else 'NG')
#     except:
#         break


# 代码2
# def check(s):
#     if len(s) <= 8:
#         return 0
#     a, b, c, d = 0, 0, 0, 0
#     for item in s:
#         if ord('a') <= ord(item) <= ord('z'):
#             a = 1
#         elif ord('A') <= ord(item) <= ord('Z'):
#             b = 1
#         elif ord('0') <= ord(item) <= ord('9'):
#             c = 1
#         else:
#             d = 1
#     if a + b + c + d < 3:
#         return 0
#     for i in range(len(s)-3):
#         if len(s.split(s[i:i+3])) >= 3:
#             return 0
#     return 1
#
# while 1:
#     try:
#         print('OK' if check(input()) else 'NG')
#     except:
#         break
