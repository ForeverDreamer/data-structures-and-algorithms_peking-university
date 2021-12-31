"""{1}--401什么是递归13m20s"""


def list_sum_accumulation(nums):
    total = 0
    for n in nums:
        total = total + n
    return total


def list_sum_recursion(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + list_sum_recursion(nums[1:])


if __name__ == '__main__':
    print(list_sum_recursion([1, 3, 5, 7, 9]))
