class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        
        #dp= [ -2 for i in range(len(nums))]
        #say -1 is true and -2 is false
        #dp[0]=-1

        #for i in range(len(nums)):
            
         #   if dp[i]==-1:
          #      for j in range(nums[i]+1):
           #         if i+j<len(nums):
                        #print("at index",i,"setting index ",i+j, "to 1")
            #            dp[i+j]=-1
        #print(dp)
        #return dp[-1]==-1
        
        #Dp O(n^2)
        
        
        #Greedy shift Target
        
        destination = len(nums)-1
        
        for i in range(len(nums)-1,-1,-1):
            
            if i + nums[i]>=destination:
                
                destination = i
                
        return destination==0
            
        
            
            