class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        
        
        nums.sort()
        
        res=0
        for n in nums:
            if n>nums[res]:
                res+=1
                
        return res