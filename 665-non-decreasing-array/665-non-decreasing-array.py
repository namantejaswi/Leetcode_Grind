class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        
        flag=True
        
        #[3,4,2,3]
        
        
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
                        
                        #if the third elment and 1st element are in sync
                        #make the seccond element equal to the first
                        nums[i-1]=nums[i]   
                        
                    elif nums[i-1]>=nums[i]:
                        
                        #else make the third element equal to second
                        #because if we made it so far 1st and 2nd should already be in sync and we have checked for first and third so the only possiblity is that third and second are not in sync
                        nums[i]=nums[i-1]
                    
        return True
        