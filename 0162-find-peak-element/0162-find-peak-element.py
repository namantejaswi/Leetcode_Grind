class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        
        #Peak element is the left most element which is greater than next next
        if len(nums)==1:    return 0
        
        l = 0 
        r = len(nums)-1
        ans = None
        
        
        if nums[l]>nums[l+1]:
            return l
        
        elif nums[r]>nums[r-1]: return r
        
        while l<=r:
            
            
            mid = (l+r)//2
            
            
            if nums[mid]>nums[mid+1]:
                pos = mid       #mid is valid we store it and greedily look for nect best in left
                r = mid-1
                
            else:
                l=mid+1
                
                
        return pos
                