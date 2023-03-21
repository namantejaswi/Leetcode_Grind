class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        
        #find the subarrays of zero and then add n*(n+1)/2  to ans
        
        
        l=0
        res=0
        
        
        for i in range(len(nums)):
            
            if nums[i]!=0:
                
                if l==0: pass
                
                else:   
                    
                    res+=(l*(l+1))/2
                    l=0
                    
            elif nums[i]==0:
                l+=1
                
                
        if l!=0:    res+=l*(l+1)/2
            
        return int(res)