class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        
        
        #Peak exists means the array before peak is increasing and array after peak is decreasing 
        
        # 
        
        l = 0
        r = len(nums)-1
        res = None
        
        
        while l<r:
            mid = (l+r)//2
            
            if nums[mid]>nums[mid+1]:   #mid can be peak 
                r = mid
                
            else:
                l = mid+1   #mmid canot be peak  mid+1 can be
                
                
        return l