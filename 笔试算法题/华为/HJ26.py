"""
HJ26 字符串排序

描述
编写一个程序，将输入字符串中的字符按如下规则排序。
规则 1 ：英文字母从 A 到 Z 排列，不区分大小写。
如，输入： Type 输出： epTy
规则 2 ：同一个英文字母的大小写同时存在时，按照输入顺序排列。
如，输入： BabA 输出： aABb
规则 3 ：非英文字母的其它字符保持原来的位置。
如，输入： By?e 输出： Be?y
注意有多组测试数据，即输入有多行，每一行单独处理（换行符隔开的表示不同行）

数据范围：输入的字符串长度满足

输入描述：
输入字符串
输出描述：
输出字符串
示例1
输入：
A Famous Saying: Much Ado About Nothing (2012/8).
输出：
A aaAAbc dFgghh: iimM nNn oooos Sttuuuy (2012/8).
"""

from string import ascii_lowercase

input_seq = ['A Famous Saying: Much Ado About Nothing (2012/8).']


def chars_sort(seq):
    output_seq = []
    for chars in seq:
        # length_seq = [len(word) for word in chars.split(' ')]
        symbol_pos = {}
        lower_chars = chars.lower()
        group_seq = []
        pos = 0
        for l_char, char in zip(lower_chars, chars):
            if l_char in ascii_lowercase:
                if len(group_seq) == 0:
                    group_seq.append(char)
                    pos += 1
                    continue
                idx = 0
                inserted = False
                while idx < len(group_seq):
                    c = group_seq[idx].lower()
                    if c in ascii_lowercase:
                        if l_char >= c:
                            idx += 1
                            continue
                        else:
                            group_seq.insert(idx, char)
                            inserted = True
                            idx += 1
                            break
                    elif c == ' ':
                        pass
                    else:
                        idx += 1
                        continue

                if not inserted:
                    group_seq.append(char)
            else:
                # group_seq.append(char)
                if char in symbol_pos:
                    symbol_pos[char].append(pos)
                else:
                    symbol_pos[char] = [pos]
            pos += 1
        # group_str = ''
        # for c in group_seq:
        #     group_str += c
        # group_seq = ''.join(group_seq)
        # group_str = ''
        # idx = 0
        # for length in length_seq:
        #     group_str += group_seq[idx:idx+length]
        #     group_str += ' '
        #     idx += length
        symbol_pos_tuples = []
        for symbol in symbol_pos:
            for pos in symbol_pos[symbol]:
                symbol_pos_tuples.append((symbol, pos))
        symbol_pos_tuples.sort(key=lambda elem: elem[1])
        for symbol, pos in symbol_pos_tuples:
            group_seq.insert(pos, symbol)
        output_seq.append(''.join(group_seq))

    return output_seq


for item in chars_sort(input_seq):
    print(item)
