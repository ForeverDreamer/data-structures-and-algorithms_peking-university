"""
HJ56 完全数计算

描述
完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。

它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。

例如：28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28。

输入n，请输出n以内(含n)完全数的个数。

数据范围： 1≤n≤5×10^5

本题输入含有多组样例。

输入描述：
输入一个数字n

输出描述：
输出不超过n的完全数的个数

示例1
输入：
1000
7
100
输出：
3
1
2

解题思路：
完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。如果一个数恰好等于它的因子之和，则称该数为“完全数”。第一个完全数是 6，它有约数 1、2、3、6，除去它本身 6 外，其余 3 个数相加，1+2+3=6。第二个完全数是 28，它有约数 1、2、4、7、14、28，除去它本身 28 外，其余 5 个数相加，1+2+4+7+14=28。第三个完全数是 496，有约数 1、2、4、8、16、31、62、124、248、496，除去其本身 496 外，其余 9 个数相加，1+2+4+8+16+31+62+124+248=496。

#coding: utf-8
#问题：1000以内的完美数
#答案：[6,28,496]
import time
#方法一：常规做法
def solution1():
	start_time = time.time()
	for n in range(1000):
		num_list = []
		for num in range(1,1000):
			sum_num = 0
			for i in range(1,num):
				if num % i == 0:
					sum_num += i
				else:
					continue
			if sum_num == num:
				num_list.append(num)
	print(num_list)
	print(time.time()-start_time)
	#运行1000次的时间：50.213872
#方法二：大于这个数1/2的公因子是不存在的
def solution2():
	start_time = time.time()
	for n in range(1000):
		num_list = []
		for num in range(1,1000):
			sum_num = 0
			for i in range(1,int(num/2)+1):
				if num % i == 0:
					sum_num += i
				else:
					continue
			if sum_num == num:
				num_list.append(num)
	print(num_list)
	print(time.time()-start_time)
	#运行1000次的时间：25.8714797
#方法三：一对因子总会发布在这个数的根号两边，或者就是这平方根值
def solution3():
	start_time = time.time()
	for n in range(1000):
		num_list = []
		for num in range(2,1000):#从1开始，会把1也写入数组
			sum_num = 1#每个数都会有个因子是1
			for i in range(2,int(pow(num,1/2)+1)):#从2开始，防止把num写入数组
				if num % i == 0:
					res = int(num/i)
					if res == i:#判断是不是恰好是平方根
						sum_num += i#正好是平方根，只写入一个数据
					else:
						sum_num += (i+res)#把一对因子写入
				else:
					continue
			if sum_num == num:
				num_list.append(num)
	print(num_list)
	print(time.time()-start_time)
	#运行1000次的时间：4.66926717758
if __name__ == '__main__':
	solution3()
PS:好像有公式和素数、质数相关？欧拉公式？我数学不好，不是很懂。如果能直接生成完美数就好了。
————————————————
版权声明：本文为CSDN博主「qq_41807327」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_41807327/article/details/102983896


牛客网答案
看了一些提交记录，里面是默认知道完全数为：6/28/496/8128。如果不知道具体的完全数是多少，如何在有限的时间和运存大小下找到完全数？仅仅只用了一些小学数学常识，参考了一个博客指路：

常规思路，复杂度很高O(n^2)

import sys
for s in sys.stdin:
 m=int(s)
 num=[]
 for i in range(1,m):
     s=0
     for k in range(1,i):
         if i%k==0:
             s=s+k
     if i==s:
         num.append(s)
 print(len(num))
执行结果： 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。 用例通过率: 90.00% 运行时间: 2001ms 占用内存: 3360KB
2.大于这个数1/2的公因子是不存在的，第二次循环次数减少了一半
import sys
for s in sys.stdin:
    m=int(s)
    num=[]
    for i in range(1,m):
        s=0
        for k in range(1,int(i/2+1)):
            if i%k==0:
                s=s+k
        if i==s:
            num.append(s)

    print(len(num))
运行时间：995ms 占用内存：3372k

3.一对因子总会发布在这个数的根号两边，或者就是这平方根值。再次减少第二次循环的复杂度
import sys
for s in sys.stdin:
    m=int(s)
    num=[]
    for i in range(2,m):#1不算
        s=1#每个数都会有个因子是1
        for k in range(2,int(pow(i,1/2)+1)):#不将1和本身写入因子中
        #print(k)
            if i%k==0:
            #print("一")
                res=i/k
                if k==res:#为平方根
                    s=s+k
                #print("二",s)
                else:
                    s=s+k+res
                #print("三",s)
        if i==s:
            num.append(s)
    print(len(num))
运行时间：73ms 占用内存：3416k

备注：牛客上编程输入，写input经常会出错，要写成：

import sys
for s in sys.stdin:
    m=int(s)
也不知道为什么。。。。
另外最后一行print的位置
"""

import sys

for s in sys.stdin:
    m = int(s)
    num = []
    for i in range(1, m):
        s = 0
        for k in range(1, int(i / 2 + 1)):
            if i % k == 0:
                s = s + k
        if i == s:
            num.append(s)

    print(len(num))
