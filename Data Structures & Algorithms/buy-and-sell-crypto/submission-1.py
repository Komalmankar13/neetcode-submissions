class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minProfit = prices[0]
        maxProfit = 0
        for i in range(1,len(prices)):
            profit = prices[i] - minProfit
            maxProfit = max(maxProfit, profit)
            minProfit = min(minProfit, prices[i])
        
        return maxProfit