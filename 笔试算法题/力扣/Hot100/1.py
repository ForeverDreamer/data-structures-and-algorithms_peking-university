

def two_sum(nums, target):
    dic = {}
    i = 0
    while i < len(nums):
        n = target-nums[i]
        if n in dic:
            return [dic[n], i]
        dic[nums[i]] = i
        i += 1


print(two_sum([2, 7, 11, 15], 9))
