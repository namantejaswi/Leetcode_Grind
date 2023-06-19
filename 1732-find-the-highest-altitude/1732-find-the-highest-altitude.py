class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        
        mx=0
        
        curr=0
        for i in gain:
            curr+=i
            mx=max(curr,mx)
            
        return mx