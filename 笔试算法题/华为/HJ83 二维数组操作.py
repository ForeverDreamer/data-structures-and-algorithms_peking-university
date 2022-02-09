"""
HJ83 二维数组操作
"""

# 牛客网答案
# 代码1
# while True:
#     try:
#         m, n = map(int, input().split())
#         x1, y1, x2, y2=map(int,input().split())
#         insert_x=int(input())
#         insert_y=int(input())
#         x,y=map(int,input().split())
#         if (0 <= m <= 9) and (0 <= n <= 9):
#             print('0')
#         else:
#             print('-1')
#         if (0 <= x1 < m) and (0 <= y1 < n) and (0 <= x2 <= m)and (0 <= y2 < n):
#             print('0')
#         else:
#             print('-1')
#         if (0 <= insert_x < m) and (m < 9):
#             print('0')
#         else:
#             print('-1')
#         if (0 <= insert_y < n) and (n < 9):
#             print('0')
#         else:
#             print('-1')
#         if(0 <= x < m)and (0 <= y < n):
#             print('0')
#         else:
#             print('-1')
#     except:
#         break


# 代码2
while True:
    try:
        # 初始化表格
        m, n = map(int, input().split())
        if m > 9 or n > 9:
            print('-1')
        else:
            print('0')

        # 交换坐标
        x1, y1, x2, y2 = map(int, input().split())
        if 0 <= x1 < m and 0 <= x2 < m and 0 <= y1 < n and 0 <= y2 < n:
            print('0')
        else:
            print('-1')

        # 插入行
        x = int(input())
        if m < 9 and 0 <= x < m:
            print('0')
        else:
            print('-1')

        # 插入列
        y = int(input())
        if n < 9 and 0 <= y < n:
            print('0')
        else:
            print('-1')

        # 查找坐标
        x, y = input().split()
        x, y = int(x), int(y)
        if 0 <= x < m and 0 <= y < n:
            print('0')
        else:
            print('-1')

    except EOFError:
        break

