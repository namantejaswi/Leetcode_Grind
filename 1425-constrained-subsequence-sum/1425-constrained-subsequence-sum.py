class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        
        
        q=deque()
        dp = [0]*len(nums)
        
        for r in range(len(nums)):
            
            if q and r-q[0]>k:     #if q greater than k
                q.popleft()
                
            if q:   dp[r] =dp[q[0]] +nums[r]        
                
            elif not q: dp[r] = nums[r]     
                
                
            while q and dp[q[-1]]<dp[r]:
                q.pop()
                
            if dp[r]>0: q.append(r)
                
                
        return max(dp)