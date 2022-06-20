class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        mx=0
        
        for i in range(1,len(prices)):
            
            #since we can sell and buy on the same day we greedly sell whenever we get a larger price and then since we buy at the same price it won't matter if we get a larger price down the line as our net profit would be same for instance 7 5 10 12 buy at 5 sell at 10 buy at 10 sell at 12
            if prices[i]>prices[i-1]:
                mx+=prices[i]-prices[i-1]
                
                
        return mx