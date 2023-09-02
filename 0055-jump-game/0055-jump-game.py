class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        
        
        max_reach = 0 
        
        for index in range(len(nums)):
            
            
            
            if index > max_reach:   return False
            
            #IF at any point there is an index where we can't reach we cant reach we simple break out
            
            
            
            else:  
                max_reach = max(max_reach,index+nums[index])
                
        return max_reach>=len(nums)-1