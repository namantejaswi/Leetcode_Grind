class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        
        
        dp=[1 for i in nums]
        
        #Each element is on its own a increasing subsequence of length 1
        
        #Now let i be the index for which we have the lis  as dp[i]
        #let j be the index from zero to less than i untill w
        
        
        for i in range(1,len(nums)):
            
            for j in range(0,i):
                
                if(nums[i]>nums[j]):    # increasing => strictly greater than
                    
                    dp[i]=max(dp[j]+1,dp[i])
    
                  
        print(dp)
        return max(dp)     
                       
        
        
            
        
        
