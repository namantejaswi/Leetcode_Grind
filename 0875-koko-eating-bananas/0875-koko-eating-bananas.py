class Solution:
    def minEatingSpeed(self, nums: List[int], h: int) -> int:
        
        
            
            
        #Find the appropiate, the min sufficient hourly rate k using binary search
        
        
        #highest we can have is max(nums)
        #lowest sum(nums)/h
        
        
        lo = max(1, math.floor(sum(nums)/h))
        
        hi = max(nums)
        
        while lo<hi:
            
            mid=(lo+hi)//2
            
            
            t=0
            
            for i in nums:  t+=math.ceil(i/mid)
                
            if t<=h: hi=mid
                
            else :   lo = mid+1
                
        return lo