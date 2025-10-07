class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mini = prices[0]
        maxProfit = 0

        for i in range(1,len(prices)):
            profit = prices[i]-mini
            maxProfit = max(profit,maxProfit)
            mini = min(mini,prices[i])
        return maxProfit

        
        