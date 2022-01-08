"""{1}--401什么是递归13m20s"""


def list_sum_accumulation(nums):
    total = 0
    for n in nums:
        total = total + n
    return total


def list_sum_recursion_1(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + list_sum_recursion_1(nums[1:])


def list_sum_recursion_2(nums):
    if len(nums) == 2:
        return nums[0] + nums[1]
    else:
        return nums[0] + list_sum_recursion_2(nums[1:])


if __name__ == '__main__':
    print(list_sum_recursion_1([1, 3, 5, 7, 9]))
    print(list_sum_recursion_2([1, 3, 5, 7, 9]))
