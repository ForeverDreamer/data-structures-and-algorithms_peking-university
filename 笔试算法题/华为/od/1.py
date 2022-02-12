"""
两个班的小朋友混合排队，每个小朋友都知道前面一个是不是同一个班的，需要把两个班的小朋友分开，
每个班占一行，按编号升序输出，第一个编号小的班先输出，如果只有一个班只输出一行，
输入数据格式错误直接输出ERROR
"""


students = ['1/N', '2/Y', '3/N', '4/Y']


def validate_input(stu):
    try:
        num = int(stu.split('/')[0])
    except ValueError:
        print('ERROR')
        exit()
        return None
    return num


def same_class(stus):
    tmp = []
    cls1 = set()
    cls2 = set()
    i = len(stus)-1
    same = True
    last_cls = None
    same_cls_stus = []
    while i >= 0:
        num, flag = stus[i].split('/')

        if flag == 'Y':
            same_cls_stus.append((stus[i-1].split('/')[0], num))
        # num = int(num)
        # if flag == 'Y':
        #     if same:
        #         last_cls.add(stus[i-1].split('/')[0])
        #         last_cls.add(num)
        #     if num in cls1:
        #         cls1.add(stus[i-1].split('/')[0])
        #         cls1.add(num)
        #         last_cls = cls1
        #     else:
        #         cls2.add(stus[i-1].split('/')[0])
        #         cls2.add(num)
        #         last_cls = cls2
        # else:
        #     same = False
        #     tmp.append(num)
        i -= 1
    i = 0
    while i+1 < len(same_cls_stus):
        first = set(same_cls_stus[i])
        second = set(same_cls_stus[i+1])
        if first.intersection(second):
            cls1.update(second)
        else:
            cls2.update(second)
        i += 1
    left_pair = set(same_cls_stus[0])
    if cls1.intersection(left_pair):
        cls1.update(left_pair)
    else:
        cls2.update(left_pair)
    cls1 = sorted(list(cls1))
    cls2 = sorted(list(cls2))
    if len(cls1) == 0:
        print(' '.join(cls2))
        print()
        return
    if len(cls2) == 0:
        print(' '.join(cls1))
        print()
        return
    if cls1[0] < cls2[0]:
        print(' '.join(cls1))
        print(' '.join(cls2))
    else:
        print(' '.join(cls2))
        print(' '.join(cls1))


same_class(students)
