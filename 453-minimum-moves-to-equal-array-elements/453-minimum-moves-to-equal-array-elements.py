class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        mini=float('inf')
        s=0
        
        for i in nums:
            s+=i
            if i<mini:  mini=i
                
        n=len(nums)
        return s-(mini*n)