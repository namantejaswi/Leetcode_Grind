class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        
        min_len=len(nums)+1
        
        curr_sum=0
        
        left=0
        right=0
        
        for i in range(len(nums)):
            
            curr_sum+=nums[i]
            right+=1
            
            
            while(left<=right and curr_sum>=target):
                min_len=min(min_len,right-left)
                
                curr_sum=curr_sum-nums[left]
                left+=1
                
        if min_len==len(nums)+1:   return 0
        else: return min_len
            