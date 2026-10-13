class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        for i in range(1,len(prices)):
            for j in range(i,len(prices)):
                profit = prices[j] - prices[i-1]
                maxprofit = max(profit, maxprofit)
        
        return maxprofit