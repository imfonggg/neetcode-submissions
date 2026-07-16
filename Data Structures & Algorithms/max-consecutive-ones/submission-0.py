class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            elif i == 0 or i == nums[-1]:
                maxCount = max(count, maxCount)
                count = 0
        maxCount = max(count, maxCount)
        return maxCount