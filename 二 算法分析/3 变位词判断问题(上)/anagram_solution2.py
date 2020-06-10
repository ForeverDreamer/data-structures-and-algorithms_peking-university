
def anagram_solution2(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()
    pos = 0
    match = True
    while pos < len(s1) and match:
        if alist1[pos] == alist2[pos]:
            pos += 1
        else:
            match = False
    return match


print(anagram_solution2('abcd', 'dcab'))
