"""
HJ31 单词倒排

描述
对字符串中的所有单词进行倒排。

说明：
1、构成单词的字符只有26个大写或小写英文字母；
2、非构成单词的字符均视为单词间隔符；
3、要求倒排后的单词间隔符以一个空格表示；如果原字符串中相邻单词间有多个间隔符时，倒排转换后也只允许出现一个空格间隔符；
4、每个单词最长20个字母；

数据范围：字符串长度满足
输入描述：
输入一行以空格来分隔的句子

输出描述：
输出句子的逆序

示例1
输入：
I am a student
输出：
student a am I

示例2
输入：
$bo*y gi!r#l
输出：
l r gi y bo
"""

from string import ascii_lowercase, ascii_uppercase

input_seq = ['I am a student', '$bo*y gi!r#l']


def reverse_words(seq):
    output_seq = []
    for line in seq:
        group_seq = []
        previous_char = ''
        for c in line:
            if c in ascii_lowercase or c in ascii_uppercase:
                group_seq.append(c)
                previous_char = c
            else:
                if previous_char != ' ':
                    group_seq.append(' ')
        group_seq = ''.join(group_seq).strip().split(' ')[::-1]
        output_seq.append(' '.join(group_seq))
    return output_seq


for item in reverse_words(input_seq):
    print(item)
