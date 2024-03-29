"""
HJ25 数据分类处理

描述
信息社会，有海量的数据需要分析处理，比如公安局分析身份证号码、 QQ 用户、手机号码、银行帐号等信息及活动记录。

采集输入大数据和分类规则，通过大数据分类处理程序，将大数据分类输出。

请注意本题有多组输入用例。

数据范围：1 \le I,R \le 100 \1≤I,R≤100  ，输入的整数大小满足 0 \le val \le 2^{31}-1\0≤val≤2
31
 −1
输入描述：
﻿一组输入整数序列I和一组规则整数序列R，I和R序列的第一个整数为序列的个数（个数不包含第一个整数）；整数范围为0~(2^31)-1，序列个数不限

输出描述：
﻿从R依次中取出R<i>，对I进行处理，找到满足条件的I：

I整数对应的数字需要连续包含R<i>对应的数字。比如R<i>为23，I为231，那么I包含了R<i>，条件满足 。

按R<i>从小到大的顺序:

(1)先输出R<i>；

(2)再输出满足条件的I的个数；

(3)然后输出满足条件的I在I序列中的位置索引(从0开始)；

(4)最后再输出I。

附加条件：

(1)R<i>需要从小到大排序。相同的R<i>只需要输出索引小的以及满足条件的I，索引大的需要过滤掉

(2)如果没有满足条件的I，对应的R<i>不用输出

(3)最后需要在输出序列的第一个整数位置记录后续整数序列的个数(不包含“个数”本身)



序列I：15,123,456,786,453,46,7,5,3,665,453456,745,456,786,453,123（第一个15表明后续有15个整数）

序列R：5,6,3,6,3,0（第一个5表明后续有5个整数）

输出：30, 3,6,0,123,3,453,7,3,9,453456,13,453,14,123,6,7,1,456,2,786,4,46,8,665,9,453456,11,456,12,786

说明：

30----后续有30个整数

3----从小到大排序，第一个R<i>为0，但没有满足条件的I，不输出0，而下一个R<i>是3

6--- 存在6个包含3的I

0--- 123所在的原序号为0

123--- 123包含3，满足条件

示例1
输入：
15 123 456 786 453 46 7 5 3 665 453456 745 456 786 453 123
5 6 3 6 3 0
复制
输出：
30 3 6 0 123 3 453 7 3 9 453456 13 453 14 123 6 7 1 456 2 786 4 46 8 665 9 453456 11 456 12 786
复制
说明：
将序列R：5,6,3,6,3,0（第一个5表明后续有5个整数）排序去重后，可得0,3,6。
序列I没有包含0的元素。
序列I中包含3的元素有：I[0]的值为123、I[3]的值为453、I[7]的值为3、I[9]的值为453456、I[13]的值为453、I[14]的值为123。
序列I中包含6的元素有：I[1]的值为456、I[2]的值为786、I[4]的值为46、I[8]的值为665、I[9]的值为453456、I[11]的值为456、I[12]的值为786。
最后按题目要求的格式进行输出即可。
"""


# 牛客网答案
while True:
    try:
        s1 = input().split()[1:]
        s2 = list(set(map(int, input().split()[1:])))
        s2.sort()
        rst = []
        for num in s2:
            tmp = []
            for i, sub in enumerate(s1):
                if str(num) in sub:
                    tmp.extend([str(i), str(sub)])
            if tmp:
                rst.extend([str(num), str(len(tmp)//2)] + tmp)
        print(str(len(rst)) + " " + " ".join(rst))
    except:
        break


# 备用代码
# while True:
#     try:
#         I=input().split()#按空格分成列表
#         R=input().split()
#         m=int(I.pop(0))#取第一个元素作为个数
#         n=int(R.pop(0))
#         for i in range(n):#字符串->整数，为了后面的排序
#             R[i]=int(R[i])
#         R=set(R)#去重
#         R=sorted(R)#排序
#         count=0#记录R中的元素在I中出现的总次数
#         num=0#记录R中有几个元素是I中元素的子串
#         flag0=False#标识位，标识当前R中元素是否是I中某元素的子串
#         for i in R:
#             for j in I:
#                 if str(i) in j:
#                     flag0=True#说明该元素至少是I中一个元素的子串
#                     count+=1
#             if flag0:
#                 num+=1
#                 flag0=False#每次循环结束置为false，为了下一个元素的判断
#         count=(count+num)*2#要输出的第一个数，表示后面元素的个数
#         #输出时，因为有位置信息所以count*2，又要输出元素和总次数
#         #因此num*2
#         print(count,end='')#按格式输出，以‘’结尾，下次输出紧跟着
#         for i in R:
#             num=0
#             for j in I:
#                 if str(i) not in j:
#                     continue
#                 flag0=True#说明该元素至少是I中一个元素的子串，有效
#                 num+=1#num记录当前元素是几个元素的子串
#             if not flag0:#如果该元素无效，跳过
#                 continue
#             print(' '+str(i)+' '+str(num),end='')#按格式
#             for index,j in enumerate(I):
#                 if str(i) in j:
#                     print(' '+str(index)+' '+j,end='')
#             flag0=False#同样置false，为了下个元素的判断
#         print()#这是为了换行，不然会过不了测试
#     except:
#         break