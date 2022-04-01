class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        
        max_p_e_h=1
        min_p_e_h=1
        maximum=0
        flag=0
        
        
        if(len(nums)==1):
            return(nums[0])
        
        for i in range(0,len(nums)):
            
            if(nums[i]>0):
                
                max_p_e_h*=nums[i]
                
                min_p_e_h=min(min_p_e_h*nums[i],1)
                flag=1
            
                
            elif(nums[i]<0):            
                
                temp=max_p_e_h
                
                max_p_e_h=max(min_p_e_h*nums[i],1)
                
                if(min_p_e_h*nums[i]>0):        #that is we foiund a pair of -ve
                    flag=1
                
                min_p_e_h=(temp*nums[i])
                                           
            elif(nums[i]==0):
                max_p_e_h=1
                min_p_e_h=1
                
                
            if(max_p_e_h>maximum):
                maximum=max_p_e_h
                
        if(flag==0):
            return(0)
            
        return maximum
                
                