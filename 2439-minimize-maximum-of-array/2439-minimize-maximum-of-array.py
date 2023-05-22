class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        
        s=0
        ans=0
        
        #we can best decrease to nums[i] to average of [0 to nums[i]]
        for i in range(len(nums)):
            
            s+=nums[i]
            ans = max(ans,(s+i)//(i+1))
            
        return ans