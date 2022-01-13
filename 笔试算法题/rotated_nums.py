rotated_nums1 = []
rotated_nums2 = [1]
rotated_nums3 = [2, 1]
rotated_nums4 = [1, 2]
rotated_nums5 = [1, 2, 3, 4, 5, 6, 7]
rotated_nums6 = [5, 6, 7, 1, 2, 3, 4]
rotated_nums7 = [2, 3, 4, 5, 6, 7, 1]
rotated_nums8 = [5, 6, 7, 8, 1, 2, 3, 4]


def find_min(nums):
    if len(nums) == 0:
        return '数组不能为空'
    if len(nums) == 1:
        return nums[0]
    # 只有两个数直接比较
    if len(nums) == 2:
        return nums[0] if nums[0] < nums[1] else nums[1]
    # 数组未旋转
    if nums[0] < nums[-1] and nums[0] < nums[1]:
        return nums[0]
    left = 0
    right = len(nums)-1
    # 旋转过的数组总是nums[0] > nums[-1]，首尾同时向中间扫描，时间复杂度最多O(n/2)
    while right > left:
        if nums[left] > nums[left+1]:
            return nums[left+1]
        if nums[right-1] > nums[right]:
            return nums[right]
        left += 1
        right -= 1
    return '数据错误'


print(find_min(rotated_nums1))
print(find_min(rotated_nums2))
print(find_min(rotated_nums3))
print(find_min(rotated_nums4))
print(find_min(rotated_nums5))
print(find_min(rotated_nums6))
print(find_min(rotated_nums7))
print(find_min(rotated_nums8))
