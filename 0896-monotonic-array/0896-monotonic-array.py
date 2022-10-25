class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        
        inc=True
        dec=True
        for i in range(len(nums)-1):
            
            if nums[i+1]>=nums[i]:
                pass
            else:   inc=False
                
                
            if nums[i+1]<=nums[i]:
                pass
            else:   dec=False
                
                
        return inc or dec
        
        