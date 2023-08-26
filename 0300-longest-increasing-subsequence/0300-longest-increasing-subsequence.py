class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        
        dp = [ 1 for i in range(len(nums))] 
        
        # dp[index] stores the longest increasing subsequence till the index
        
        for end in range(1, len(nums)):     #the subsequence ending at endd
            
            for start in range(0, end ):#all the n-1 start points for the subs ending at n

                if nums[end]>nums[start]:
                    
                    dp[end] = max(dp[end], 1+ dp[start])
                    
        
        return max(dp)
        