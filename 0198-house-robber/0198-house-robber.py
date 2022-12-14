class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)<2: return max(nums)
        
        dp=[-1 for i in range(len(nums))]
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        
        def rob(index):
            
            if index<0:    return 0
            
            if dp[index]!=-1:   return dp[index]
            
            
            else:   
                
                pick_current= rob(index-2)+nums[index] 
                leave_current=rob(index-1)
                
                dp[index]=max(pick_current,leave_current)
                return dp[index]
                                
        rob(len(nums)-1)
        
        return dp[-1]