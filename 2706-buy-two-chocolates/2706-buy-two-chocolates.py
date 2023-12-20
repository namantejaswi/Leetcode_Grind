class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        min_1 = float('inf')
        min_2 = float('inf')
        
        
        for p in prices:
            
            if p <min_1:
                
                min_2 = min_1
                min_1 = p
                
            else:
                
                min_2 = min(p,min_2)
                
        #print(min_1,min_2)
        if money -min_1-min_2 >=0: return money-min_1-min_2
        else:   return money