class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        
        
        ptr1=0
        ptr2=len(nums)-1
        
        
        while ptr2>ptr1:
            
            if nums[ptr1]%2 ==0 and nums[ptr2]%2==1:
                ptr1+=1
                ptr2-=1
                
            elif nums[ptr1]%2==0 and nums[ptr2]%2!=1:
                ptr1+=1
                
            elif nums[ptr1]%2!=0 and nums[ptr2]%2==1:
                ptr2-=1
                
            elif nums[ptr1]%2!=0 and nums[ptr2]%2!=1:
                nums[ptr1],nums[ptr2]=nums[ptr2],nums[ptr1]
                ptr1+=1
                ptr2-=1
                
                
        return nums