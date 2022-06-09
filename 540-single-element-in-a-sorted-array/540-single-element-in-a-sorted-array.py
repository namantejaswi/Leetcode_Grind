class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        
        lo=0
        hi=len(nums)-1
        mid=None
        
        if len(nums)==1:    return nums[0]
        
        if nums[0]!=nums[1]:
            return nums[0]
        
        if nums[-1]!=nums[-2]:
            return nums[-1]
        
        
        while(lo<=hi):
            mid =lo + (hi-lo)//2
            #print(lo,mid,hi)
            
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            
            if ((mid%2==0 and nums[mid]==nums[mid+1]) or (mid%2==1 and nums[mid]==nums[mid-1])):
             
            #Xor trick    
            #if nums[mid]==nums[mid^1]:
                lo=mid+1
            
            else:
                hi=mid-1
            
            
        
        
            
            