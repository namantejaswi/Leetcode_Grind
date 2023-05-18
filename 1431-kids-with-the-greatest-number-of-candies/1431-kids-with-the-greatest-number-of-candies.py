class Solution:
    def kidsWithCandies(self, candies: List[int], ex: int) -> List[bool]:
        
        
        mx = max(candies)
        
        
        for i in range(len(candies)):
            if candies[i]+ex>=mx:   candies[i]=True
                
            else:   candies[i]=False
                
                
        return candies