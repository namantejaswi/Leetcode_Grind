class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        mx = 0
        curr = 0
        
        for i in nums:
            
            if i==1:
                
                curr+=1
                mx=max(curr,mx)
                
                
            else:   curr=0
                
                
                
        return mx
                        
                