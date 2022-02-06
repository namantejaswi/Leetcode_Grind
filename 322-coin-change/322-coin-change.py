class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        #first we try recurssively
    
        
        def count(coins, amount, dic):
            
            
            if amount==0:
                return 0
                    
            if amount not in dic:    
                dic[amount]=1+ min(count(coins,amount-coins[i],dic) if coins[i]<=amount else float("inf") for i in range(len(coins)))
            
            #bruh moment
            
            return dic[amount]
                
            
        dic={}
        if count(coins,amount,dic)==float("inf"): return -1
            
        else:   return count(coins,amount,dic)
                
        
                