class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        
        
        l=0
        r=len(nums)-1
        
        while(l<r):
        
            mid=(l+r+1)//2
            
            #if number of missing elment in first half is less than k look in second half else look in first half
            if nums[mid]-nums[0]-mid<k:        
    
                l=mid
                
            else:   r=mid-1
                
        return nums[0]+k+l