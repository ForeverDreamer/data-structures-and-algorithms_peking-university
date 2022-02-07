"""
HJ23 删除字符串中出现次数最少的字符

描述
实现删除字符串中出现次数最少的字符，若多个字符出现次数一样，则都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
注意每个输入文件有多组输入，即多个字符串用回车隔开

数据范围：输入的字符串长度满足  ，保证输入的字符串中仅出现小写字母
输入描述：
字符串只包含小写英文字母, 不考虑非法输入，输入的字符串长度小于等于20个字节。

输出描述：
删除字符串中出现次数最少的字符后的字符串。

示例1
输入：
abcdd
aabcddd
输出：
dd
aaddd
"""

input_seq = ['abcdd', 'aabcddd']


def delete_chars(seq):
    letter_dict = {}
    output_seq = []
    for chars in seq:
        for c in chars:
            if c in letter_dict:
                letter_dict[c] += 1
            else:
                letter_dict[c] = 1
        letter_seq = list(letter_dict.items())
        letter_seq.sort(key=lambda elem: elem[1])
        # group_seq = [elem[0] for elem in group_seq]
        count = letter_seq[0][1]
        to_be_deleted = []
        for c, cnt in letter_seq:
            if count == cnt:
                to_be_deleted.append(c)
            else:
                break
        group_seq = []
        for c in chars:
            if c in to_be_deleted:
                continue
            group_seq.append(c)
        output_seq.append(''.join(group_seq))
        letter_dict.clear()

    return output_seq


for item in delete_chars(input_seq):
    print(item)
