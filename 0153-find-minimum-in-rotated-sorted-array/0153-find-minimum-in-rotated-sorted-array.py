class Solution:
    def findMin(self, nums: List[int]) -> int:
        
     
        #the array has 2 increasung parts  and the kink in between where the second part begins is the minimum.
        #if mid is greater than right that means the answer lies in the right section not including mid i.e. mid not a valid par
        #else the answer lies in the left part and mid could be the answer
    
        
        if len(nums)==1:    return nums[0]
        
        l = 0
        r = len(nums)-1
        
        #edge case smallest at first or last
        #if last element is greater than first elemeent means no rotation
        
        if nums[l]<=nums[r]:    return nums[l]
        
        
        ans = None
   
        
        while l<=r:
            
            mid = (l+r)//2
            #check if mid itself is the answer
            
            if mid!=0 and mid!=len(nums)-1 and nums[mid] < nums[mid - 1] and  nums[mid] < nums[mid + 1]:
                return nums[mid]
            
            
            if nums[mid]<=nums[r]:      #answer lies to the left mid could be answer
                ans = mid
                r = mid-1 
                
            else:                   #answer lies to the right mid is not  the answe
                l = mid +1
                
    
        return nums[ans]