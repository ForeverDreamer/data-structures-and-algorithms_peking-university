"""
剑指 Offer 51. 数组中的逆序对

在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

 

示例 1:

输入: [7,5,6,4]
输出: 5
 

限制：

0 <= 数组长度 <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# class Solution:
#     def reversePairs(self, nums) -> int:
#         def merge_sort(l, r):
#             # 终止条件
#             if l >= r: return 0
#             # 递归划分
#             m = (l + r) // 2
#             res = merge_sort(l, m) + merge_sort(m + 1, r)
#             # 合并阶段
#             i, j = l, m + 1
#             tmp[l:r + 1] = nums[l:r + 1]
#             for k in range(l, r + 1):
#                 # 无逆序对
#                 if i == m + 1:
#                     nums[k] = tmp[j]
#                     j += 1
#                 # 无逆序对
#                 elif j == r + 1 or tmp[i] <= tmp[j]:
#                     nums[k] = tmp[i]
#                     i += 1
#                 # 统计逆序对
#                 else:
#                     nums[k] = tmp[j]
#                     j += 1
#                     res += m - i + 1  # 统计逆序对
#             return res
#
#         tmp = [0] * len(nums)
#         return merge_sort(0, len(nums) - 1)


class Solution:
    def reversePairs(self, nums) -> int:
        count = 0

        def merge_sort(nums):
            # 递归结束条件
            if len(nums) <= 1:
                return nums

            nonlocal count
            # 分解问题，递归调用
            middle = len(nums) // 2
            left = merge_sort(nums[:middle])  # 左半部分排好序
            right = merge_sort(nums[middle:])  # 右半部分排好序

            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] > right[j]:
                    merged.append(right[j])
                    count += len(left) - i
                    j += 1
                else:
                    merged.append(left[i])
                    i += 1

            merged.extend(right[j:] if right[j:] else left[i:])
            return merged

        print(merge_sort(nums))
        return count


print(Solution().reversePairs([7, 3, 2, 6, 0, 1, 5, 4]))
