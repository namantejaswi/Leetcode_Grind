class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)

        
        def find_leftmost_equal_or_greater(target):
            
            pos = n
            l = 0
            r = len(nums)-1
            
            while l<=r:
                
                mid = (l+r)//2
                
                if nums[mid]>=target:
                    
                    pos = mid
                    r = mid-1   #mid valid but we try to find a tighter bound
                    
                else: 
                    l = mid+1   #mid invalid check fomr left = mid+1
                    
                    
            return pos
                
        p1=find_leftmost_equal_or_greater(target)
        p2=find_leftmost_equal_or_greater(target+1)-1


        if p1 == n or p1>p2:  return[-1,-1]

        return [p1,p2]
                    
                    
                    