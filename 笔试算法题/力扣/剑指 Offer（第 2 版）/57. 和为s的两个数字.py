"""
剑指 Offer 57. 和为s的两个数字

输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]

示例 2：
输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]

限制：
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6

解题思路：
利用 HashMap 可以通过遍历数组找到数字组合，时间和空间复杂度均为 O(N)O(N) ；
注意本题的 numsnums 是 排序数组 ，因此可使用 双指针法 将空间复杂度降低至 O(1)O(1) 。

算法流程：
初始化： 双指针 ii , jj 分别指向数组 numsnums 的左右两端 （俗称对撞双指针）。
循环搜索： 当双指针相遇时跳出；
计算和 s = nums[i] + nums[j]s=nums[i]+nums[j] ；
若 s > targets>target ，则指针 jj 向左移动，即执行 j = j - 1j=j−1 ；
若 s < targets<target ，则指针 ii 向右移动，即执行 i = i + 1i=i+1 ；
若 s = targets=target ，立即返回数组 [nums[i], nums[j]][nums[i],nums[j]] ；
返回空数组，代表无和为 targettarget 的数字组合。
"""


class Solution:
    def twoSum(self, nums, target: int):
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else:
                return nums[i], nums[j]
        return []
