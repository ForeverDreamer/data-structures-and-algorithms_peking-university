
def anagram_solution1(word1, word2):
    if len(word1) != len(word2):
        return False

    word2 = list(word2)
    pos1 = 0
    is_anagram = True

    while pos1 < len(word1):
        pos2 = 0
        found = False
        while pos2 < len(word2):
            if word1[pos1] == word2[pos2]:
                found = True
                break
            else:
                pos2 += 1
        if found:
            del word2[pos2]
        else:
            is_anagram = False
            break
        pos1 += 1
    return is_anagram


print(anagram_solution1('abcd', 'dcab'))
