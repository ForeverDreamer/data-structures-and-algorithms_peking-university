"""
HJ80 整型数组合并

描述
题目标题：

将两个整型数组按照升序合并，并且过滤掉重复数组元素。
输出时相邻两数之间没有空格。
请注意本题有多组样例。

输入描述：
输入说明，按下列顺序输入：
1 输入第一个数组的个数
2 输入第一个数组的数值
3 输入第二个数组的个数
4 输入第二个数组的数值

输出描述：
输出合并之后的数组

示例1
输入：
3
1 2 5
4
-1 0 3 2
输出：
-101235
"""


while True:
    try:
        num1 = int(input())
        arr1 = list(map(int, input().split()))
        num2 = int(input())
        arr2 = list(map(int, input().split()))
        arr = arr1+arr2
        list_arr = sorted(set(arr))
        res = ''.join(list(map(str,list_arr)))
        print(res)
    except:
        break
