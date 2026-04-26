from typing import DefaultDict, List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences = DefaultDict[int, int]()
        for n in nums:
            occurences[n] = occurences.get(n, 0) + 1

        buckets: List[List] = [[] for _ in range(len(nums) + 1)]
        for key, v in occurences.items():
            buckets[v].append(key)

        
        result = []
        for i in range(len(nums), 0, -1):
            if buckets[i]:
                result.extend(buckets[i])
            if len(result) >= k:
                return result[:k]

        return result
