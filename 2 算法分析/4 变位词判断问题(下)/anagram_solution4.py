CHAR_NUM = 26


# def anagram_solution4(s1, s2):
#     c1 = [0] * 26
#     c2 = [0] * 26
#     for char in s1:
#         pos = ord(char) - ord('a')
#         c1[pos] += 1
#     for char in s2:
#         pos = ord(char) - ord('a')
#         c2[pos] += 1
#     j = 0
#     still_ok = True
#     while j < CHAR_NUM and still_ok:
#         if c1[j] == c2[j]:
#             j += 1
#         else:
#             still_ok = False
#     return still_ok


def anagram_solution4(s1, s2):
    if len(s1) != len(s2):
        return False

    d1 = {}
    d2 = {}

    for c1, c2 in zip(s1, s2):

        code1 = ord(c1)
        if code1 in d1:
            d1[code1] += 1
        else:
            d1[code1] = 1

        code2 = ord(c2)
        if code2 in d2:
            d2[code2] += 1
        else:
            d2[code2] = 1

    for key1 in d1:
        if d1.get(key1) == d2.get(key1):
            continue
        return False

    return True


print(anagram_solution4('abcd', 'dcab'))
print(anagram_solution4('李升林', '林李升'))
print(anagram_solution4('1234', '3215'))
print(anagram_solution4('寻寻觅觅', '觅觅寻寻'))
