class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        
        
        max_global=float('-inf')
        
        
        curr=0
        
        
        
        
        for i in range(len(nums)):
        
            curr+=nums[i]
        
            max_global=max(curr,max_global)

            
            if(curr<0):
                curr=0
                
            
        return max_global