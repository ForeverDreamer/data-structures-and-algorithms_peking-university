""""
HJ64 MP3光标位置

描述
MP3 Player因为屏幕较小，显示歌曲列表的时候每屏只能显示几首歌曲，用户要通过上下键才能浏览所有的歌曲。为了简化处理，假设每屏只能显示4首歌曲，光标初始的位置为第1首歌。


现在要实现通过上下键控制光标移动来浏览歌曲列表，控制逻辑如下：

歌曲总数<=4的时候，不需要翻页，只是挪动光标位置。

光标在第一首歌曲上时，按Up键光标挪到最后一首歌曲；光标在最后一首歌曲时，按Down键光标挪到第一首歌曲。



其他情况下用户按Up键，光标挪到上一首歌曲；用户按Down键，光标挪到下一首歌曲。



2. 歌曲总数大于4的时候（以一共有10首歌为例）：


特殊翻页：屏幕显示的是第一页（即显示第1 – 4首）时，光标在第一首歌曲上，用户按Up键后，屏幕要显示最后一页（即显示第7-10首歌），同时光标放到最后一首歌上。同样的，屏幕显示最后一页时，光标在最后一首歌曲上，用户按Down键，屏幕要显示第一页，光标挪到第一首歌上。



一般翻页：屏幕显示的不是第一页时，光标在当前屏幕显示的第一首歌曲时，用户按Up键后，屏幕从当前歌曲的上一首开始显示，光标也挪到上一首歌曲。光标当前屏幕的最后一首歌时的Down键处理也类似。



其他情况，不用翻页，只是挪动光标就行。

数据范围：本题含有多组输入数据，数据组数1≤t≤5 ，命令长度1≤s≤100 ，歌曲数量1≤n≤150
进阶：时间复杂度：O(n) ，空间复杂度：O(n)
输入描述：
输入说明：
1 输入歌曲数量
2 输入命令 U或者D

本题含有多组输入数据！

输出描述：
输出说明
1 输出当前列表
2 输出当前选中歌曲

示例1
输入：
10
UUUU
输出：
7 8 9 10
7
"""

input_seq = [
    '2', 'DUDUDDUUDUDDDDUDUDDDUUDDUDDUDUDUDDDUDUDUUDDUUDDUUUDUDUUUDDUDUDDUUDUDDDDUDUDUUDUDDDDDUU',
    '10', 'UUUU',
    '83', 'UUDUDDDDUDUUDDDDUDD',
    '81', 'DDUUUDUUDDUDUUUUDUDDDDDUDUUDDUUDUDDUUUDUUUUUDDDDUDDDUUUDUUUDDDDDUDDDDDUDDDDDUDDUDDDDU'
]


def execute(n, moves):
    screen_size = 4

    songs_idx = screen_idx = 1
    if n <= screen_size:
        for move in moves:
            if move == 'U':
                if songs_idx == 1:
                    songs_idx = n
                else:
                    songs_idx -= 1
            else:
                if songs_idx == n:
                    songs_idx = 1
                else:
                    songs_idx += 1
    else:
        for move in moves:
            if move == 'U':
                if screen_idx == 1:
                    if songs_idx == 1:
                        screen_idx = screen_size
                        songs_idx = n
                    else:
                        songs_idx -= 1
                else:
                    songs_idx -= 1
                    screen_idx -= 1
            else:
                if screen_idx == screen_size:
                    if songs_idx == n:
                        screen_idx = 1
                        songs_idx = 1
                    else:
                        songs_idx += 1
                else:
                    songs_idx += 1
                    screen_idx += 1

    start_idx = songs_idx-screen_idx+1
    size = screen_size if n > screen_size else n
    print(' '.join([str(i) for i in range(start_idx, start_idx+size)]))
    print(songs_idx)


def mp3_cursor(seq):
    output_seq = []
    i = 0
    while i+1 < len(seq):
        n = seq[i]
        moves = seq[i+1]
        output_seq.append(execute(int(n), moves))
        i += 2


mp3_cursor(input_seq)
