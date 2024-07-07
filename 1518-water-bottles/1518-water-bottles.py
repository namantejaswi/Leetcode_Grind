class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        
        k=numExchange
        res= numBottles
        
        
        
        def calc(empty,k):
            nonlocal res
            
            if empty<k: return
            
            else:
                
                res += empty//k
                calc(empty%k + empty//k,k)
                
                
    
        calc(numBottles,numExchange)
        
        
        return res
    