class Solution:
    def minimumTotal(self, nums: List[List[int]]) -> int:
        
        
        #Memoization 
        dp= [ [-1]*len(nums) for i in range(len(nums))]

        #print(dp)
        
        
        def tri(r,c):
            
            if r==len(nums):
                return 0
            
            if dp[r][c]!=-1:    return dp[r][c]
            else:
                dp[r][c]= nums[r][c] + min(tri(r+1,c),tri(r+1,c+1))
                return dp[r][c]
            
        return tri(0,0)