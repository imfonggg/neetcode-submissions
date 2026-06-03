class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i, 0);
        count_sorted = dict(sorted(count.items(), key = lambda x:x[1], reverse = True))
        arr = list(count_sorted.keys())

        for i in range(k , len(arr)):
            arr.pop()

        return arr