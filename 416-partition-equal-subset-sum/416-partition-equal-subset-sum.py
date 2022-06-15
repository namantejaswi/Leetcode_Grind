class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        s=sum(nums)
        
        #we want to divide it into 2 subsets of equal sum
        #i.e s1 + s2 =s
        
        if s%2!=0:  return False
        
        
        dp =[[-1 for i in range((s//2)+1)] for j in range(len(nums))]
        #dp of nx s//2
        def subset(s,n,nums):
            
            if n==-1:
                return False
            
            if s==0:    return True
            
          
            if nums[n]<=s:
                if dp[n][s]!=-1:    return dp[n][s]
            
                else:   
                    dp[n][s]= subset(s-nums[n],n-1,nums) or subset(s,n-1,nums)
                    return dp[n][s]
                
            else:   
                if dp[n-1][s]!=-1:  return dp[n-1][s]
                else: 
                    dp[n-1][s]=subset(s,n-1,nums)
                    return dp[n-1][s]
            
        return subset(s//2,len(nums)-1,nums)
