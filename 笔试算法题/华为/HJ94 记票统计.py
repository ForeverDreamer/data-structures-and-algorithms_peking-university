"""
HJ94 记票统计

描述
请实现一个计票统计系统。你会收到很多投票，其中有合法的也有不合法的，请统计每个候选人得票的数量以及不合法的票数。
本题有多组样例输入。

数据范围：每组输入中候选人数量满足 1≤n≤100  ，总票数量满足 1≤n≤100
输入描述：
输入候选人的人数n，第二行输入n个候选人的名字（均为大写字母的字符串），第三行输入投票人的人数，第四行输入投票。

输出描述：
按照输入的顺序，每行输出候选人的名字和得票数量（以" : "隔开，注：英文冒号左右两边都有一个空格！），最后一行输出不合法的票数，格式为"Invalid : "+不合法的票数。

示例1
输入：
4
A B C D
8
A D E CF A GG A B
复制
输出：
A : 3
B : 1
C : 0
D : 1
Invalid : 3
"""

while True:
    try:
        res={}
        n=int(input())
        arr=input().split()
        m=int(input())
        vote=input().split()
        for x in vote:
            # 如果这个票不是合法的，那么非法票数加1
            if x not in arr:
                res["Invalid"]=res.get("Invalid", 0)+1
            else:
                res[x]=res.get(x,0)+1
        # 循环遍历输出合法得票数的情况
        for name in arr:
            print(name,":",res.get(name,0))
        print("Invalid", ":", res.get("Invalid", 0))
    except:
        break
