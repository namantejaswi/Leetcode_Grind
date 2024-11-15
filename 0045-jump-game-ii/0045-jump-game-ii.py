class Solution:
    def jump(self, nums: List[int]) -> int:
        
        
       #Dp O(n^2) solution 
    
    
        #dp=[float(inf) for i in range(len(nums))]
        #dp[0]=0
        
        #print(dp)
        #Each elment in dp represents the minimum steps to reach it
        
        
        #for i in range(len(nums)):
            
            
         #   for j in range(0,nums[i]+1):
            
          #      if i+j<len(nums):
                
           #         dp[i+j] =min(dp[i+j],dp[i]+1)
                
                
        #return (dp[-1])
             
        #Greedy O(n) 
        
        count=0
        curr=0
        farthest=0
        
        
        for i in range(len(nums)-1):
            
            farthest=max(farthest,i+nums[i])
            
            
            if i==curr:
                curr=farthest
                count+=1
                
        return count
        