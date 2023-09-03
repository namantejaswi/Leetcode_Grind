class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        
        mx= float(-inf)
        
        curr = 0
        
        for i in range(len(nums)):
            
            curr += nums[i]
           
            if curr>mx: mx=curr  
            
            if curr<0:    
                curr = 0        #we ignore if our sum is -ve
        
               
                
           
        return mx