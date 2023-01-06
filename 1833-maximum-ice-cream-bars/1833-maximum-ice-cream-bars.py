class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        
        
        costs.sort()
        
        cnt=0
        for i in costs:
            
            if coins>0:
                
                if i <=coins:
                    
                    coins-=i
                    cnt+=1
                    
                else: return cnt
                    
            else:   return cnt
                
        return cnt