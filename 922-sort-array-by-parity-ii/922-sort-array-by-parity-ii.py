class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        
        idx_odd=1
        idx_even=0
        
    
    
        while idx_even<len(nums) and idx_odd<len(nums):
    
            if  nums[idx_even]%2==0:
               
                idx_even+=2
                
            elif nums[idx_odd]%2==1:
                
                idx_odd+=2
                
                
            else:
                
                nums[idx_odd],nums[idx_even]=nums[idx_even],nums[idx_odd]
                
                idx_odd+=2
                idx_even+=2
   

        return nums