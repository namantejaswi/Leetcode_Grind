class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        
        curr=sum(nums)
        n=len(nums)
        l=0
        r=0
        mi=inf
        
        
        for r in range(n):
            
            curr-=nums[r]
            
            while l<=r and curr< x:
                
                curr+=nums[l]
                l+=1
                
            if curr ==x:
                mi = min(mi,(n-1-r+l))
                
        if mi!=inf:
            return mi
        return -1