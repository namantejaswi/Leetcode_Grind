class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        

        #Recurrsive non memoized
        #def calc(arr,s,idx):
            #print("called function param",arr,idx,s)
          #  if idx==len(multipliers)-1:
           #     return max(s+ (arr[0]*multipliers[idx]),(s+(arr[-1]*multipliers[idx])))
        
            #else:           
                
             #   return max(calc(arr[1:],s+(multipliers[idx]*arr[0]),idx+1) 
                               
              #                 , calc(arr[:-1],s+(multipliers[idx]*arr[-1]),idx+1) )
        
        #return calc(nums,0,0)
        
        
        #Memoized Recurrsive solution
        
        #dp={}
        
        #def calc(idx,lptr):
            
         #   if idx==len(multipliers):
          #      return 0
        
           # if (idx,lptr) in dp:    return dp[(idx,lptr)]
            
            #else:
                #max of when we select first first and when we select last
             #   dp[(idx,lptr)]=max((nums[lptr]*multipliers[idx]+calc(idx+1,lptr+1)), (nums[len(nums)-1-idx+lptr]*multipliers[idx]+calc(idx+1,lptr)))
                                                                                      
              #  return dp[(idx,lptr)]                                                                   
            
        #return calc(0,0)
    
    
        
        m = len(multipliers)
        n = len(nums)

        dp = [0] * (m + 1)

        for op in range(m - 1, -1, -1):
            next_row = dp.copy()
            # Present Row is now next_Row because we are moving upwards

            for left in range(op, -1, -1):

                dp[left] = max(multipliers[op] * nums[left] + next_row[left + 1],
                               multipliers[op] * nums[n - 1 - (op - left)] + next_row[left])

        return dp[0]
        
        
        