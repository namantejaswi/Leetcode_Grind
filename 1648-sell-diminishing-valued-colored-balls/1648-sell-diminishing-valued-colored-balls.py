class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
                
        
        
        lo=0
        hi=max(inventory)
        
        
        while hi-1>lo:
            
            mid = (lo + hi)//2
            possible_sell= sum(i - mid for i in inventory if i > mid)   
            if possible_sell>orders:   lo=mid
            else:   hi=mid
                
            
        #we can now select all balls less than right    
            
        count=0
        value=0
                        
        for i in inventory:
            if i>hi:
                count+=i-hi  
                
                value+= (i + hi + 1) * (i - hi) // 2
                
                
        #if we still can add some balls of price equal to right
        
        if count < orders:
            value += (orders - count) * hi    
            
        return value % ((10**9)+7)        
        
        
        
        
        
            
                
                
                
                
                
                
                
                
            