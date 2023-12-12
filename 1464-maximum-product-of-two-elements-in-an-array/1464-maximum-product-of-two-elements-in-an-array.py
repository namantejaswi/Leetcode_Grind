class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        mx = None
        mx_2 = None
        
        
        if nums[0]>=nums[1]:
            mx=nums[0]
            mx_2=nums[1]
            
        else:   mx,mx_2 = nums[1], nums[0]
        
        
        for i in range(2,len(nums)):
            
            if nums[i] > mx:
                mx_2 = mx
                mx=nums[i]
                
            elif nums[i] <=mx and nums[i] >mx_2:   #lesss than equal to if we get same elment
                mx_2=nums[i]
        
        
        return (mx-1)*(mx_2-1)        
        
                