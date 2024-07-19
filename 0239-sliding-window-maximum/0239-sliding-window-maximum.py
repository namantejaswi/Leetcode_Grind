class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        from collections import deque
        
        q = deque()
        res = []
        
        
        
        for r in range(len(nums)):
            
        
            #check if the left most index of our que is still within window
            
            while q and q[0]<=r-k:
                q.popleft()
        
        
            #check if the elment is largest than the left most element if so keep removing
            while q and nums[r]>nums[q[-1]]:
                
                q.pop()
                
                
            #add element to q
            
            q.append(r)
            
            
            #if we are at an index where window can be formed add largest element of the q that is the leftmost element
            
            if r>=k-1:          #if we have seen at least k elements
                
                res.append(nums[q[0]])
             
        #print(q)
        return res
                
                
        