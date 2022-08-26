"""
剑指 Offer 42. 连续子数组的最大和

输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)。

示例1:
输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

提示：
1 <= arr.length <= 10^5
-100 <= arr[i] <= 100
"""


class Solution:
    def maxSubArray(self, nums) -> int:
        dp = [nums[0]]
        continuous = [False]
        for i in range(1, len(nums)):
            if dp[i-1] > 0:
                dp.append(nums[i] + dp[i-1])
                continuous.append(True)
            else:
                dp.append(nums[i])
                continuous.append(False)
        # for i in range(1, len(nums)):
        #     nums[i] += max(nums[i - 1], 0)
        _max = max(dp)
        i = dp.index(_max)
        array = [nums[i]]
        while i >= 0 and continuous[i]:
            array.append(nums[i - 1])
            i -= 1
        return _max, array


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
