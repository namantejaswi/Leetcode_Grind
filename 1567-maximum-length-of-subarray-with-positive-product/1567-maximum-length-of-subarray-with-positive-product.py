class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        
        
        #dp[index][sign] sign represents 0 +ve product 1 -ve product ending at index
        
        
        
        #dp=[[0 for i in range(2)] for j in range(len(nums))]
      
        pve=[0]*len(nums)
        nve=[0]*len(nums)
        
        if nums[0]>0:
            pve[0]=1
            
        elif nums[0]<0:
            nve[0]=1
            
        mx=pve[0]
         #rest by default initialized to zero
        
        
        for i in range(1,len(nums)):
            
            if nums[i]>0:
            
                pve[i]=1+pve[i-1]
                
                
                if nve[i-1]>0:
                    
                    nve[i]=1+nve[i-1]
                    
                    
            if nums[i]<0:
                
                nve[i]=1+pve[i-1]
                
                
                if nve[i-1]>0:
                    
                    pve[i]=1+nve[i-1]
                    
                    
            mx=max(mx,pve[i])
    
        return mx  
        
        
        
        