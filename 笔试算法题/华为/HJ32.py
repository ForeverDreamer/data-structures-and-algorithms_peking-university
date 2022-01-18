"""
HJ32 密码截取

描述
Catcher是MCA国的情报员，他工作时发现敌国会用一些对称的密码进行通信，比如像这些ABBA，ABA，A，123321，但是他们有时会在开始或结束时加入一些无关的字符以防止别国破解。比如进行下列变化 ABBA->12ABBA,ABA->ABAKK,123321->51233214　。因为截获的串太长了，而且存在多种可能的情况（abaaab可看作是aba,或baaab的加密形式），Cathcer的工作量实在是太大了，他只能向电脑高手求助，你能帮Catcher找出最长的有效密码串吗？

数据范围：字符串长度满足
输入描述：
输入一个字符串（字符串的长度不超过2500）

输出描述：
返回有效密码串的最大长度

示例1
输入：
ABBA
输出：
4

示例2
输入：
ABBBA
输出：
5

示例3
输入：
12HHHHA
输出：
4

解题思路
（1）按题目要求即找到从中间位置开始往左右两边扩展能保持对称的最大字符串长度

（2）字符串长度为偶数时，对称中线左右两边的字符相等，即

string[i] == string[i+1]
（3）字符串长度为奇数时，对称中心字符左右两边的字符相等，即

string[i-1] == string[i+1]
（4）从中心点index出发，向两边寻找，元素相等则最大长度+2，否则输出当前最大长度
"""
input_seq = ['ABBA', 'ABBBA', '12HHHHA']


def is_palindrome(chars):
    start = 0
    end = len(chars)-1
    equal = True
    while equal and start < end:
        if chars[start] != chars[end]:
            equal = False
        else:
            start += 1
            end -= 1
    return equal


def max_len(seq):
    output_seq = []
    for line in seq:
        i = 0
        maximum = 1
        while i < len(line):
            length = 1
            while i + length <= len(line):
                chars = line[i:i+length]
                if is_palindrome(chars) and length > maximum:
                    maximum = length
                length += 1
            i += 1
        output_seq.append(maximum)

    return output_seq


for item in max_len(input_seq):
    print(item)
