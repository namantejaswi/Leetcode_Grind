class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        
        flag=True
        
        
        for i in range(1,len(nums)):
            
            if nums[i]>=nums[i-1]:
                #everything is good
                pass
            
            elif nums[i]<nums[i-1]:
                
                if flag==False:
                    return False
                else:   
                    
                    flag=False
                    
                    
                    if i<2 or nums[i-2]<=nums[i]:
                        nums[i-1]=nums[i]   
                        
                    else:
                        nums[i]=nums[i-1]
                    
        return True
        