class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        
        
        l=0
        r=len(nums)-1
        
        opt=float('-inf')
        res=None
        nums.sort()
        
        while(l<r):
            
            if nums[l]+nums[r]>=k:
                r-=1
                
            elif nums[l]+nums[r]<k:
                opt=max(opt,nums[l]+nums[r])
                res=opt
                l+=1
                             
        if res: return res
        return -1
                
                
                
    