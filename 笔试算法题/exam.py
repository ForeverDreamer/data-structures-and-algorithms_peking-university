"""第1题"""


def str_to_num(s):

    if not isinstance(s, str) or s == '':
        raise TypeError('仅接受非空字符串类型参数！')
    try:
        return int(s)
    except ValueError:
        num_code = (range(48, 58))
        comma_code = ord(',')
        num_str = []
        for c in s:
            if ord(c) in num_code:
                num_str.append(c)
            elif ord(c) == comma_code:
                continue
            else:
                raise ValueError('字符串中仅能包含数字和逗号！')
        if num_str:
            return ''.join(num_str)
        else:
            raise ValueError('字符串中没有有数字！')


# 非数字
# str_to_num([])
# 空字符
# str_to_num('')
# 包含非数字或逗号的字符串
# str_to_num('29,ks')
# 全是逗号
# print(str_to_num(',,,,,'))
# 数字
# print(str_to_num('292543'))
# 数字加逗号
print(str_to_num('29,254,3'))


"""第2题"""


def find_list_max(l):
    if not isinstance(l, list) or len(l) == 0:
        raise ValueError('只接受非空整数列表参数！')
    elif len(l) == 1:
        return l[0]
    elif len(l) == 2:
        return l[0] if l[0] > l[1] else l[1]
    left_index = len(l) // 2
    right_index = left_index + 1
    max_num = l[left_index]
    while left_index >= 0 and right_index < len(l):
        if (not isinstance(l[left_index], int)) or (not isinstance(l[right_index], int)):
            raise ValueError('列表元素只能是整数！')
        max_num = l[left_index] if l[left_index] > max_num else max_num
        max_num = l[right_index] if l[right_index] > max_num else max_num
        left_index -= 1
        right_index += 1
    return max_num


# 非列表类型
# find_list_max('sdf')
# 空列表
# find_list_max([])
# 列表元素非整数
# find_list_max([1, 2, 3, '5', 4])
# 列表元素都是整数
print(find_list_max([1, 2, 12, 35, 68, 45, 21, 12, 11]))
