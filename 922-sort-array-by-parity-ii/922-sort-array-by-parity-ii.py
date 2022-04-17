class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        
        odd=[]
        even=[]

        
        for i in range(len(nums)):
            
            if i%2==0 and nums[i]%2!=0:
                odd.append(i)
                
                
            elif i%2==1 and nums[i]%2!=1:
                even.append(i)
                
                
        for i in range(len(odd)):
            
            nums[odd[i]],nums[even[i]]=nums[even[i]],nums[odd[i]]
            
            
        return nums