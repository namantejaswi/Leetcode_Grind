class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        #unbounded knapsack
        
        
        dp = [[ -1 for i in range(amount+1)]for j in range(len(coins))]
        
        #dp of n x amount 
        
        def calc(amount,coins,n):
            
            
            if amount==0:
                return 1
            
            if n==-1 or amount<0:   return 0
            

            else:                
                if dp[n][amount]!=-1:
                    return dp[n][amount]
                
                else:
                    dp[n][amount]=calc(amount-coins[n],coins,n)+calc(amount,coins,n-1)
                    return dp[n][amount]
            
        return calc(amount,coins,len(coins)-1)