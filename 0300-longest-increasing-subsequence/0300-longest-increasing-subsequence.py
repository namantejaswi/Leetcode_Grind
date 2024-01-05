class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        #dp[i] represents the length of longest subseq ending at i
        
        dp = [ 1 for i in range(len(nums))]
        
        for end in range(1,len(nums)):
            
            for start in range(0,end):
                
                if nums[end]>nums[start]:
                    
                    dp[end]=max(1+dp[start],dp[end])
                    
        return max(dp)