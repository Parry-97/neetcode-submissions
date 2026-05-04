class Solution:
    # NOTE: We could simple use two pointer approach and maximize it
    # like maximize it the most waiter
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        left = 0
        right = left + 1

        max_profit = float("-inf")

        while right < len(prices):
            current_profit = prices[right] - prices[left]
            max_profit = max(max_profit, current_profit)
            if current_profit < 0:
                left = right
            right += 1

        return int(max_profit) if max_profit > 0 else 0