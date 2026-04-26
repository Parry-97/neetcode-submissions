class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numset = set(nums)
        max_count = 1
        for n in nums:
            if (n - 1) not in numset:
                current_count = 1
                seq = n + 1
                while seq in numset:
                    current_count += 1
                    seq += 1
                max_count = max(max_count, current_count)

        return max_count