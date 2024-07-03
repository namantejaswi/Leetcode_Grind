class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        mi = prices[0]
        mx_profit = 0
        
        for i in range(1, len(prices)):
            
            mx_profit = max(mx_profit, prices[i]-mi)
            mi = min(mi,prices[i])
            
            
        return mx_profit