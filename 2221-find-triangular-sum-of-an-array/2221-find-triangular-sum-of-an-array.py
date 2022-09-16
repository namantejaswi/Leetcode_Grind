class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        cnt=0
        
        l=len(nums)-1
        while(l>0):
            
                        
            for i in range(l):
                
                nums[i]=(nums[i]+nums[i+1])%10
            
            
            l-=1
            
        return nums[0]