"""
HJ107 求解立方根

描述
计算一个浮点数的立方根，不使用库函数。
保留一位小数。

数据范围：∣val∣≤20

输入描述：
待求解参数，为double类型（一个实数）

输出描述：
输入参数的立方根。保留一位小数。

示例1
输入：
216
复制
输出：
6.0
复制
示例2
输入：
2.7
复制
输出：
1.4
"""

# 代码1
import sys

def cube():
    num = float(sys.stdin.readline().strip())
    if num == 0:
        return 0
    if num > 0:
        sig = 1
    else:
        sig = -1
    num = abs(num)

    if num > 1:
        start = 0
        end = num
    else:
        start = num
        end = 1
    mid = (end + start) / 2
    while abs(mid ** 3 - num) > 0.001:
        if mid ** 3 > num:
            end = mid
        else:
            start = mid
        mid = (end + start) / 2
    print(round(sig * mid, 1))

cube()


# 代码2
# while True:
#     try:
#         Num = float(input())
#         if Num<0:
#             N_flag = -1
#             Num = (-1)*Num
#         elif Num == 0:
#             result = 0
#         else:
#             N_flag = 1
#         i = 0
#         while(i**3<=Num):
#             i+=1
#         j=0
#         while((i-1)+j*0.1)**3 <= Num:
#             j+=1
#         k=0  #为了对小数点后第二位进行四舍五入，需要计算到第二位。
#         while((i-1)+(j-1)*0.1+k*0.01)**3 <= Num:
#             k+=1
#         if k>=5:  #四舍五入
#             result =(i-1 + (j)*0.1) * N_flag  #注意处理负数
#         else:
#             result =(i-1 + (j-1)*0.1) * N_flag
#         #print(result)
#         print(round(result,1))  ##最坑莫过于此，要取round
#     except:
#         break

