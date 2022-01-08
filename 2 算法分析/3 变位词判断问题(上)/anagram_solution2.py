
def anagram_solution2(word1, word2):
    word1 = list(word1)
    word2 = list(word2)

    word1.sort()
    word2.sort()
    pos = 0
    match = True
    while pos < len(word1) and match:
        if word1[pos] == word2[pos]:
            pos += 1
        else:
            match = False
    return match


print(anagram_solution2('abcd', 'dcab'))
