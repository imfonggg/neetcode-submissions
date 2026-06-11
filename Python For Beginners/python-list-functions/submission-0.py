from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    sum_res = 0
    for num in nums:
        sum_res += num
    return sum_res

def get_min(nums: List[int]) -> int:
    min_res = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < min_res:
            min_res = nums[i]
    return min_res

def get_max(nums: List[int]) -> int:
    max_res = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > max_res:
            max_res = nums[i]
    return max_res

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
