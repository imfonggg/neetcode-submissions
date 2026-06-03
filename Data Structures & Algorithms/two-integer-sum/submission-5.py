class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idList = {}

        for index, num in enumerate(nums):
            difference = target - num
            if difference in idList:
                return [idList[difference], index]
            idList[num] = index