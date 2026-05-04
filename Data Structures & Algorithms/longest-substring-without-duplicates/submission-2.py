class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        right = left + 1

        max_len = 1

        current_sub = set(s[left])
        while right < len(s):
            if s[right] in current_sub:
                max_len = max(len(current_sub), max_len)
                left += 1
                right = left + 1
                current_sub = set(s[left])
            else:
                current_sub.add(s[right])
                right += 1

        return max(len(current_sub), max_len)