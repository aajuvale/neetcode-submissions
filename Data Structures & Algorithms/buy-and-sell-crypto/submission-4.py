class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        left = 0
        right = 0
        while right < len(prices):
            if prices[right] > prices[left]:
                result = max(result, prices[right] - prices[left])
            else:
                left = right
            right += 1
        return result
        