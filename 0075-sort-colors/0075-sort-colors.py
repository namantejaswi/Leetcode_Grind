class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    
        
        #We maintain the following invariant while iterating through index i
        
        # elements to left of left are all zeros
        # elements to the right of right are all twos
        # elments between i and right are unsorted and mixed
        # elments. between left and i-1 are ones
        
        # i iterates
        # --- L --- R---
        #.0.     1.   2 
        
        
        left = 0
        right=len(nums)-1
        
        i=0
        while i<=right:
            
            if nums[i]==0:
                nums[i],nums[left]= nums[left],nums[i]
                i+=1
                left+=1
                
            elif nums[i]==2:
                nums[i],nums[right]=nums[right],nums[i]
                right-=1
                
            elif nums[i]==1:    i+=1
                
        return nums
                
        