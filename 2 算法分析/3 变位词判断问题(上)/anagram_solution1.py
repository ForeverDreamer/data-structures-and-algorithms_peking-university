
def anagram_solution1(word1, word2):
    word2 = list(word2)
    pos1 = 0
    still_ok = True
    while pos1 < len(word1) and still_ok:
        pos2 = 0
        found = False
        while pos2 < len(word2) and not found:
            if word1[pos1] == word2[pos2]:
                found = True
            else:
                pos2 += 1
        if found:
            del word2[pos2]
        else:
            still_ok = False
        pos1 += 1
    return still_ok


print(anagram_solution1('abcd', 'dcab'))
