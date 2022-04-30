class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        
        
        
        
        mi=min(nums)
        mx=max(nums)
        
        if len(nums)!=len(set(nums)):   return False
        
        
        s=int((mx-mi+1) * (mi + mx) / 2)
        
        
        a=0
        for i in nums:
            a+=i
                        
        return s==a
            
            
            
            
