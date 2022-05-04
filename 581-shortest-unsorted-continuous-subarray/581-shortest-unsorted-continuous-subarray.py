class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        
        
        n_s=sorted(nums)
        
        start=len(nums)-1
        end=0
    
        
        for i in range(len(nums)):
            
            if nums[i]!=n_s[i]:
                
                start=min(i,start)
                
                end=max(i,end)      
                
              
        print(start,end)
        if end-start<=0:  return 0
        
        return end-start+1
        