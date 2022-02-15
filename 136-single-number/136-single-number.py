class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        
        #print(0^13)
        #print(2^10)
        #print(2^10^2)
        #print(1^1^1)
        
        res=0
        
        for i in nums:
            res=res^i
            
        return res