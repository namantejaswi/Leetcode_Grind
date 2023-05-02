class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        
        count_negative=0
        
        for n in nums:
            
            if n==0:    return 0
            
            elif n<0:   count_negative+=1
                
                
        if count_negative%2==0: return 1
        
        else:   return -1