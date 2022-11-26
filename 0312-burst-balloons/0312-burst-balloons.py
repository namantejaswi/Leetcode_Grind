class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        #Matrix chain multiplication 
        
        nums=[1]+nums+[1]       #append for edges
        
        dp=[[-1 for i in range(len(nums))]for j in range(len(nums))]
        
        
        def mcm(nums,l,r):
            
            if l>r:    return 0
            
            if dp[l][r]!=-1:    return dp[l][r]
            
            for k in range(l,r+1):
                
                coins=nums[l-1]*nums[k]*nums[r+1]
                coins+=mcm(nums,l,k-1)+mcm(nums,k+1,r)
                
                dp[l][r]=max(dp[l][r],coins)
            return dp[l][r]
        
        l=1 
        r=len(nums)-2
        return mcm(nums,l,r)
                
                
        
        