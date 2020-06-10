CHAR_NUM = 26


def anagram_solution4(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26
    for char in s1:
        pos = ord(char) - ord('a')
        c1[pos] += 1
    for char in s2:
        pos = ord(char) - ord('a')
        c2[pos] += 1
    j = 0
    still_ok = True
    while j < CHAR_NUM and still_ok:
        if c1[j] == c2[j]:
            j += 1
        else:
            still_ok = False
    return still_ok


print(anagram_solution4('abcd', 'dcab'))
