class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        
        index_rem=dict()
        
        s=0        
        index_rem[0]=-1
        
        for i in range(len(nums)):
            
            
            s+=nums[i]
            
            rem=s%k

            if rem in index_rem:
                
                #The subarray is atleast of 2 in length
                if i-index_rem[rem]>1:  return True


            else:   index_rem[rem]=i
                
        return False


                    
        
     
                
            